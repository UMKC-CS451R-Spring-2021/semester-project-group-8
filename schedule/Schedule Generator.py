import random

# I hope you like dictionaries

profClassDict = {"Purple": ["CS 6000", "CS 6500"],
             "Brown": ["CS 6000", "CS 6500"],
             "Tan": ["CS 150", "CS 160", "CS 170", "CS 180"],
             "Pink": ["CSEE 5000"],
             "Green": ["ECE 1000", "ECE 2000"],
             "Blue": ["CS 100", "CS 200", "CS 300", "CS 400"],
             "Orange": ["EE 400", "EE 500"]}

days = ("M", "T", "W", "R", "F", "SA", "SU")
timeSlots = ("8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM",
              "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM")
class_list = []

def getRand(list):
    randI= int(random.random() * len(list))
    return list[randI]

## haven't implemented preferences and restrictions
## soo cant calculate a fitness score yet
def fitness():
    return 10

def makeSchedule():
    profTimeDict = {}
    for prof in profClassDict:
        classes = profClassDict[prof]
        profTimeDict[prof] = []
        dayAndTime = []

        i = 0
        while i < len(classes):
            dayAndTime.append(getRand(days))
            dayAndTime.append(getRand(timeSlots))
            i+=1
            profTimeDict[prof].append(dayAndTime)
            dayAndTime = []
# wow sry did i overcomplicate that
#    for prof in profTimeDict:
#        print(profTimeDict[prof])
    return profTimeDict

def printSchedule(profTimeDict):

    for prof in profClassDict:
        classes = profClassDict[prof]
        dayAndTime = profTimeDict[prof]
        i = 0
        print(prof, " Classes: ")
        while i < len(classes):
            print(" Class: ", classes[i], dayAndTime[i][0], dayAndTime[i][1])
            i+=1

times = makeSchedule()
printSchedule(times)