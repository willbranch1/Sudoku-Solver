import math

def solveSudoku(row, col, size, sudoku):
    if col == size:
        if row == size - 1:
            return True
        else:
            row += 1
            col = 0
    
    if sudoku[row][col] == 0:
        for guess in range(1, size + 1, 1):
            flag = True
            
            for i in range(size):
                if sudoku[row][i] == guess or sudoku[i][col] == guess:
                    flag = False
                    break
            
            sqr = int(math.sqrt(size))
            sqr_row = row - row % sqr
            sqr_col = col - col % sqr
            for i in range(sqr):
                if not flag:
                    break
                for j in range(sqr):
                    if sudoku[i + sqr_row][j + sqr_col] == guess:
                        flag = False
                        break
            if flag: 
                sudoku[row][col] = guess
                if solveSudoku(row, col + 1, size, sudoku):
                    return True
            sudoku[row][col] = 0
        return False
    
    else:
        return solveSudoku(row, col + 1, size, sudoku)

def prettyPrintSudoku(size, sudoku):
    sqr = int(math.sqrt(size))
    for i in range(size):
        for j in range(size):
            print(str(sudoku[i][j]) + " ", end="")
            if j % sqr == sqr - 1 and j != size - 1:
                print("| ", end="")
        print()
        if i % sqr == sqr - 1 and i != size - 1:
            for j in range(size * 2 + sqr - 1):
                print("-", end="")
            print()

def readSudokuFile(filepath, sudoku):
    file = open(filepath, "r")
    data = file.readline()

    size = int(math.sqrt(len(data)))
    
    if (size == 4 or size == 6 or size == 9) and data.isdigit():
        row = 0
        col = 0
        for i in range(len(data)):
            sudoku[row][col] = int(data[i])
            if (i + 1) % size == 0:
                row += 1
                col = 0
            else:
                col += 1
        file.close()
        return size
    else:
        file.close()
        return 0
            
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
        print("ERROR: Invalid Sudoku Entered")
    else:
        prettyPrintSudoku(size, sudoku)
        solveSudoku(0, 0, size, sudoku)
        print("\nSOLVED:")
        prettyPrintSudoku(size, sudoku)
        
if __name__ == "__main__":
    main()