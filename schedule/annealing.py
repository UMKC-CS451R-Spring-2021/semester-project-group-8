import SampleData as x
import fitness_scoring as fit
import random
import math

class Schedule:
    def __init__(self, courseID):
        self.courseID = courseID
        self.name = ""
        self.time = ""
        self.day = ""
        self.instruct = ""
    def setName(self, name):
        self.name = name
    def setTime(self, time):
        self.time = time
    def setDay(self, day):
        self.day = day
    def setInstruct(self, instruct):
        self.instruct = instruct

def getRand(list):
    randI= int(random.random() * len(list))
    return list[randI]

def simulated_annealing(schedule):
    temp = 1000
    finalTemp = 1
    alpha = 0.01

    currTemp = temp
    currSch = schedule
    while (currTemp > finalTemp):
        neighbor = makeNeighbor(currSch)

        diff = getScore(currSch) - getScore(neighbor)
        if diff < 0:
            currSch = neighbor
        else:
            if random.uniform(0, 1) < math.exp(-diff / currTemp):
                currSch = neighbor
        currTemp -= alpha
    return currSch

def makeNeighbor(schedule):
    toChange = getRand(schedule)
    var = getRand([1,2])
    if (var == 1):# change day
        toChange.setDay(getRand(x.days))
        #print("changed day for ", toChange.courseID)
    if (var == 2):
        toChange.setTime(getRand(x.timeSlots))
        #print("changed time for ", toChange.courseID)

    return schedule

def getScore(schedule):
    score = 0
    for obj in schedule:
        score = score + fit.checkTimes(obj.time, obj.instruct)
        score = score + fit.checkDays(obj.day, obj.instruct)
    return score

# assigns courses their IDs and professors
idObjList = []
i = 1
for prof in x.classDict:
    j = 0
    while j < len(x.classDict[prof]):
        currCourses = x.classDict[prof]
        id = i
        id = Schedule(i)
        id.setName(currCourses[j])
        id.setInstruct(prof)
        idObjList.append(id)
        j+=1
        i+=1

# creates initial random schedule
for obj in idObjList:
    obj.setDay(getRand(x.days))
    obj.setTime(getRand(x.timeSlots))

for obj in idObjList:
    print(obj.courseID, obj.name, obj.instruct, obj.day, obj.time)
print(getScore(idObjList))


best = simulated_annealing(idObjList)

for obj in best:
    print(obj.courseID, obj.name, obj.instruct, obj.day, obj.time)
print(getScore(best))