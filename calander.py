#Extracting from calander

class Calender():

	def __init__(self):
		self.Calander = []



	def classSchedule(text):
		f = readFile(text)
		contents = f.splitlines(0)
		for line in contents:
			if line == '/n' or line == '':
				continue






def readFile(path):
    with open(path, "rt") as f:
        return f.read()

cal = Calendar()
