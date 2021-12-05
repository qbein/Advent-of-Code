def part01():
  """
  Advent of Code 2021; December 4th, part 1
  """
  numbers, boards = read_data()
  
  winner:Board = None

  for number in numbers:
    for board in boards:
      if(board.add(number)):
        winner = board
        break
    else:
      continue
    break

  print("December 4, Part 1; result: {0}".format(winner.get_score()))

def part02():
  """
  Advent of Code 2021; December 4th, part 2
  """
  numbers, boards = read_data()
  
  winner:Board = None

  for number in numbers:
    for board in boards:
      if(board.add(number)):
        winner = board

  print("December 4, Part 1; result: {0}".format(winner.get_score()))  

def read_data():
  numbers:list = None
  boards = []
  
  current_board_numbers:list = None

  file = open("data_04.txt", "r")
  for _line in file:
    line = _line.strip()
    
    if(numbers is None):
      numbers = list(map(int, line.strip().split(",")))
      continue

    if(len(line) == 0):
      if(current_board_numbers is not None):
        boards.append(Board(current_board_numbers))
      current_board_numbers = []
      continue

    current_board_numbers.append([int(char) for char in line.split()])

  if(len(current_board_numbers) > 0):
    boards.append(Board(current_board_numbers))

  file.close()
  return numbers, boards

class Board:
  def __init__(self, numbers):
    self.numbers = numbers
    self.scores = [[0 for x in range(len(row))] for row in self.numbers]
    self.winning_number:int = None
  
  def add(self, drawed_number):
    # If we're already a winner we do not score more numbers
    if(self.winning_number is not None): return False

    for x, row in enumerate(self.numbers):
      for y, num in enumerate(row):
        if(num == drawed_number):
          self.scores[x][y] = 1;
          break
      else:
        continue
      break
    
    if(self.__has_won()):
      self.winning_number = drawed_number
      return True
    
    return False

  def __has_won(self):
    for row in self.scores:
      if(sum(row) == 5):
        return True

    for row in zip(*self.scores):
      if(sum(row) == 5):
        return True

    return False

  def __get_sum(self):
    # Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won
    sum = 0
    for index_y, row in enumerate(self.scores):
      for index_x, col in enumerate(row):
        if(col == 0):
          sum += self.numbers[index_y][index_x]
    return sum

  def get_score(self):
    if(self.winning_number is not None):
      return self.winning_number * self.__get_sum()
    else:
      return 0

  def __str__(self):
    return str(self.numbers) + str(self.scores)