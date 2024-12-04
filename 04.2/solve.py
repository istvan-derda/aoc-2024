DIRECTIONS = [
    (1,1),
    (-1,1),
    (-1,-1),
    (1,-1),
]


def get_letter_at(row, column, grid):
    if row not in range(0, len(grid)):
        return None
    if column not in range(0, len(grid[row])):
        return None
    return grid[row][column]


def check_word_dir(start_row, start_column, searched_word, direction, grid):
    for i, expected_letter in enumerate(searched_word):
        row = start_row + i*direction[0]
        column = start_column + i*direction[1]
        found_letter = get_letter_at(row, column, grid)
        if found_letter != expected_letter:
            return False
    return True


def find_x_mas_at(row, column, grid):
    mas_count = 0
    for direction in DIRECTIONS:
        if check_word_dir(row - direction[0], column - direction[1], 'MAS', direction, grid):
            mas_count += 1
        if mas_count == 2:
            return 1
    return 0


def solve(intext):
    grid = [line for line in intext.split('\n')]
    x_mas_count = 0
    for row, _ in enumerate(grid):
        for column, _ in enumerate(grid[0]):
            x_mas_count += find_x_mas_at(row, column, grid)
    return x_mas_count


def get_input(filename):
    with open(filename) as infile:
        return infile.read()


def main():
    test_input = get_input("testinput")
    test_result = solve(test_input)
    print(test_result)
    expected = 9
    print(test_result == expected)

    input = get_input("input")
    result = solve(input)
    print(result)
       

if __name__ == "__main__":
    main()
