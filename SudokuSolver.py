import math

def solveSudoku(row, col, size, sudoku):
    """Solves the sudoku. Recursivly calls itself an minimum of n^2 times as it is cycling through the sudoku list.

    Args:
        row (int): row index for recursion
        col (int): column index for recursion
        size (int): the size of the sudoku(a 9x9 sudoku has size 9)
        sudoku (list[list[int]]): the list created to represent the sudoku grid

    Returns:
        boolean: returns True if the recursive step is successful and False otherwise.
    """
    if col == size: # then you know you are at the end of a row
        if row == size - 1: # then you have reached the end of the sudoku and return
            return True
        else: # go down a row
            row += 1
            col = 0
    
    if sudoku[row][col] == 0: # 0 represents an 'empty' space in the sudoku
        for guess in range(1, size + 1, 1): # cycles through possible guesses and tries each one
            flag = True
            
            for i in range(size): # check if guess is in row or col
                if sudoku[row][i] == guess or sudoku[i][col] == guess:
                    flag = False
                    break
            
            sqr = int(math.sqrt(size))
            sqr_row = row - row % sqr
            sqr_col = col - col % sqr
            for i in range(sqr): # check if the guess is in the same square
                if not flag:
                    break
                for j in range(sqr):
                    if sudoku[i + sqr_row][j + sqr_col] == guess:
                        flag = False
                        break
                    
            if flag: # if the guess was not in the same row, col, or square update the grid
                sudoku[row][col] = guess
                if solveSudoku(row, col + 1, size, sudoku): # recursively call to jump to the next entry in the sudoku list
                    return True
            sudoku[row][col] = 0 # if the solveSudoku() recursive call came back False, the current entry was wrong and we need to reset it
        return False # if no guess is found to be correct then return False
    
    else:
        return solveSudoku(row, col + 1, size, sudoku) # if the entry already has a number then jump to the next empty entry

def prettyPrintSudoku(size, sudoku):
    """Prints the sudoku in a nice format.

    Args:
        size (int): the size of the sudoku(a 9x9 sudoku has size 9)
        sudoku (list[list[int]]): the list created to represent the sudoku grid
    """
    sqr = int(math.sqrt(size))
    for i in range(size):
        for j in range(size):
            print(str(sudoku[i][j]) + " ", end="")
            if j % sqr == sqr - 1 and j != size - 1: # prints a verticle bar every two or three columns based on the sudoku size
                print("| ", end="")
        print()
        if i % sqr == sqr - 1 and i != size - 1:  # prints a horizontal bar with the length based on the sudoku size
            for j in range(size * 2 + sqr - 1):
                print("-", end="")
            print()

def readSudokuFile(filepath, sudoku):
    """Reads the sudoku in from the designated filepath.

    Args:
        filepath (str): user inputted sudoku filepath
        sudoku (list[list[int]]): the list created to represent the sudoku grid

    Returns:
        int: the size of the sudoku(a 9x9 sudoku has size 9)
    """
    file = open(filepath, "r")
    data = file.readline()

    size = int(math.sqrt(len(data)))
    
    if (size == 4 or size == 9) and data.isdigit(): # can only solve 4x4 and 9x9 problems
        row = 0
        col = 0
        for i in range(len(data)):
            sudoku[row][col] = int(data[i])
            if (i + 1) % size == 0: # if the index is at the end of the row for the given sudoku size, change the the next row
                row += 1
                col = 0
            else:
                col += 1
        file.close()
        return size
    else:
        file.close()
        return 0 # returns 0 if the sudoku is not valid
            
def main():
    sudoku = [[0, 0 , 0, 0, 0, 0, 0, 0, 0], #a 4x4 sudoku uses this same list, but only uses a 4x4 section of it
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0]]
    
    filepath = input("Enter filepath: ")
    size = readSudokuFile(filepath, sudoku)
    if size == 0:
        print("\nERROR: Invalid Sudoku Entered")
    else:
        print("\nUnsolved:")
        prettyPrintSudoku(size, sudoku)
        flag = solveSudoku(0, 0, size, sudoku)
        if flag:
            print("\nSOLVED:")
            prettyPrintSudoku(size, sudoku)
        else:
            print("\nERROR: No Possible Solution")
        
if __name__ == "__main__":
    main()