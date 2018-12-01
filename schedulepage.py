#page 1: Adding the classes in a schedule page
from tkinter import *
from calendar import *

# class SchedulePage()

# def __init__(self):





def retrieveSchedule():
    schedule = str(textbox.get("1.0", END))
    return 'F18_schedule.ics'


def addSchedule():
    path = retrieveSchedule()
    schedule = Calendar()
    print(schedule.classSchedule(path))
    print(schedule.Calendar)
    return schedule.Calendar




#def run():
root = Tk()

root.geometry("810x580")

label = Label(root, height = 2, width = 50, text = "Insert directory of .ics file of schedule below")
label.pack()
textbox = Text(root, height = 2, width = 30, relief = 'solid')
textbox.pack()

button = Button(root, text = "Import schedule", command = addSchedule)
button.pack()

result = Label(root, height = 200 , width = 200, text = getTimesLocation(addSchedule()), \
	wraplength = 700)
result.pack()

mainloop()

#run()
# def runMainLoop():
# 	mainloop()