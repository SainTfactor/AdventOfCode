from copy import deepcopy
from collections import defaultdict
from pathlib import Path
import re
import statistics

import graphviz
from matplotlib import colormaps

class MaxCyclesReached(Exception):
    pass


class Pipelines:
    def __init__(self, input_text):
        self.valves = {}
        self.player_location = None
        self.clock = 0
        self.max_clock = 30
        self.total_value = 0
        self.moves = []
        self.open_times = []
        for line in input_text.splitlines():
            valve = Valve.parse_input(line)
            self.valves[valve.name] = valve
            if self.player_location is None:
                self.player_location = valve.name
        self.moves.append(self.player_location)
        self.calc_distances()

    def ranked_potentials(self):
        potentials = []
        for valve in self.valves.values():
            if valve.potential > 0:
                potentials.append(valve)
        potentials = sorted(potentials, key=lambda v: v.potential, reverse=True)
        if len(potentials) > 4:
            potentials = potentials[0:4]
        return potentials


    def move(self, name):
        destination_valve = self.valves[name]
        distance = destination_valve.distance
        for _ in range(destination_valve.distance):
            self.tick()
        self.player_location = name
        self.moves.append(name)
        self.calc_distances()
        return distance

    def open_valve(self):
        valve = self.valves[self.player_location]
        if valve.open:
            raise Exception(f'Valve {valve.name} is already open. Moves: {self.moves}')
        else:
            self.tick()
            valve.open = True
            self.open_times.append(self.clock)

    def tick(self):
        if self.clock >= self.max_clock:
            raise MaxCyclesReached('Max clock cycles reached.')
        self.clock += 1
        self.total_value = sum([valve.tick() for valve in self.valves.values()])
            

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
                    if self.valves[neighbor].open:
                        self.valves[neighbor].potential = 0
                    else:
                        self.valves[neighbor].potential = max([(self.valves[neighbor].flow_rate * (self.max_clock - self.clock - 1)) - ((self.valves[neighbor].distance + 1) * self.valves[neighbor].flow_rate), 0])
                    self.max_potential = max([self.max_potential, self.valves[neighbor].potential])

        while queue:
            location = queue.pop(0)
            visit_neighbors(location)   
        
        self.color_map = colormaps.get_cmap('plasma').resampled(self.max_potential + 1)
                

    def graph(self):
        dot = graphviz.Graph(format='svg', filename=f'out/pl_{self.clock}_{"_".join(self.moves)}')
        dot.attr(bgcolor='black', label=f'[ CLOCK: {self.clock} | TOTAL VALUE: {self.total_value} | MOVES: {self.moves} ]', fontcolor='#dddddd', fontsize='10', fontname='Courier')
        dot.strict = True

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


if __name__ == '__main__':
    data = Path('sample_input.txt').read_text()
    pl = Pipelines(data)
    queue = [Pipelines(data)]
    results = {}
    while queue:
        print(len(queue))
        pl = queue.pop(0)
        ranked_potentials = pl.ranked_potentials()
        if ranked_potentials:
            for valve in ranked_potentials:
                pl_copy = deepcopy(pl)
                distance = pl_copy.move(valve.name)
                pl_copy.open_valve()
                queue.append(pl_copy)
        else:
            while True:
                try:
                    pl.tick()
                except MaxCyclesReached:
                    results[','.join(pl.moves)] = pl
                    break      

    best_move = None
    max_result_value = 0
    best_pl = None
    for move, pl in results.items():
        if pl.total_value > max_result_value:
            max_result_value = pl.total_value
            best_move = move
            best_pl = pl
    print(best_move)
    print(max_result_value)
    print(best_pl.open_times)
    print(best_pl.moves)
    best_pl.graph()

