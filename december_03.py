import helpers

def part01():
  """
  Advent of Code 2021; December 3rd, part 1
  """
  gamma = ""
  epsilon = ""

  lines = helpers.read_lines("data_03.txt")
  counts = count_occurences(lines);

  threshold = len(lines) / 2
  for count in counts:
    if count > threshold:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"

  result = int(gamma, 2) * int(epsilon, 2)
  print("December 3, Part 1; result: {0}".format(result))
  assert(result == 2724524)

def part02():
  """
  Advent of Code 2021; December 3rd, part 1
  """
  
  oxygen = ""
  co2 = ""

  lines = helpers.read_lines("data_03.txt")

  oxygen = find_rating(lines, True)
  co2 = find_rating(lines, False)
  
  result = int(oxygen, 2) * int(co2, 2)
  print("December 3, Part 1; result: {0}".format(result))
  assert(result == 2775870)

def filter_by_occurence(item, index, value):
  return item[index] == value

def count_occurences(lines):
  counts = []
  for line in lines:
    for index, character in enumerate(line):
      if(len(counts) <= index):
        counts.append(int(character))
      else:
        counts[index] += int(character)
  return counts

def find_rating(_lines, find_dominant):
  lines = _lines.copy()
  for index in range(len(lines[0])):
    threshold = len(lines) / 2
    counts = count_occurences(lines)
    
    dominant = True if counts[index] >= threshold else False
    find_bit = dominant if find_dominant else not dominant
    filter_bit = '1' if find_bit else '0'

    lines = list(filter(lambda line: line[index] == str(filter_bit), lines))
    
    if(len(lines) == 1):
      return lines[0]
