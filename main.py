from datetime import datetime
from datetime import timedelta

def findJJsTimes():
    startingDate = datetime(2022, 2, 24, 13, 40, 0)
    jjsTimes = [startingDate]
    for i in range(10):
        jjsTimes.append(startingDate + timedelta(days=5 + 7 * i))
        jjsTimes.append(startingDate + timedelta(days=2 + 7 * i))
    return jjsTimes

def findNextTime(curTime, jjsTimes):
    for time in jjsTimes:
        if (curTime < time):
            return time

def main():
    jjsTimes = findJJsTimes()
    curTime = datetime.now()
    print(jjsTimes[1] > curTime)
    nextTime = findNextTime(curTime, jjsTimes)
    print(nextTime - curTime)


if __name__ == "__main__":
    main()
