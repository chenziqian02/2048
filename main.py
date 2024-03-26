# imports necessary modules
import turtle
import random
from turtle import *

# initializing the screen
sc = Screen()
sc.setup(800, 800)

# initializing turtle
t = turtle.Turtle()
t.speed(0)

# initializing constants in the game
GAME_RUNNING = 0
GAME_WON = 1
GAME_LOST = 2

# initializing variables
game_result = ""
board_full = False
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score = 0
last_move = ""


def draw():
    """
    Draws a square of side length 60 using the turtle graphics
    library. Moves the turtle forward by 60 units after drawing
    the square.
    """
    for i in range(4):
        t.forward(60)
        t.left(90)
    t.forward(60)


def get_color(number):
    """
    Returns the corresponding color for a given number in the game.
    :param number(int): The number for which the color needs to
    be determined.
    :return: a dictionary contains numbers that appears in the
    game and its corresponding color
    """
    color_map = {
        0: "white",
        2: "#eee4da",
        4: "#eee1c9",
        8: "#f3b279",
        16: "#f49564",
        32: "#f77c5f",
        64: "#f75f3d",
        128: "#edd074",
        256: "#eccc60",
        512: "#edc950",
        1024: "#eec341",
        2048: "#edc22e"
    }

    return color_map.get(number, "black")  # Default color is black for any number not in the map


def show_board(board, score, last_move):
    """
    Displays the 2048 game board using the turtle graphics library.
    Draws the board, displays the score and last move,
    and updates the screen.
    :param board: A 4x4 matrix representing the game board.
    :param score: The current score of the game.
    :param last_move: The last move made by the player.
    """
    # initializing pen speed
    t.speed(0)

    # initializing the board with nested loop
    for i in range(4):
        t.up()
        # Draw each row
        for j in range(4):
            # Set row position
            t.setpos(60 * j + 10, 60 * i + 10)
            # Set pen down to draw
            t.down()
            # Set the color based on the number
            col = get_color(board[4 - i - 1][j])
            t.fillcolor(col)

            if board[4 - i - 1][j] != 0:
                # Lift the pen up before writing the number
                t.up()
                # Adjust the pen position to center the text
                # and use align parameter
                t.setpos(60 * j + 30, 60 * i + 20)
                t.write(
                    str(board[4 - i - 1][j]),
                    align="center",
                    font=("Verdana", 12, "normal"))
                # Put the pen down after writing the number
                t.down()
            t.end_fill()
            t.up()

    # shows the last move
    t.setpos(-250, 200)
    t.down()
    t.fillcolor(col)
    t.write("Last action: " + last_move, font=("Verdana", 10, "normal"))
    t.up()

    # Show score
    t.setpos(-250, 100)
    t.down()
    t.fillcolor(col)
    t.write("Score: " + str(score), font=("Verdana", 25, "normal"))
    t.up()


def add_new_2_to_board():
    """
    Adds a new '2' tile to a random empty location on the game board.
    """
    i = random.randint(0, 3)
    j = random.randint(0, 3)

    # regenerate as long as this location is occupied
    while board[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)

    # set the new 2 at the new random location
    board[i][j] = 2


def add_new_4_to_board():
    """
    Adds a new '4' tile to a random empty location on the game board.
    """
    i = random.randint(0, 3)
    j = random.randint(0, 3)

    # regenerate as long as this location is occupied
    while board[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)

    # set the new 2 at the new random location
    board[i][j] = 4


def add_2_or_4():
    """
    Adds either a '2' or a '4' tile to a random empty
    location on the game board.
    """
    if random.randint(1, 100) % 2 == 0:
        add_new_2_to_board()
    else:
        add_new_4_to_board()


