def part01():
  """
  Advent of Code 2021; December 1st, part 1
  """
  previous_depth = -1
  increase_count = 0

  file = open("data_01.txt", "r")
  for line in file:
    current_depth = int(line)
    if(previous_depth > 0 and current_depth > previous_depth):
      increase_count += 1
    previous_depth = current_depth

  file.close()

  result = increase_count
  print("December 1, Part 1; result: {0}".format(result))
  assert(result == 1316)

def part02():
  """
  Advent of Code 2021; December 1st, part 2
  """
  increase_count = 0
  depth_list = []
  file = open("data_01.txt", "r")
  for line in file:
    current_depth = int(line)
    depth_list.append(current_depth)
    if(len(depth_list) < 4):
      continue

    if(sum(depth_list[1:4]) > sum(depth_list[0:3])):
      increase_count += 1
    depth_list.pop(0) 

  file.close()

  result = increase_count
  print("December 1, Part 2; result: {0}".format(result))
  assert(result == 1344)
