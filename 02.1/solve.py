def solve(intext):
    rows = [row for row in intext.split("\n") if row != ""]
    reports = [[int(level) for level in row.split(" ")] for row in rows]
    safe_reports_count = 0
    for report in reports:
        if verify_report(report) == True:
            safe_reports_count += 1
    return safe_reports_count


def verify_report(report) -> bool:
    print(report)
    if report[0] < report[1]:
        return verify_increasing_report(report)
    else:
        return verify_decreasing_report(report)


def verify_increasing_report(report) -> bool:
    i = 0
    while i+1 < len(report):
        if report[i+1] - report[i] < 1 or report[i+1] - report[i] > 3:
            return False
        i += 1
    return True


def verify_decreasing_report(report) -> bool:
    i = 0
    while i+1 < len(report):
        if report[i] - report[i+1] < 1 or report[i] - report[i+1] > 3:
            return False
        i += 1
    return True


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