def show_instructions():
    """
    Displays instructions for the player on how to exit the game
    and start a new game. Also displays the game result if
    the game is over.
    """
    t.speed(0)
    # Display instructions to exit the game and start a new game
    t.setpos(-250, 250)
    t.down()
    # t.fillcolor('blue')
    t.write("Please press esc to exit game.",
            font=("Verdana", 10, "normal"))
    t.up()

    t.speed(0)
    t.setpos(-250, 270)
    t.down()
    # t.fillcolor('blue')
    t.write("Please press r to start new game.",
            font=("Verdana", 10, "normal"))
    t.up()

    # If the game is over, display the game result
    if game_result != "":
        t.speed(0)
        t.setpos(-250, 230)
        t.down()
        # t.fillcolor('blue')
        t.write(game_result, font=("Verdana", 10, "normal"))
        t.up()


def unsupported_key(key):
    """
    Handles unsupported key presses by displaying an
    "unsupported key" message on the screen.
    :param key: The unsupported key that was pressed.
    """

    global game_result
    game_result = f"Unsupported key '{key}' pressed."
    # Turn off screen updates to avoid flickering
    sc.tracer(0)
    # Clear the screen
    t.clear()
    # Redraw the game board, score, and last_move
    draw_board(board, score, last_move)
    # Update the screen to show the changes
    sc.update()


def draw_board(board, score, last_move):
    """
    Draws the game board using the turtle graphics library.
    :param board: A 4x4 matrix representing the game board.
    :param score: The current score of the game.
    :param last_move: The last move made by the player.
    """
    # Set the speed of the turtle
    t.speed(0)
    # Loop through each row of the board
    for i in range(4):
        # Move the turtle to the left edge of the row
        t.up()
        t.setpos(0, 60 * i)
        # Set the pen down to begin drawing
        t.down()
        # Draw each tile in the row
        for j in range(4):
            # Set the color for the tiles based on the number
            col = get_color(board[4 - i - 1][j])
            t.fillcolor(col)
            t.begin_fill()
            draw()
            t.end_fill()
    # Hide the turtle back to the left edge of the row
    t.hideturtle()
    # Show the board values and instructions
    show_board(board, score, last_move)
    show_instructions()


def reverse_values(values):
    """
    Reverses the input list of values.
    :param values: A list of values.
    :return: A list with reversed values.
    """

    # Swap 1st and last
    temp = values[0]
    values[0] = values[3]
    values[3] = temp

    # swap 2nd and 3rd
    temp = values[1]
    values[1] = values[2]
    values[2] = temp

    return values


def left_merge(values):
    """
    Merges the input list of values to the left according
    to the 2048 game rules.
    :param values: A list of values.
    :return: A list with merged values.
    """
    global score
    # Get non-zero values from this row
    row = []
    for i in values:
        if i != 0:
            row.append(i)
    for i in range(len(row), 4):
        row.append(0)
    # Merge values
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] = 2 * row[i]
            score += row[i]
            for j in range(i + 1, 3):
                row[j] = row[j + 1]
            row[3] = 0
    return row


def right_merge(values):
    """
    Merges the input list of values to the right according
    to the 2048 game rules.
    :param values: A list of values.
    :return: A list with merged values.
    """
    # Reverse the row
    values = reverse_values(values)

    # Left merge
    values = left_merge(values)

    # Reverse and return the row
    return reverse_values(values)


def up_merge(values):
    """
    Merges the input list of values upwards according to the 2048 game rules.
    :param values: A list of values.
    :return: A list with merged values.
    """

    # Call the left_merge function to perform the merging operation
    return left_merge(values)


def down_merge(values):
    """
    Merges the input list of values downwards according to the 2048 game rules.
    :param values: A list of values.
    :return: A list with merged values.
    """
    # Call the right_merge function to perform the merging operation
    return right_merge(values)


def move_up():
    """
    Moves the game board upwards and updates the game state.
    """

    # Print 'up' to the console to indicate the move direction
    print("up")

    # Iterate through each column of the board
    for j in range(4):
        # Initialize an empty list to store the column values
        col = []
        # Iterate through each row in the current column
        for i in range(4):
            # Append the value of the current cell to the column list
            col.append(board[i][j])
        # Call the up_merge function to merge the values in the column
        col = up_merge(col)
        # Update the board with the merged column values
        for i in range(4):
            board[i][j] = col[i]

    # Call the process_game function to update the game state
    process_game("up")


