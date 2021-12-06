import helpers

def part01():
  fish = evolve_fish("data/06.txt", 80)

  result = len(fish)
  print("December 6, Part 1; result: {0}".format(result))
  assert(result == 372984)

def part02():
  fish = evolve_fish("data/06_test.txt", 256)
  
  result = len(fish)
  print("December 6, Part 2; result: {0}".format(result))
  assert(result == -1)

def evolve_fish(filename, days):
  fish = []
  for line in helpers.yield_lines(filename):
    fish = [int(x) for x in line.split(",")]

  for day in range(0, days):
    advance_day(fish)

  return fish

def advance_day(state):
  new_fish = []
  for index, timer in enumerate(state):
    if(timer == 0):
      new_fish.append(8)
      state[index] = 6
    else:
      state[index] = timer-1
  state.extend(new_fish)