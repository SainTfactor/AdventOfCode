#!/usr/bin/env python3

class Grid:
  
  class Directions:
    UP = 0
    UP_RIGHT = 1
    RIGHT = 2
    DOWN_RIGHT = 3
    DOWN = 4
    DOWN_LEFT = 5
    LEFT = 6
    UP_LEFT = 7

    def get_all():
      for direction in range(8):
        yield direction

    def turn_right(direction):
      return (direction + 2) % 8

    def turn_left(direction):
      return (direction - 2) % 8
    
    def half_turn_right(direction):
      return (direction + 1) % 8

    def half_turn_left(direction):
      return (direction - 1) % 8

  def __init__(self, grid):
    self._grid = grid

  def __iter__(self):
    for x,y in self.generate_grid_scan():
      yield self.at(x,y), x, y

  def rows(self):
    num_rows = len(self._grid)
    for row_id in range(num_rows):
      yield self._grid[num_rows-row_id-1]
  
  def cols(self):
    num_cols = len(self._grid[0])
    for col_id in range(num_cols):
      yield [i[col_id] for i in self._grid]

  # 0,0 is bottom left, so translation is needed
  def at(self, x,y):
    grid = self._grid
    if y >= len(grid):
      return None #out of bounds
    if x >= len(grid[0]):
      return None #out of bounds
    if x < 0 or y < 0:
      return None #out of bounds
    return grid[len(grid)-y-1][x]
  
  def set(self, x, y, new_value):
    grid = self._grid
    if y >= len(grid):
      raise Exception #out of bounds
    if x >= len(grid[0]):
      raise Exception #out of bounds
    if x < 0 or y < 0:
      raise Exception #out of bounds
    grid[len(grid)-y-1][x] = new_value
  
  def print(self, print_function=lambda x: str(x)):
    grid = self._grid
    for i in grid:
      print("".join([print_function(j) for j in i]))
  
  def maxs(self):
    grid = self._grid
    #returns max_x and max_y
    return len(grid[0]), len(grid)
  
  def generate_grid_scan(self):
    grid = self._grid
    max_x, max_y = self.maxs()
    for y in range(max_y):
      for x in range(max_x):
        yield x,y
  
  def next(self, x, y, direction):
    grid=self._grid
    if direction == self.Directions.UP:
      return self.at(x,y+1), x, y+1
    elif direction == self.Directions.UP_RIGHT:
      return self.at(x+1,y+1), x+1, y+1
    elif direction == self.Directions.RIGHT:
      return self.at(x+1,y), x+1, y
    elif direction == self.Directions.DOWN_RIGHT:
      return self.at(x+1,y-1), x+1, y-1
    elif direction == self.Directions.DOWN:
      return self.at(x,y-1), x, y-1
    elif direction == self.Directions.DOWN_LEFT:
      return self.at(x-1,y-1), x-1, y-1
    elif direction == self.Directions.LEFT:
      return self.at(x-1,y), x-1, y
    elif direction == self.Directions.UP_LEFT:
      return self.at(x-1,y+1), x-1, y+1
    else:
      raise Exception

  def region(self, x, y, ret_val=None):
    if ret_val == None:
      ret_val = []
    ret_val.append((x,y))
    node_value = self.at(x, y)

    for new_value, new_x, new_y in self.neighbors(x,y):
      if new_value == node_value and not (new_x, new_y) in ret_val:
        self.region(new_x, new_y, ret_val)
    
    return ret_val

  def neighbors(self, x, y):
    direction = Grid.Directions.UP
    for i in range(4):
      yield self.next(x,y,direction)
      direction = Grid.Directions.turn_right(direction)

  def all_neighbors(self, x, y):
    direction = Grid.Directions.UP
    for i in range(8):
      yield self.next(x,y,direction)
      direction = Grid.Directions.half_turn_right(direction)

  def all_regions(self):
    regions = []
    all_matched_nodes = []
    for node, x, y in self:
      if not (x,y) in all_matched_nodes:
        region = self.region(x,y)
        regions.append(region)
        for item in region:
          all_matched_nodes.append(item)
    return regions

  def find_start(self, target_char="S"):
    for n,x,y in self:
      if n == target_char:
        return x,y
    raise Exception("No start character found!")

  def _create_cost_grid(self, start_node, obstacle_list = ["#"]):
    self._cost_grid = Grid([[{ "tile" : item } for item in line] for line in self._grid])
    for node, x, y in self._cost_grid:
      node["visited"] = node["tile"] in obstacle_list 
      if (x,y) == start_node:
        node["distance"] = 0
      else:
        node["distance"] = None

  def _simple_cost_function(self, node, x, y, obstacle_list = ["#"]):
    node["visited"] = True
    direction = Grid.Directions.UP
    for _ in range(4):
      next_node, next_x, next_y = grid.next(x, y, direction)
      direction = Grid.Directions.turn_right(direction)
      if not next_node["tile"] in obstacle_list:
        if next_node["distance"] == None or next_node["distance"] >= (1 + node["distance"]):
          next_node["distance"] = 1 + node["distance"]
          if not "previous_nodes" in next_node:
            next_node["previous_nodes"] = [(x,y)]
          else:
            next_node["previous_nodes"].append((x,y))


  def calculate_path_costs(self, start, end=None, obstacle_list=["#"], cost_function=_simple_cost_function):
    self._create_cost_grid(start, obstacle_list)
    while any([not n["visited"] for n,x,y in self._cost_grid]):
      # get minimum node
      min_grid = None
      for n,x,y in self._cost_grid:
        if not n["visited"] and n["distance"] != None:
          if min_grid == None or min_grid[0]["distance"] > n["distance"]:
            min_grid = (n,x,y)

      # update neighbors
      cost_function(self._cost_grid, *min_grid)

      if end != None and (x,y) == end:
        return 

  def path_cost_to(self, end):
    if self._cost_grid == None:
      raise Exception
    return self._cost_grid.at(*end)["distance"]


  def _path_check_function(cur, nxt):
    node, x, y = cur
    next_node, next_x, next_y = nxt
    return "previous_nodes" in node and (next_x,next_y) in node["previous_nodes"]

  def print_paths(self, end, valid_next_step_function=_path_check_function):
    if self._cost_grid == None:
      raise Exception
    grid = self._cost_grid
    point = grid.at(*end)
    check_nodes = [(point, *end)]

    while len(check_nodes) > 0:
      node, x, y = check_nodes.pop()
      direction = Grid.Directions.UP
      node["path_part"] = True
      for _ in range(4):
        next_node, next_x, next_y = grid.next(x,y,direction)
        direction = Grid.Directions.turn_right(direction)
        if next_node["distance"] != None and not "path_part" in next_node and valid_next_step_function((node, x, y), (next_node, next_x, next_y)):
          check_nodes.append((next_node, next_x, next_y))

    for n,x,y in grid:
      #print("{},{} ({}): {}, {}".format(x,y,n["tile"],n["distance"],n["previous_nodes"] if "previous_nodes" in n else "No Previous"))
      pass

    grid.print(lambda x: "O" if "path_part" in x else x["tile"])

  def calculate_cost_total(self, total_cost_function):
    if self._cost_grid == None:
      raise Exception
    return total_cost_function(self._cost_grid)
