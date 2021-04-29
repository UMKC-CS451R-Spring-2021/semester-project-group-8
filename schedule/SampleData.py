
# with the way its reading data right now, information needs to be in a dict with professor:[listOfValues]
format = {"Purple": [],
             "Brown": [],
             "Tan": [],
             "Pink": [],
             "Green": [],
             "Blue": [],
             "Orange": []}

days = ("M", "T", "W", "R", "F", "SA", "SU")
timeSlots = ("8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM",
              "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM")

classDict = {"Purple": ["CS 6000", "CS 6500"],
             "Brown": ["CS 6000", "CS 6500"],
             "Tan": ["CS 150", "CS 160", "CS 170", "CS 180"],
             "Pink": ["CSEE 5000"],
             "Green": ["ECE 1000", "ECE 2000"],
             "Blue": ["CS 100", "CS 200", "CS 300", "CS 400"],
             "Orange": ["EE 400", "EE 500"]}

timeAvail = {"Purple": ["A"],
             "Brown": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM"],
             "Tan": ["A"],
             "Pink": ["A"],
             "Green": ["A"],
             "Blue": ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"],
             "Orange": ["A"]}

dayAvail = {"Purple": ["A"],
             "Brown": ["T", "R"],
             "Tan": ["A"],
             "Pink": ["A"],
             "Green": ["F", "SA", "SU"],
             "Blue": ["M", "T", "W"],
             "Orange": ["A"]}

# not utilized right now, this was for the preference of having two teachers not teach at the same time
conflict = {"Purple": "Brown",
             "Brown": "Purple",
             "Tan": [],
             "Pink": [],
             "Green": "Blue",
             "Blue": "Green",
             "Orange": []}