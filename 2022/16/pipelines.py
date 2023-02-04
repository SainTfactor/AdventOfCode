from pathlib import Path
import re

import graphviz
from matplotlib import colormaps



class Pipelines:
    def __init__(self, input_text):
        self.valves = {}
        self.player_location = None
        self.clock = 0
        self.max_clock = 30
        for line in input_text.splitlines():
            valve = Valve.parse_input(line)
            self.valves[valve.name] = valve
            if self.player_location is None:
                self.player_location = valve.name
        self.calc_distances()
        self.color_map = colormaps.get_cmap('plasma').resampled(self.max_potential + 1)

    def move(self, name):
        a , b = self.player_location, name
        if self.valves[a].name in self.valves[b].connections and self.valves[b] in self.valves[a].connections:
            raise Exception(f'Connection not found between {a} and {b}')
        self.player_location = name
        self.tick()

    def open_valve(self):
        valve = self.valves[self.player_location]
        if valve.open:
            raise Exception(f'Valve {valve.name} is already open')
        else:
            self.tick()
            valve.open = True

    def tick(self):
        self.clock += 1
        for valve in self.valves.values():
            valve.tick()

    def calc_distances(self):
        queue = [self.player_location]
        self.valves[self.player_location].distance = 0
        self.valves[self.player_location].potential = 0
        checked = [self.player_location]
        self.max_potential = 0

        def visit_neighbors(location):
            for neighbor in self.valves[location].connections:
                if neighbor not in checked:
                    queue.append(neighbor)
                    checked.append(neighbor)
                    self.valves[neighbor].distance = self.valves[location].distance + 1
                    self.valves[neighbor].potential = (self.valves[neighbor].flow_rate * self.max_clock) - ((self.valves[neighbor].distance + 1) * self.valves[neighbor].flow_rate)
                    self.max_potential = max([self.max_potential, self.valves[neighbor].potential])

        while queue:
            location = queue.pop(0)
            visit_neighbors(location)   
                

    def graph(self):
        dot = graphviz.Graph(format='svg')
        dot.attr(bgcolor='black')
        dot.strict = True
        self.valves[self.player_location].open = True
        for  name, valve in self.valves.items():
            if name == self.player_location:
                shape = 'diamond'
            else:
                shape = 'box'

            if valve.open:
                fillcolor = '#001155'
            else:
                fillcolor = '#111111'

            color = '#{0:0>2x}{1:0>2x}{2:0>2x}'.format(*[int(color * 255) for color in self.color_map.colors[valve.potential][0:3]])
            


            label = f'{name}\nF:{valve.flow_rate}\nD:{valve.distance}\nP:{valve.potential}'
            dot.node(name, label=label, shape=shape, color=color, fontcolor='#ffffff', style='filled', fillcolor=fillcolor, fontsize='10', fontname='Courier')
            for connection in valve.connections:
                dot.edge(name, connection, color='#999999')
        dot.render()

class Valve:
    @classmethod
    def parse_input(cls, line):
        regex = re.compile(r'Valve (\w\w) has flow rate=(\d+); \w+ \w+ to \w+ (.*)')
        name, flow_rate, connections = regex.findall(line)[0]
        connections = [connection.strip() for connection in connections.split(',')]
        return cls(name, flow_rate, *connections)

    def __init__(self, name, flow_rate, *connections):
        self.name = name
        self.flow_rate = int(flow_rate)
        self.connections = connections
        self.open = False
        self.output = 0

    def tick(self):
        if self.open:
            self.output += self.flow_rate
            return self.output
        else:
            return 0


def get_paths(pipeline: Pipelines):
    valves = pipeline.valves
    current_valve = valves[pipeline.player_location]
    connections = [valves[name] for name in current_valve.connections]


if __name__ == '__main__':
    data = Path('input.txt').read_text()
    pl = Pipelines(data)
    pl.graph()