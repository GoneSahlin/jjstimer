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
    i = 0
    while(jjsTimes[i + 1] < curTime):
        i += 1
    return jjsTimes[i]

def main():
    jjsTimes = findJJsTimes()
    curTime = datetime.now()
    nextTime = findNextTime(curTime, jjsTimes)
    print(nextTime - curTime)


if __name__ == "__main__":
    main()
