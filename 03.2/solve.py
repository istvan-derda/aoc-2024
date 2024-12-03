import re

def solve(intext):
    enabled_snippets = [outer_match for (outer_match, _, _) in re.findall(string=intext, pattern=r"((^|do\(\)).*?(don't\(\)|$))", flags=re.MULTILINE)]
    enabled = '\n'.join(enabled_snippets)
    with open('enabled', 'w') as file:
        file.write(enabled)

    multiplications = re.findall(string=enabled, pattern=r'mul\((\d+),(\d+)\)')
    multiplication_results = [int(a) * int(b) for (a, b) in multiplications]
    return sum(multiplication_results)


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
