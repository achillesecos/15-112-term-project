#Extracting from calander

class Calendar():

	def __init__(self):
		self.Calendar = {'MO':[], 'TU':[],
		'WE':[],'TH':[],'FR':[],'SA':[],
		'SU':[]}

	#def __repr__(self,calendar):
	#	return self.calendar 	


	def readFile(self,path):
	    with open(path, "rt") as f:
	        return f.read()

	def classSchedule(self,text):
		f = self.readFile(text)
		contents = f.splitlines(0)
		location = None
		for line in contents:
			if line == '/n' or line == '':
				continue
			if 'DTSTART' in line:
				startTime = line.split(":")[1]
			if 'DTEND' in line:
				endTime = line.split(":")[1]
			if "SUMMARY" in line:
				course = line.split('::')[1]
				#print(course)
			if 'BYDAY' in line:
				dayOfClass = line.split(';')[2].split('=')[1].split(',')
				#print(dayOfClass)
			if 'LOCATION' in line:
				location = line.split("-")[0]
				#print(location)
				for day in dayOfClass:
					self.Calendar[day].append((course, location, \
						int(str(startTime)[-6:-2]), int(str(endTime)[-6:-2])))

path = 'F18_schedule.ics'
achillesCalendar = Calendar()
print(achillesCalendar.classSchedule(path))
print(achillesCalendar.Calendar)

#cal = Calendar()



def getTimesLocation(schedule):
	result = {}
	lst = []
	for day in schedule:
		print(day + ':')
		#result[day] = schedule[day]
		for tup in schedule[day]:
			print((tup[0],tup[2],tup[3]))
			lst.append((tup[0],tup[2],tup[3]))
			lst.sort(key=lambda tup: tup[1])

		result[day] = lst
		lst = []
			#for eachInfo in schedule[day][tup]:
			#result[schedule[day][tup][eachInfo][2]] = schedule[day][tup][eachInfo][1]
	return result

def getLocations(schedule):
	result = {}
	lst = []
	for day in schedule:
		print(day + ':')
		#result[day] = schedule[day]
		for tup in schedule[day]:
			print((tup[1]))
			lst.append((tup[1],tup[2]))
			lst.sort(key=lambda tup: tup[1])

		result[day] = lst
		lst = []
		
	return result


#print(getTimesLocation(achillesCalendar.Calendar)['MO'])
print(getLocations(achillesCalendar.Calendar))

def getTodayClasses(schedule,day):
	result = []
	for i in range(1,len(schedule[day])):
		print('result is', result)
		result.append((schedule[day][i-1][0][9:], schedule[day][i][0][9:]))
	return result

print(getTodayClasses(getLocations(achillesCalendar.Calendar), 'MO'))




def getNeigboringNodes(node):
    neighboringNodes = [dijkstra.getNeighbors(node)]
    return neighboringNodes

def recommendPlace(node):
    pass




def classScheduleAutomatic():
    pass

def classScheduleManual(input):
    classes = {}
    for theClass in input:
        classes[theClass] = getNeigboringNodes(theClass)
    return classes

def getIntersectionNodes(node1,node2):
    set1 = set(getNeigboringNodes(node1))
    set2 = set(getNeigboringNodes(node2))
    return set1.intersection(set2)



















