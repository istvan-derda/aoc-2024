import re
from test import *


def parse_rules(rules_text):
    rules = re.findall(string=rules_text, pattern=r'(\d+)\|(\d+)')
    rules = [(int(a), int(b)) for (a, b) in rules]
    return rules


def parse_updates(updates_text):
    updates = [row.split(',') for row in updates_text.split('\n') if row != '']
    updates = [[int(c) for c in row] for row in updates]
    return updates

def parse(intext):
    split_text = intext.split("\n\n")
    rules = parse_rules(split_text[0])
    updates = parse_updates(split_text[1])
    return rules, updates


def get_middle(update):
    return update[int(len(update)/2)]


def validate_update(update, rules):
    for rule in rules:
        if not is_compliant(update, rule):
            return False
    return True


def is_compliant(update, rule):
    try:
        if update.index(rule[0]) < update.index(rule[1]):
            return True
        else:
            return False
    except ValueError:
        return True


def fix_update(update, rules):
    while not validate_update(update, rules):
        print("starting fix run")
        for rule in rules:
            update = apply_rule(update, rule)
    return update


def apply_rule(update, rule):
    left = rule[0]
    right = rule[1]
    try:
        left_index = update.index(left)
        right_index = update.index(right)
        if left_index > right_index:
            update[left_index] = right
            update[right_index] = left
        return update
    except:
        return update


def compute_checksum(updates):
    return sum([get_middle(update) for update in updates])


def solve(intext):
    rules, updates = parse(intext)
    fixed_updates = []
    for update in updates:
        print(update)
        if not validate_update(update, rules):
            print("fixing..")
            fixed_update = fix_update(update, rules)
            fixed_updates.append(fixed_update)
    return compute_checksum(fixed_updates)



def get_input(filename):
    with open(filename) as infile:
        return infile.read()


def main():
    test_all()
    test_input = get_input("testinput")
    test_result = solve(test_input)
    print(test_result)
    expected = 143
    print(test_result == expected)

    input = get_input("input")
    result = solve(input)
    print(result)
       

if __name__ == "__main__":
    main()
