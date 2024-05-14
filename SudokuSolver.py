import copy

def solveSudoku(board):
    '''
    General method: Starting for top left cell on board, snake through every empty cell. On each cell assign a possible value.
    If a contradcition occurs re-assign different value to first cell that has not had all possible values checked. BACKTRACKING
    '''
    return solveSudokuHelper(copy.deepcopy(board), 0, 0)
    
    
def solveSudokuHelper(board, cellRow, cellCol):
    #When we reach the final cell on the board, if there is only 1 legal value, then the board is solved
    if cellRow == len(board) -1 and cellCol == len(board) - 1:
        legalVals = list(possibleVals(board, cellRow, cellCol))
        if board[cellRow][cellCol] != 0:
            return board
        elif legalVals == []:
            return None
        else:
            board[cellRow][cellCol] = legalVals[0]
            return board
    else:
        #Determining index for next cell
        if cellCol == len(board) - 1:
            newCol = 0
            newRow = cellRow + 1
        else:
            newRow, newCol = cellRow, cellCol + 1
        #Skip if the cell in non-empty
        if board[cellRow][cellCol] != 0:
            return solveSudokuHelper(board, newRow, newCol)
        else:
            #Check through all possible values
            legalVals = possibleVals(board, cellRow, cellCol)
            for val in legalVals:
                board[cellRow][cellCol] = val
                solution = solveSudokuHelper(copy.deepcopy(board), newRow, newCol)
                if solution != None:
                    return solution
        return None
        
def possibleVals(board, cellRow, cellCol):
    possibleVals = set()
    #Create set of all values
    for i in range(len(board)):
        possibleVals.add(i + 1)
    #Remove values in row
    for value in board[cellRow]:
        if value in possibleVals:
            possibleVals.remove(value)
    #Remove Values in coloumn
    for j in range(len(board)):
        if board[j][cellCol] in possibleVals:
            possibleVals.remove(board[j][cellCol])
    #Remove values in localized grid
    gridSize = int(len(board)**0.5)
    if cellRow % gridSize == 0:
        startRow = cellRow
    elif cellRow % gridSize == 1:
        startRow = cellRow - 1
    else:
        startRow = cellRow - 2

    if cellCol % gridSize == 0:
        startCol = cellCol
    elif cellCol % gridSize == 1:
        startCol = cellCol - 1
    else:
        startCol = cellCol - 2
    for drow in range(gridSize):
        for dcol in range(gridSize):
            if board[startRow + drow][startCol + dcol] in possibleVals:
                possibleVals.remove(board[startRow + drow][startCol + dcol])
    
    return possibleVals

#Please insert empty cells as 0
board  = [[0, 5, 6, 8, 9, 1, 0, 4, 0],
           [0, 4, 0, 7, 0, 0, 0, 0, 1],
           [8, 0, 1, 0, 0, 5, 2, 0, 0],
           [1, 0, 2, 0, 7, 0, 0, 0, 0],
           [5, 9, 8, 0, 6, 0, 0, 0, 4],
           [0, 6, 4, 0, 3, 8, 1, 0, 0],
           [0, 2, 7, 0, 0, 3, 0, 5, 0],
           [0, 0, 0, 2, 0, 4, 0, 0, 7],
           [9, 0, 0, 0, 8, 0, 4, 3, 2]]
print(solveSudoku(board))