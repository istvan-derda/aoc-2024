from solve import *


def test_parse_rules():
    input = '''1|2

               34|55
               9449|3'''
    expected = [
        (1,2),
        (34,55),
        (9449,3)]

    test("test_parse_rules", parse_rules, input, expected)


def test_parse_updates():
    input = '''1,2,3,4
               5,6,7,8
               123,12,1,1,3'''
    expected = [[1,2,3,4],
                [5,6,7,8],
                [123,12,1,1,3]]

    test("test_parse_updates", parse_updates, input, expected)
    

def test_parse():
    input = '''1|2
               3|23

               1,2,23
               55,2,1,23'''
    expected = ([(1,2),
                          (3,23)],
                         [[1,2,23],
                          [55,2,1,23]])
    test("test_parse", parse, input, expected)


def test_get_middle():
    test("test_get_middle3", get_middle, [1,2,3], 2)
    test("test_get_middle5", get_middle, [5,4,3,2,1], 3)


def test_compute_checksum():
    input = [[1,2,3],
             [48,50,77],
             [1,2,3,4,5,6,7],
             [99,4,101010]]
    expected = 60
    test("test_compute_checksum", compute_checksum, input, expected)


def test_all():
    test_parse()
    test_parse_rules()
    test_parse_updates()
    test_get_middle()
    test_compute_checksum()


def test(test_name, fun, input, expected):
    if (fun(input) != expected):
        print("TEST FAILURE: " + test_name)
        print(fun(input))
        print("does not match expected:")
        print(expected)
    else:
        print(test_name + ": OK")


