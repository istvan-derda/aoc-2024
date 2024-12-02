def solve(intext):
    rows: list[str] = [row for row in intext.split("\n") if row != ""]
    reports: list[list[int]]= [[int(level) for level in row.split(" ")] for row in rows]
    safe_reports_count = 0
    for report in reports:
        if verify_report(report) == True:
            safe_reports_count += 1
    return safe_reports_count


def verify_report(report: list[int]) -> bool:
    incr_count = 0
    decr_count = 0
    i = 0
    while i+1 < len(report):
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            return False
        if report[i] < report[i+1]:
            incr_count += 1
        else:
            decr_count += 1
        i += 1
    if (incr_count > 1 and decr_count > 1):
        return False
    return True


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
