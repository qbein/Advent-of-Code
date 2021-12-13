import helpers
import numpy as np

def part01():
  lows = list(map(
    lambda _: _[2],
    find_low_points(helpers.read_lines("data/09.txt"))
    ))
  
  result = len(lows) + sum(lows)

  print("December 9, Part 1; result: {0}".format(result))
  assert result == 508

def part02():
  basins = []
  lines = helpers.read_lines("data/09_sample.txt")
  lows = find_low_points(lines)

  for low in lows:
    basins.append(collect_basin(lines, low[0], low[1]))
  
  basins.sort(key=lambda _:len(_))
  print(basins)
  print(list(map(lambda _:len(_), basins[-3:])))

  result = np.prod(list(map(lambda _:len(_), basins[-3:])))
  print("December 9, Part 2; result: {0}".format(result))
  assert result == 479

def collect_basin(lines, y, x):
  basin = []

  while(x >= 0 and lines[y][x] != '9'):  
    x -= 1

  start = y, x

  _y = y
  while(_y >= 0):
    line = collect_line(lines, y, x, start)
    if(len(line) == 0):
      break
    basin.append([int(lines[_[0]][_[1]]) for _ in line])
    y -= 1

  _y = y+1
  while(_y < len(lines)):
    line = collect_line(lines, y+1, x, start)
    if(len(line) == 0):
      break
    basin.append([int(lines[_[0]][_[1]]) for _ in line])
    y += 1

  return basin

def collect_line(lines, y, x, start):
  line = []
  while(x >= 0 and lines[y][x] != '9'):
    x -= 1

  while(x < start[1] or lines[y][x] != '9'):
    if(lines[y][x] != '9'):
      line.append((y, x))
    x += 1
  return line

def find_low_points(lines):
  low_points = []
  
  for row, line in enumerate(lines):
    for column, character in enumerate(line):
      current = int(character)

      left:int = None
      right:int = None
      top:int = None
      bottom:int = None

      if(row > 0):
        top = int(lines[row-1][column])
      if(row < len(lines)-1):
        bottom = int(lines[row+1][column])
      if(column > 0):
        left = int(lines[row][column-1])
      if(column < len(line)-1):
        right = int(lines[row][column+1])

      if((top is None or top > current)
        and (left is None or left > current)
        and (right is None or right > current)
        and (bottom is None or bottom > current)):
        low_points.append((row, column, current))

  return low_points