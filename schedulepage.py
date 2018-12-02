#page 1: Adding the classes in a schedule page
from tkinter import *
from calendar import *
import datetime

# class SchedulePage()

# def __init__(self):





def retrieveSchedule():
    schedule = str(textbox.get("1.0", END))
    return 'F18_schedule.ics'


# def addSchedule():
#     path = retrieveSchedule()
#     schedule = Calendar()
#     print(schedule.classSchedule(path))
#     print(schedule.Calendar)
#     return schedule.Calendar

currentDay = datetime.datetime.now()
currentTime = datetime.datetime.now()


#def run():
root = Tk()

root.geometry("810x580")


canvas = Canvas(root)
canvas.pack()

label = Label(root, height = 2, width = 50, \
	text = "Insert directory of .ics file of schedule below")
label.pack()
textbox = Text(root, height = 2, width = 30, relief = 'solid')
textbox.pack()

button = Button(root, text = "Import schedule", command = addSchedule)
button.pack()

result = Label(root, height = 200 , width = 200, \
	text = getTimesLocation(addSchedule()), wraplength = 700)
result.pack()


canvas.create_text(50, 15, text = "Your currernt day is " + currentDay.strftime('%A'),\
	anchor = NW)
canvas.create_text(50, 30, text = "Your currernt time is " + currentTime.strftime('%H:%M'),\
 	anchor = NW)

print(getTimesLocation(addSchedule()))

for day in getTimesLocation(addSchedule()):
	print(day)
	print(currentDay.strftime('%A').upper()[:2])
	#check 'MO' for monday, since there are no classes SA and SU
	
	if day == currentDay.strftime('%A').upper()[:2]:
		print('poop')
		canvas.create_text(50,70,text = 'Your classes for ' + day + ' are: ' + \
			str(getTimesLocation(addSchedule())[day]), anchor = NW, \
			 width = 300)

mainloop()

#run()
# def runMainLoop():
# 	mainloop()