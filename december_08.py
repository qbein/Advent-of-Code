import helpers

def part01():
  target_lengths = [ 2, 3, 4, 7 ]
  result = 0
  for line in helpers.yield_lines("data/08.txt"):
    result += len(list(filter(
      lambda length: length in target_lengths,
      [len(x.strip()) for x in line.split('|')[1].split()] 
    )))
  
  print("December 8, Part 1; result: {0}".format(result))
  assert result == 479

def part02():
  result = 0
  for line in helpers.yield_lines("data/08.txt"):
    sequences = [x.strip() for x in line.split('|')[0].split()]
  
    output = [x.strip() for x in line.split('|')[1].split()]
    
    mapping = resolve_mapping(sequences)
    
    text = ""
    for x in output:
      text += str(mapping[''.join(sorted(x))])
    
    result += int(text)

  print("December 8, Part 2; result: {0}".format(result))
  assert result == 1041746

def resolve_mapping(sequences):
  mapping = {}
  
  for index, sequence in enumerate(sequences):
    sequence_length = len(sequence)
    if(sequence_length == 2):
      mapping[1] = index
    elif(sequence_length == 3):
      mapping[7] = index
    elif(sequence_length == 4):
      mapping[4] = index
    elif(sequence_length == 7):
      mapping[8] = index
  
  fives = [ x for x in sequences if len(x) == 5 ]
  sixes = [ x for x in sequences if len(x) == 6 ]

  for f in fives:
    if(len(remove_segments(f, sequences[mapping[7]])) == 2):
      mapping[3] = sequences.index(f)
  
  for f in fives:
      rest = remove_segments(f, sequences[mapping[4]])
      if(len(rest) == 3):
        mapping[2] = sequences.index(f)

  for f in fives:
      rest = remove_segments(f, sequences[mapping[2]])
      if(len(rest) == 2):
        mapping[5] = sequences.index(f)

  for f in sixes:
    rest = remove_segments(f, sequences[mapping[4]])
    if(len(rest) == 2):
      mapping[9] = sequences.index(f)
    elif(len(rest) == 3):
      rest = remove_segments(f, sequences[mapping[1]])
      if(len(rest) == 5):
        mapping[6] = sequences.index(f)
      else:
        mapping[0] = sequences.index(f)

  sequence_map = {}

  
  for key in mapping:
    sequence_map[''.join(sorted(sequences[mapping[key]]))] = key

  return sequence_map

def remove_segments(a, b):
  s = a
  for c in b:
    s = s.replace(c, "")
  return s