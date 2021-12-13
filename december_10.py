import helpers

def part01():
  pairs = [
    ("(", ")", 3),
    ("[", "]", 57),
    ("{", "}", 1197),
    ("<", ">", 25137)
  ]

  result = 0

  for line in helpers.yield_lines("data/10.txt"):
    stack = []
    for index, character in enumerate(line):
      x = next((x for x in pairs if character == x[0]), None)
      if(x is not None):
        stack.append(x)
      else:
        x = next((x for x in pairs if character == x[1]), None)
        if(x is not None):
          y = stack.pop()
          if(x[1] != y[1]):
            result += x[2]
            break

  print("December 10, Part 1; result: {0}".format(result))
  assert result == 266301 

def part02():
  pairs = [
    ("(", ")", 1),
    ("[", "]", 2),
    ("{", "}", 3),
    ("<", ">", 4)
  ]

  incomplete_stacks = []
  
  for line in helpers.yield_lines("data/10.txt"):
    stack = []
    for index, character in enumerate(line):
      x = next((x for x in pairs if character == x[0]), None)
      if(x is not None):
        stack.append(x)
      else:
        x = next((x for x in pairs if character == x[1]), None)
        if(x is not None):
          y = stack.pop()
          if(x[1] != y[1]):
            break
    else:
      if(len(stack) > 0):
        incomplete_stacks.append(stack)
  
  row_scores = []
  for line in incomplete_stacks:
    row_score = 0
    for index, x in reversed(list(enumerate(line))):
      row_score *= 5
      row_score += x[2]
    row_scores.append(row_score)

  row_scores.sort()
  result = row_scores[int(len(row_scores) / 2)]

  print("December 10, Part 1; result: {0}".format(result))
  assert result == 3404870164
