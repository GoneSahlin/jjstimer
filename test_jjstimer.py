from jjstimer import findNextTime

from datetime import datetime


def test_findNextTime():
    time_1 = datetime(2022, 4, 5, 10)
    next_1 = findNextTime(time_1)
    correct_1 = datetime(2022, 4, 5, 13, 40)
    assert next_1 == correct_1
    time_2 = datetime(2022, 4, 6, 13, 20)
    next_2 = findNextTime(time_2)
    correct_2 = datetime(2022, 4, 7, 13, 40)
    assert next_2 == correct_2
    time_3 = datetime(2022, 5, 31, 14)
    next_3 = findNextTime(time_3)
    correct_3 = datetime(2022, 6, 2, 14, 40)
    assert next_3 == correct_3

if __name__ == "__main__":
    test_findNextTime()