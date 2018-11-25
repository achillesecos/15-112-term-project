#Extracting from calander

class Calendar():

	def __init__(self):
		self.Calendar = {'MO':[], 'TU':[],
		'WE':[],'TH':[],'FR':[],'SA':[],
		'SU':[]}


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
				print(course)
			if 'BYDAY' in line:
				dayOfClass = line.split(';')[2].split('=')[1].split(',')
				print(dayOfClass)
			if 'LOCATION' in line:
				location = line.split("-")[0]
				print(location)
				for day in dayOfClass:
					self.Calendar[day].append((course, location, \
						int(str(startTime)[-6:-2]), int(str(endTime)[-6:-2])))

path = 'F18_schedule.ics'
achillesCalendar = Calendar()
print(achillesCalendar.classSchedule(path))
print(achillesCalendar.Calendar)












cal = Calendar()
