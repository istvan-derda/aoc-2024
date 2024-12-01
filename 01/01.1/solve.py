def solve(intext):
    list1 = []
    list2 = []
    rows = [row for row in intext.split("\n") if row != ""]
    for row in rows:
        row = row.split("   ")
        list1.append(int(row[0]))
        list2.append(int(row[1]))
    list1.sort()
    list2.sort()
    difflist = []
    for i, e1 in enumerate(list1):
        difflist.append(abs(e1 - list2[i]))
    result = sum(difflist)
    return result


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
