from typing import Optional

def solve(intext):
    rows: list[str] = [row for row in intext.split("\n") if row != ""]
    reports: list[list[int]]= [[int(level) for level in row.split(" ")] for row in rows]
    safe_reports_count = 0
    for report in reports:
        if verify_report(report) == True:
            safe_reports_count += 1
    return safe_reports_count


def verify_report(report: list[int]) -> bool:
    print("---")
    print(report)
    bad_level = find_bad_level(report)
    if bad_level == None:
        print("ok")
        return True
    print(bad_level)
    fix_attempt1 = report[:bad_level] + report[bad_level + 1:]
    fix_attempt2 = report[:bad_level + 1] + report[bad_level + 2:]
    print(fix_attempt1)
    print(fix_attempt2)
    if find_bad_level(fix_attempt1) == None:
        print("ok")
        return True
    if find_bad_level(fix_attempt2) == None:
        print("ok")
        return True
    print("no")
    return False


def find_bad_level(report: list[int]) -> Optional[int]:
    i = 0
    is_increasing = None
    while i+1 < len(report):
        if (abs(report[i] - report[i+1]) < 1) or (abs(report[i] - report[i+1]) > 3):
            return i
        if is_increasing == None:
            is_increasing = report[i] < report[i+1]
        if is_increasing != (report[i] < report[i+1]):
            return i
        i += 1
    return None


def main():
    with open("input") as infile:
        intext = infile.read()
        result = solve(intext)
        print(result)
        

if __name__ == "__main__":
    main()
