import re

def solve(intext):
    multiplications = re.findall(string=intext, pattern=r'mul\((\d+),(\d+)\)')
    multiplication_results = [int(a) * int(b) for (a, b) in multiplications]
    return sum(multiplication_results)


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
