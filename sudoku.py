import json

blank = " "

# Blank Sudoku board.
blank_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

# Reads the board from an existing file.
def read_board_from_file(filename):
    try:
        with open(filename, "r") as file:
            # Read the board from a json dictionary.
            board_text = file.read()
            board_json = json.loads(board_text)
            board = board_json["board"]
            return board
    except:
        return blank_board

# Writes the board to a file to save the game.
def write_board_to_file(filename, board):
    with open(filename, "w") as file:
        # Put the board into a json dictionary.
        board_json = {"board" : board}
        board_text = json.dumps(board_json)
        file.write(board_text)
        file.close()
        exit(f"Your game has been saved to {filename}.")

# Checks for any squares that contain a zero (are blank) to determine if the game is done.
def game_is_complete(board):
    num_of_blank_squares = 0
    
    # Counts the number of zeros in each row of the board.
    for index in range(9):
        num_of_blank_squares += board[index].count(0)
    
    # Displays a message to the user when the game is completed.
    if num_of_blank_squares == 0:
        print("You won!")
        return True
    else:
        return False

# Puts a blank (" ") into every square on the board that contains a zero.
def change_square_from_zero_to_blank(board):
    for row in range(9):
        for column in range(9):
            if int(board[row][column]) == 0:
                board[row][column] = blank
    return board

