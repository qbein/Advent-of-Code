import helpers

def part01():
  positions = []
  for line in helpers.yield_lines("data/07.txt"):
    positions = list(map(int, line.split(",")))
  
  result = find_meeting_position(positions)
  print("December 7, Part 1; result: {0}".format(result))
  assert result == 323647

def part02():
  for line in helpers.yield_lines("data/07.txt"):
    positions = list(map(int, line.split(",")))
  
  result = find_meeting_position(positions, True)
  print("December 7, Part 2; result: {0}".format(result))
  assert result == 87640209

# https://stackoverflow.com/a/61720945
def sum_range(f, t):
    dist = f - t
    return f * (dist+1) + int(dist*(dist+1)/2)

def find_meeting_position(positions, incremental=False):
  min_pos, max_pos = min(positions), max(positions)
  
  min_steps:int = None
  for i in range(min_pos, max_pos+1):
    steps = 0
    for position in positions:
      distance = abs(position-i)
      if distance > 0 and incremental:
        steps += sum_range(0, distance+1)
      else:
        steps += distance
    
    if min_steps is None or steps < min_steps:
      min_steps = steps

  return min_steps
