from datetime import datetime
from datetime import timedelta
import random as rd
from datetime import date
sandwich_names =["N/A","The Pepe","Big John","Totally Tuna",
                    "Turkey Tom","Vito","The Veggie","Spicy East Coast Italian","Billy Club","Italian Night Club","Hunter's Club","Country Club","Beach Club","Jimmy Cubano","Bootlegger Club","Club Tuna","Club LuLu","Ultimate Porker","JJ Gargantuan"]

def findNextTime(curTime):
    nextTime = datetime(curTime.year, curTime.month, curTime.day, 13, 40, 0, 0)
<<<<<<< HEAD
=======
   
>>>>>>> f81615a2ed67905e2d368a0b402ea7a5dd94ace2
    while nextTime.weekday() not in [1, 3] or nextTime < curTime:
        nextTime += timedelta(days=1)
    return nextTime

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
    curTime = datetime.now()
    nextTime = findNextTime(curTime)
    print(nextTime - curTime)
    Sandwich_of_the_day()


if __name__ == "__main__":
    main()

