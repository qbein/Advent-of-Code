import helpers

def part01():
  grid = []
  for line in helpers.yield_lines("data/11.txt"):
    grid.append([ int(x) for x in list(line) ])

  result = 0

  for i in range(0, 100):
    result += step(grid)
    
  print("December 11, Part 1; result: {0}".format(result))
  assert result == 1627

def part02():
  grid = []
  for line in helpers.yield_lines("data/11.txt"):
    grid.append([ int(x) for x in list(line) ])

  flash_count = 0

  result = 0
  while(flash_count != len(grid) * len(grid[0])):
    flash_count = step(grid)
    result += 1
    
  print("December 11, Part 2; result: {0}".format(result))
  assert result == 329

def yield_items(grid):
  for y, line in enumerate(grid):
    for x, value in enumerate(line):
      yield (y, x)

def step(grid):
  flash_count = 0

  for y, x in yield_items(grid):
    grid[y][x] += 1

  flashed = []
  for y, x in yield_items(grid):
    if(grid[y][x]>9):
      flashed.append((y, x))
  len_y = len(grid)
  len_x = len(grid[0]) if len_y > 0 else 0
  while(len(flashed)):
    flash_count += len(flashed)
    new_flashed = []
    for y, x in flashed:
      miny = max(0, y-1)
      minx = max(0, x-1)
      maxy = min(len_y, y+2)
      maxx = min(len_x, x+2)
      for _y in range(miny, maxy):
        for _x in range(minx, maxx):
          if(grid[_y][_x] > 0):
            grid[_y][_x] += 1
          if(grid[_y][_x] == 10):
            new_flashed.append((_y, _x))
      
      for y, x in yield_items(grid):
        if(grid[y][x] > 9):
          grid[y][x] = 0
      
      flashed = new_flashed
  
  for y, x in yield_items(grid):
    if(grid[y][x] > 9):
      grid[y][x] = 0

  return flash_count