def move_down():
    """
    Moves the game board downwards and updates the game state.
    """
    print("down")

    # make down move
    for j in range(4):
        col = []
        for i in range(4):
            col.append(board[i][j])
        col = down_merge(col)
        for i in range(4):
            board[i][j] = col[i]

    process_game("down")


def move_left():
    """
    Moves the game board to the left and updates the game state.
    """
    print("left")

    # make left move
    for i in range(4):
        board[i] = left_merge(board[i])

    process_game("left")


def move_right():
    print("right")

    # make right move
    for i in range(4):
        board[i] = right_merge(board[i])

    process_game("right")


# the method to check the board contains the given integer
# we use this to check if the board contains a 2048 - means the game is won
# we also use this to check if the board contains a 0 - that is game is not over yet
def find_on_board(x):
    """
    Checks if the given integer x is present on the game board.
    :param x(int): The integer to search for on the game board.
    :return: A boolean value indicating whether the given integer
    is present on the game board.
    """
    for i in range(4):
        for j in range(4):
            if board[i][j] == x:
                return True
    return False


def is_board_full():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
    return True


def get_game_status():
    # if there is a 2048 on board, game is won
    if find_on_board(2048):
        return GAME_WON

    # if there is a 0 on board, game still running
    if find_on_board(0):
        return GAME_RUNNING

    # else, check if a move can create an empty space on board
    # check for the 3x3 board
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]:
                return GAME_RUNNING
    # check for last column
    for i in range(3):
        if board[i][3] == board[i + 1][3]:
            return GAME_RUNNING
    # check for last row
    for j in range(3):
        if board[3][j] == board[3][j + 1]:
            return GAME_RUNNING

    # finally, the game is lost
    return GAME_LOST


def is_game_over():
    """
    Determines if the game is over by checking if there are any
    valid moves left.
    :return: A boolean value indicating whether the game is over.
    """
    game_status = get_game_status()
    return game_status == GAME_LOST or game_status == GAME_WON


def process_game(last_move):
    """
    Process the game state based on the last move made by the player.
    Checks if the game is over, updates the game state by adding
    a new number (2 or 4) to the board, determines the game result (won, lost,
    or no more moves), and updates the game board display.
    :param last_move (str): A string representing the last move
    made by the player (e.g., "up", "down", "left", or "right").
    """

    if not is_game_over():
        # Add 2 or 4
        add_2_or_4()
    else:
        global game_result
        game_status = get_game_status()
        if game_status == GAME_WON:
            game_result = "You won!"
        elif game_status == GAME_LOST:
            game_result = "You lost!"

    sc.tracer(0)
    t.clear()
    draw_board(board, score, last_move)
    sc.update()


def main():
    """
    This function serves as the entry point of the game.
    Initializes the game board, score, and other variables.
    It also adds initial numbers (2 and 4) to the board and sets up
    key bindings for user input. The game loop listens for the user's
    key presses to perform the corresponding actions (move up, down,
    left, right, exit the game, or restart). Unsupported keys
    are handled by the unsupported_key function, which is not shown
    in this code snippet.
    """
    global board, score, last_move, game_result, board_full
    board = [[0 for _ in range(4)] for _ in range(4)]
    score = 0
    last_move = ""
    game_result = ""
    add_new_2_to_board()
    add_new_4_to_board()

    listen()

    sc.tracer(0)
    draw_board(board, score, "")
    sc.update()

    onkey(move_up, 'Up')
    onkey(move_down, 'Down')
    onkey(move_left, 'Left')
    onkey(move_right, 'Right')
    onkey(exit, 'Escape')
    onkey(main, 'r')

    unsupported_keys = (
        'abcdefghijklmnopqstuvwxyz'
        '0123456789'
        '!@#$%^&*()-_=+[]{}|;:,.<>?/'
    )
    for key in unsupported_keys:
        onkey(
            lambda key=key: unsupported_key(key),
            key
        )

    mainloop()


if __name__ == "__main__":
    main()
