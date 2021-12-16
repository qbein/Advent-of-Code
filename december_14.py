import helpers

def part01():  
  template:str = None
  rules:dict = None

  for line in helpers.yield_lines("data/14.txt"):
    if(template is None):
      template = line.strip()
      continue
    if(rules is None):
      rules = {}
      continue
    key, insert = line.split(" -> ")
    rules[key] = insert

  input = template
  for step in range(0, 10):
    output = ""
    l = len(input)
    for i in range(0, l):
      output += input[i]
      if(i < l-1):
        key = input[i] + input[i+1]
        if key in rules:
          output += rules[key]
    input = output
  
  stats = {}
  for c in output:
    if c not in stats:
      stats[c] = 0
    stats[c] += 1

  result = stats[max(stats, key=stats.get)] - stats[min(stats, key=stats.get)]
  
  print("December 14, Part 1; result: {0}".format(result))
  assert result == 2408

def part02():
  print(2)
