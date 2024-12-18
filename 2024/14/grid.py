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
  
  def print(self, print_function=lambda x: x):
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

