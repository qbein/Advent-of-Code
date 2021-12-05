def read_lines(filename):
  """
  Read lines from a file.
  """

  lines = []
  for line in yield_lines(filename):
    lines.append(line)
  return lines

def yield_lines(filename):
  """
  Yield lines from a file.
  """
  file = open(filename, "r")
  for line in file:
    yield line.strip()
  file.close()
