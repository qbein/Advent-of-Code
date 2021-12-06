import helpers
import numpy as np

def part01():
  result = find_overlapping_lines()
  
  print("December 5, Part 1; result: {0}".format(result))
  assert(result == 5835)

def part02():
  result = find_overlapping_lines(True)
  print("December 5, Part 2; result: {0}".format(result))
  assert(result == 17013)
  
def find_overlapping_lines(count_diagonal = False):
  lines = []
  for line in helpers.yield_lines("data/05.txt"):
    _a, _b = line.split(" -> ")
    a = np.array(_a.split(",")).astype(int)
    b = np.array(_b.split(",")).astype(int)

    if(count_diagonal or any(i == 0 for i in a ^ b)):
      lines.append([a, b])

  dimension = np.amax(lines)
  grid = np.zeros((dimension+1, dimension+1), dtype=int)  
  
  for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]

    if(x1 == x2):
      for y in range(min(y1, y2), max(y1, y2)+1):
        grid[y][x1] += 1
    elif(y1 == y2):
      for x in range(min(x1, x2), max(x1, x2)+1):
        grid[y1][x] += 1
    else:
      # This is messy; should find cleaner way to configure ranges
      stepx = -1 if x1 > x2 else 1
      stepy = -1 if y1 > y2 else 1
      range_x = [*range(x1, x2 + stepx, stepx)]
      range_y = [*range(y1, y2 + stepy, stepy)]
      for index, x in enumerate(range_x):
        y = range_y[index]
        grid[y][x] += 1
      
  return (grid.flatten() > 1).sum()