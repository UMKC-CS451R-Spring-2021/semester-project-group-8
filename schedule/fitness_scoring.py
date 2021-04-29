import SampleData as x

class Professor:
    def __init__(self, name):
        self.name = name
        self.availableTimes = []
        self.classes = []
        self.availableDays = []
    def addTimes(self, time):
        self.availableTimes = time
    def addClasses(self, course):
        self.classes = course
    def addDays(self, day):
        self.availableDays = day

def getObj(prof):
    for obj in professor_list:
        if obj.name == prof:
            return obj

def checkTimes(setTime, prof):
    profObj = getObj(prof)
    if setTime not in profObj.availableTimes:
        #print(setTime, "not in", profObj.availableTimes)
        return int(-10)
    else:
        return 0
def checkDays(setDay, prof):
    profObj = getObj(prof)
    if setDay not in profObj.availableDays:
        #print(setDay, "not in", profObj.availableDays)
        return int(-10)
    else:
        return 0

professor_list = []
for prof in x.classDict:
    curr = prof
    prof = Professor(prof)
    professor_list.append(prof)
    prof.addClasses(x.classDict[curr])
    if x.timeAvail[curr] == ["A"]:
        prof.addTimes(x.timeSlots)
    else:
        prof.addTimes(x.timeAvail[curr])
    if x.dayAvail[curr] == ["A"]:
        prof.addDays(x.days)
    else:
        prof.addDays(x.dayAvail[curr])
    #print(prof.name)

#for prof in professor_list:
#    print(prof.name, prof.classes)



#def checkTime()