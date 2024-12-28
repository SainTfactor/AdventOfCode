  def dijkstrafy(grid, start_node):
    for node, x, y in grid:
      node["visited"] = node["tile"] == "#"
      if (x,y) == start_node:
        node["distance"] = 0
        node["direction"] = Grid.Directions.LEFT
      else:
        node["distance"] = None
        node["direction"] = None

  def update_neighbor_function(grid, n,x,y):
    n["visited"] = True
    direction = n["direction"]
    for turncost in [1001,2001,1001,1]: # left, back, right, straight
      direction = Grid.Directions.turn_left(direction)
      next_node, next_x, next_y = grid.next(x, y, direction)
      if next_node["tile"] != "#":
        if next_node["distance"] == None or next_node["distance"] > (turncost + n["distance"]):
          next_node["distance"] = turncost + n["distance"]
          next_node["direction"] = direction
          next_node["previous_node"] = (x,y)
          next_node["updated_count"] += 1
      

  def dijkstra_walk(grid, start, update=update_neighbor_function):
    dijkstrafy(grid, start)
    while any([not n["visited"] for n,x,y in grid]):
      # get minimum node
      min_grid = None
      for n,x,y in grid:
        if not n["visited"] and n["distance"] != None:
          if min_grid == None or min_grid[0]["distance"] > n["distance"]:
            min_grid = (n,x,y)

      # update neighbors
      update(grid, *min_grid)