# Puts a zero into every square on the board that contains a blank (" ").
def change_square_from_blank_to_zero(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == blank:
                board[row][column] = 0
    return board

# Displays the Sudoku board on the screen.
def display_board(board):
    # Changes all of the zeros to blanks for the user.
    change_square_from_zero_to_blank(board)
    # Displays the header.
    print("   A B C   D E F   G H I")
    # Displays every square in each row of the board with the dividing lines.
    print(f"1  {board[0][0]} {board[0][1]} {board[0][2]} | {board[0][3]} {board[0][4]} {board[0][5]} | {board[0][6]} {board[0][7]} {board[0][8]}")
    print(f"2  {board[1][0]} {board[1][1]} {board[1][2]} | {board[1][3]} {board[1][4]} {board[1][5]} | {board[1][6]} {board[1][7]} {board[1][8]}")
    print(f"3  {board[2][0]} {board[2][1]} {board[2][2]} | {board[2][3]} {board[2][4]} {board[2][5]} | {board[2][6]} {board[2][7]} {board[2][8]}")
    print("   ------+-------+------")
    print(f"4  {board[3][0]} {board[3][1]} {board[3][2]} | {board[3][3]} {board[3][4]} {board[3][5]} | {board[3][6]} {board[3][7]} {board[3][8]}")
    print(f"5  {board[4][0]} {board[4][1]} {board[4][2]} | {board[4][3]} {board[4][4]} {board[4][5]} | {board[4][6]} {board[4][7]} {board[4][8]}")
    print(f"6  {board[5][0]} {board[5][1]} {board[5][2]} | {board[5][3]} {board[5][4]} {board[5][5]} | {board[5][6]} {board[5][7]} {board[5][8]}")
    print("   ------+-------+------")
    print(f"7  {board[6][0]} {board[6][1]} {board[6][2]} | {board[6][3]} {board[6][4]} {board[6][5]} | {board[6][6]} {board[6][7]} {board[6][8]}")
    print(f"8  {board[7][0]} {board[7][1]} {board[7][2]} | {board[7][3]} {board[7][4]} {board[7][5]} | {board[7][6]} {board[7][7]} {board[7][8]}")
    print(f"9  {board[8][0]} {board[8][1]} {board[8][2]} | {board[8][3]} {board[8][4]} {board[8][5]} | {board[8][6]} {board[8][7]} {board[8][8]}")
    # Changes all of the blanks back to zeros.
    change_square_from_blank_to_zero(board)

# Adds the number the user indicated into the correct square on the board.
def update_board(board, row, column, number):
    board[row][column] = number
    return board

# Converts "B3" into (2, 1) as a row and column.
def convert_coordinates_to_row_and_column(coordinates):
    # Turns the string "3" into the number 2.
    for character in coordinates:
        # Turns the numerical value into the row on the board.
        if character.isdigit():
            row = int(character) - 1
        # Turns the alphabetical value into the capital coordinate letter.
        elif character.isalpha():
            coordinate_letter = character.upper()
            # Turns the letter "C" into the number 2.
            column = ord(coordinate_letter) - ord("A")
    # Returns the row and column as a tuple.
    return row, column

# Converts row and column (2, 1) into the coordinates "B3".
def convert_row_and_column_to_coordinates(row, column):
    return chr(column + ord("A")) + (str(row + 1))

# Checks whether the coordinates are valid or not.
def coordinates_are_valid(board, row, column):
    # Converts row and column into user-friendly coordinates.
    coordinates = convert_row_and_column_to_coordinates(row, column)
    
    # Displays a message if the row or column are invalid.
    if (row < 0 or row > 8) or (column < 0 or column > 8):
        print(f"ERROR: Square {coordinates} is invalid.")
        return False
    # Displays a message if the selected square is already filled.
    elif board[row][column] != 0:
        print(f"ERROR: Square {coordinates} is filled.")
        return False
    else:
        return True

# Checks whether a number is in the valid numbers list or not.
def number_is_valid(number, valid_numbers):
    if number in valid_numbers:
        return True
    else:
        return False

# Creates a list of all of the valid numbers for a given row, column, and inside square.
def generate_valid_numbers_list(board, row, column):
    valid_numbers = []
    numbers_in_column = []
    # Adds the value from each column into the numbers_in_column list.
    for index in range(0, 9):
        numbers_in_column.append(board[index][column])
    # For numbers 1 through 9.
    for number in range(1, 10):
        # Checks if the number is in the inside square if the number is not in the current row or column.
        if ((number not in numbers_in_column) and (number not in board[row])):
            # Loops through the beginning row and column indices where each inside square starts (at 0, 3, and 6).
            for row_start in range(0, 9, 3):
                for column_start in range(0, 9, 3):
                    # Determines where the correct inside square starts based on the row and column from the coordinates.
                    if (row_start <= row <= row_start+2) and (column_start <= column <= column_start+2):
                        # Checks each number in the inside square that begins at the determined start_row and start_column.
                        if ((number not in board[row_start][column_start:(column_start+3)]) 
                        and (number not in board[row_start+1][column_start:(column_start+3)]) 
                        and (number not in board[row_start+2][column_start:(column_start+3)])):
                            # Adds the numbers that are not in the inside square (are valid).
                            valid_numbers.append(number)
    
    # Returns a list of all of the valid numbers that the user could input.
    return valid_numbers

# Plays a round of Sudoku.
def play_round(board):
    # Prompts user for coordinates.
    print("\nSpecify a coordinate to edit or 'q' to save and quit.")
    coordinates = input("> ")
   
    # Quits game if user enters "q" so it can be saved. 
    if coordinates.lower() == "q":
        return False
    # Displays a message if the input is not two characters long.
    elif len(coordinates) != 2:
        print(f"ERROR: Square {coordinates} is invalid.")
        return True

    try:
        # Turns coordinates into row and column.
        row, column = convert_coordinates_to_row_and_column(coordinates)
    except:
        print(f"ERROR: Square {coordinates} is invalid.")
        return True
    
    # Checks to see if coordinates are valid and restarts the round if not.
    if not coordinates_are_valid(board, row, column):
        return True
    
    # Propmts for number until the number is valid.
    while True:
        # Prompts user for number to place at coordinates.
        number = input(f"Enter a number to place at {convert_row_and_column_to_coordinates(row, column)} or 's' to display a list of valid numbers: ")
        
        # Returns a list of valid numbers that the user can place into the designated square.
        valid_numbers = generate_valid_numbers_list(board, row, column)

        # Displays a list of valid numbers when user enters "s" and restarts loop.
        if number.lower() == "s":
            print(f"Valid Numbers: {valid_numbers}")
            continue
        else:
            try:
                number = int(number)
            except:
                print(f"ERROR: The value {number} is invalid.")
                continue

        # Checks if the number is in the valid numbers list and restars the loop if not.
        if number_is_valid(number, valid_numbers):
            # Adds the number to the board at the indicated coordinates.
            update_board(board, row, column, number)
            display_board(board)
            return True
        else:
            print(f"ERROR: The value {number} is invalid.")
            continue

# Starts a game of Sudoku.
def main():
    # Displays the title of the game.
    print("\n-+{ SUDOKU GAME }+-")

    # Reads the board from a file or displays a blank board if no file is indicated.
    board = read_board_from_file(input("Where is your game board located? "))
    display_board(board)
    
    continue_round = True
    # Plays a round of Sudoku until the game is completed or the user enters "q".
    while not game_is_complete(board) and continue_round:     
        continue_round = play_round(board)

    # Saves the game and writes the board to a file.
    write_board_to_file(input("What file would you like to save your game to? "), board)

# Starts the program.
if __name__ == "__main__":
    main()
