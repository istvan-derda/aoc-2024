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
    i = 0
    lastid = -1
    count = 0
    sum = 0
    for id in list1:
        if id == lastid:
            sum += count * id
            continue
        lastid = id
        count = 0
        while i<len(list2) and list2[i] < id:
            i+=1
        while i<len(list2) and list2[i] == id:
            count+=1
            i+=1
        sum+=count * id
    return sum
            
        

def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
