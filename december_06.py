import helpers
import numpy as np

def part01():
  result = num_fish_after_days("data/06.txt", 80)
  print("December 6, Part 1; result: {0}".format(result))
  assert result == 372984

def part02():
  result = num_fish_after_days("data/06.txt", 256)
  print("December 6, Part 2; result: {0}".format(result))
  assert result == 1681503251694

def num_fish_after_days(filename, days):
  fish = dict.fromkeys(range(0, 9), 0)
  for line in helpers.yield_lines(filename):
    unique, counts = np.unique(
      [int(x) for x in line.split(",")], 
      return_counts=True
      )

    for index, item in enumerate(unique):
      fish[item] = counts[index]

  for day in range(0, days):
    advance_day(fish)
  
  return sum(fish.values())

def advance_day(state):
  new_count = state[0]
  for timer in range(1, 9):
    state[timer-1] = state[timer]
  state[8] = new_count
  state[6] += new_count

