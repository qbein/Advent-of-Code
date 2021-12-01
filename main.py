
def part01():
  """
  Advent of Code 2021 December 1st, part 1
  """
  before = -1
  count = 0

  file = open("data_01.txt", "r")
  for line in file:
    now = int(line)
    if(before > 0 and now > before):
      count += 1
    before = now

  print("Part 1; count: {0}".format(count))

def part02():
  """
  Advent of Code 2021 December 1st, part 2
  """
  count = 0
  list = []
  file = open("data_01.txt", "r")
  for line in file:
    now = int(line)
    list.append(now)
    if(len(list) < 4):
      continue

    if(sum(list[1:4]) > sum(list[0:3])):
      count += 1
    list.pop(0) 

  print("Part 2; count: {0}".format(count))

part01()
part02()
