from typing import Tuple, Optional, List

board : List[List[int]] = [
    [0,0,5,0,0,3,0,0,0],
    [4,0,0,0,0,0,0,8,0],
    [0,3,0,0,9,0,5,2,0],
    [6,9,0,0,8,0,0,0,0],
    [8,2,0,4,0,5,0,9,6],
    [0,0,0,0,2,0,0,1,0],
    [0,6,9,0,3,0,0,5,0],
    [0,4,0,0,0,0,0,0,7],
    [0,0,0,7,0,0,8,0,0]
]



def print_board(board: List[List[int]]) -> None:
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("--------------------------")

    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")

      if j == 8:
          print(board[i][j])
      else:
          print(str(board[i][j]) + " ", end="")


def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return row, column  # row, col

    return None, None


def solver(board: List[List[int]]) -> bool:
  rowPos, columnPos  = find_empty(board)
  
  if rowPos == None and columnPos == None:
    return True

  else:
    for i in range(1,10):
      if validator(board, rowPos, columnPos, i ):
          board[rowPos][columnPos] = i

          if solver(board):
              return True

          board[rowPos][columnPos] = 0

    return False

def validator(board: List[List[int]], rowPos: int, columnPos: int, number: int) -> bool:

  if number in board[rowPos]:
    return False
  
  for x in range(9):
    if number == board[x][columnPos]:
      return False

  xColumn, yColumn = calculateColumn(rowPos, columnPos)
 
  for i in range(0,3):
    for j in range(0,3):
      if board[xColumn + i][yColumn + j] == number:
        return False

  return True

def calculateColumn(rowPos: int, columnPos: int) -> Tuple[int, int]:
  return int(rowPos//3) * 3, int(columnPos//3)* 3 


print_board(board)
solver(board)
print("_________solved__________")
print_board(board)
