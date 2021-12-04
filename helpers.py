def read_lines(filename):
  """
  Read lines from a file.
  """
  file = open(filename, "r")
  lines = []
  for line in file:
    lines.append(line.strip())
  file.close()
  return lines
