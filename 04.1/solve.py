DIRECTIONS = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1),
]


def get_letter_at(row, column, grid):
    if row not in range(0, len(grid)):
        return None
    if column not in range(0, len(grid[row])):
        return None
    return grid[row][column]


def check_xmas_dir(start_row, start_column, grid, direction):
    searched_word = "XMAS"
    for i, expected_letter in enumerate(searched_word):
        row = start_row + i*direction[0]
        column = start_column + i*direction[1]
        found_letter = get_letter_at(row, column, grid)
        if found_letter != expected_letter:
            return False
    return True


def find_xmas_at(row, column, grid):
    xmas_count = 0
    for direction in DIRECTIONS:
        if check_xmas_dir(row, column, grid, direction):
            xmas_count += 1
    return xmas_count


def solve(intext):
    grid = [line for line in intext.split('\n')]
    xmas_count = 0
    for row, _ in enumerate(grid):
        for column, _ in enumerate(grid[0]):
            xmas_count += find_xmas_at(row, column, grid)
    return xmas_count


def get_input(filename):
    with open(filename) as infile:
        return infile.read()


def main():
    test_input = get_input("testinput")
    test_result = solve(test_input)
    print(test_result)
    expected = 18
    print(test_result == expected)

    input = get_input("input")
    result = solve(input)
    print(result)
       

if __name__ == "__main__":
    main()
