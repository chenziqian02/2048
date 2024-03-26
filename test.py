from main import *


def test_left_merge(values, expected_result):
    """
    Tests the left merge function by merging the given list of
    values to the left and comparing it with the expected result.

    Parameters:
    values (list): A list of integers to be merged to the left.
    expected_result (list): A list of integers that represents the
    expected result after merging the input values to the left.
    """
    print("Testing values", values)
    actual_result = left_merge(values)
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def test_right_merge(values, expected_result):
    """
    Tests the right merge function by merging the given list of
    values to the right and comparing it with the expected result.

    Parameters:
    values (list): A list of integers to be merged to the right.
    expected_result (list): A list of integers that represents
     the expected result after merging the input values to the right.
    """
    print("Testing values", values)
    actual_result = right_merge(values)
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def test_up_merge(values, expected_result):
    """
    Tests the up merge function by merging the given list of values
    up and comparing it with the expected result.

    Parameters:
    values (list): A list of integers to be merged up.
    expected_result (list): A list of integers that represents the
    expected result after merging the input values up.
    """
    print("Testing values", values)
    actual_result = up_merge(values)
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def test_down_merge(values, expected_result):
    """
    Tests the down merge function by merging the given list of values
    down and comparing it with the expected result.

    Parameters:
    values (list): A list of integers to be merged down.
    expected_result (list): A list of integers that represents the
    expected result after merging the input values down.
    """
    print("Testing values", values)
    actual_result = down_merge(values)
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def test_find_on_board(x, board, expected_result):
    """
     Tests whether the given value is present on the given board.

     Parameters:
     x (int): The value to search for on the board.
     board (list of lists): The board to search for the given value.
     expected_result (bool): The expected result of the search. True
     if the value is expected to be found, False otherwise.
     """
    print("Testing values", x, "board is:", board)
    actual_result = find_on_board(x)
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def test_board_full(board, expected_result):
    """
    Tests whether the given board is full.

    Parameters:
    board (list of lists): The board to check for fullness.
    expected_result (bool): The expected result of the check.
    True if the board is expected to be full, False otherwise.
    """
    print("Testing values", board)
    actual_result = is_board_full()
    print("\tExpected......", expected_result)
    print("\tActual........", actual_result)


def main():
    """
    serves as the test driver
    """
    print('testing left merge')
    # tests basic case
    test_left_merge([0, 0, 2, 2], [4, 0, 0, 0])
    # tests all the same numbers
    test_left_merge([4, 4, 4, 4], [8, 8, 0, 0])
    # tests when all numbers are zero
    test_left_merge([0, 0, 0, 0], [0, 0, 0, 0])
    # tests when there are no zeroes
    test_left_merge([2, 4, 4, 8], [2, 8, 8, 0])

    print('\ntesting right merge')
    test_right_merge([0, 0, 2, 2], [0, 0, 0, 4])
    test_right_merge([4, 4, 4, 4], [0, 0, 8, 8])
    test_right_merge([0, 0, 0, 0], [0, 0, 0, 0])
    test_right_merge([2, 4, 4, 8], [0, 2, 8, 8])

    print('\ntesting up merge')
    test_up_merge([0, 0, 2, 2], [4, 0, 0, 0])
    test_up_merge([4, 4, 4, 4], [8, 8, 0, 0])
    test_up_merge([0, 0, 0, 0], [0, 0, 0, 0])
    test_up_merge([2, 4, 4, 8], [2, 8, 8, 0])

    print('\ntesting down merge')
    test_down_merge([0, 0, 2, 2], [0, 0, 0, 4])
    test_down_merge([4, 4, 4, 4], [0, 0, 8, 8])
    test_down_merge([0, 0, 0, 0], [0, 0, 0, 0])
    test_down_merge([2, 4, 4, 8], [0, 2, 8, 8])

    print('\ntesting find_on_board')
    board = [
        [2, 4, 2, 0],
        [8, 16, 8, 2],
        [4, 8, 16, 4],
        [0, 2, 4, 8]
    ]
    test_find_on_board(0, board, True)
    test_find_on_board(3, board, False)

    print('\ntesting is board full')
    board_1 = [
        [2, 4, 2, 4],
        [8, 16, 8, 2],
        [4, 8, 16, 4],
        [8, 2, 4, 8]
    ]

    board_2 = [
        [2, 4, 2, 0],
        [8, 16, 8, 2],
        [4, 8, 16, 4],
        [0, 2, 4, 8]
    ]
    test_board_full(board_1, True)
    test_board_full(board_2, False)


if __name__ == '__main__':
    main()


