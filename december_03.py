def part01():
  """
  Advent of Code 2021; December 3nd, part 1
  """
  gamma = ""
  epsilon = ""

  file = open("data_03.txt", "r")
  counts = [0] * 12
  line_count = 0
  for line in file:
    line_count += 1
    for index, character in enumerate(line.strip()):
      counts[index] += int(character)

  file.close()
  
  for count in counts:
    if count > line_count / 2:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"

  print("December 3, Part 1; result: {0}".format(int(gamma, 2) * int(epsilon, 2)))
