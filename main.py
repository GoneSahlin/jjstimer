from datetime import datetime
from datetime import timedelta
import random as rd
from datetime import date
sandwich_names =["N/A","The Pepe","Big John","Totally Tuna",
                    "Turkey Tom","Vito","The Veggie","Spicy East Coast Italian","Billy Club","Italian Night Club","Hunter's Club","Country Club","Beach Club","Jimmy Cubano","Bootlegger Club","Club Tuna","Club LuLu","Ultimate Porker","JJ Gargantuan"]
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

def Sandwich_of_the_day():
    dashes = 0
    day = ""
    month = ""
    for char in str(date.today()):
        if char == '-':
            dashes = dashes + 1
        if dashes == 1:
            month = month + char
        if dashes == 2: 
            day = day + char 

    month = (-1 *int(month))
    day = (-1 * int(day))
    seed = month * day 
    rd.seed(seed)
    temp = rd.randrange(1,18)
    print("Today's sandwich of the day is a #"+str(temp)+" "+sandwich_names[temp])

def main():
    jjsTimes = findJJsTimes()
    curTime = datetime.now()
    print(jjsTimes[1] > curTime)
    nextTime = findNextTime(curTime, jjsTimes)
    print(nextTime - curTime)
    Sandwich_of_the_day()


if __name__ == "__main__":
    main()

