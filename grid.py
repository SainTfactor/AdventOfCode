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

  def __init__(self, grid):
    self._grid = grid

  # 0,0 is bottom left, so translation is needed
  def at(self, x,y):
    grid = self._grid
    if y == len(grid):
      return None #out of bounds
    if x == len(grid[0]):
      return None #out of bounds
    if x < 0 or y < 0:
      return None #out of bounds
    return grid[len(grid)-y-1][x]
  
  def print_grid(self):
    grid = self._grid
    for i in grid:
      print("".join(i))
  
  def grid_maxs(self):
    grid = self._grid
    #returns max_x and max_y
    return len(grid[0]), len(grid)
  
  def generate_grid_scan(self):
    grid = self._grid
    max_x, max_y = self.grid_maxs()
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
