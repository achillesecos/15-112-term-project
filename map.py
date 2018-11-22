# Basic Animation Framework
import module_manager
module_manager.review()
from tkinter import *
import cv2
from PIL import Image, ImageTk
from dijkstra import *
import math
#from page1 import *



graph = Graph()

def nodeDistance(self,othernode):
    return math.sqrt(abs((self.x - othernode.x)**2 - (self.y - othernode.y)**2))

class Node:
    #coordinates of a node
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #distance between two nodes

    def __repr__(self):
        return str(self.x) + "," + str(self.y)

    

    def __hash__(self):
        return hash((self.x,self.y))


node1 = Node(758,150)
node2 = Node(702,262)
node3 = Node(686,247)


#place each node
graph.addEdge(node1, node2, nodeDistance(node1, node2))
graph.addEdge(node2, node3, nodeDistance(node2, node3))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
# graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))



print(dijkstra(graph,node1,node3))

def getNeigboringNodes(node):
    neighboringNodes = [dijkstra.getNeighbors(node)]
    return neighboringNodes

def recommendPlace(node):
    pass

def readFile(path):
    with open(path, "rt") as f:
        return f.read()




def classScheduleAutomatic():
    pass

def classScheduleManual(input):
    classes = {}
    for theClass in input:
        classes[theClass] = getNeigboringNodes(theClass)
    return classes

def getIntersectionNodes(node1,node2):
    set1 = set(getIntersectionNodes(node1))
    set2 = set(getIntersectionNodes(node2))
    return set1.intersection(set2)
    

#user inputs the different classes
#we need to order them in order of time
#iterate throughthem and add them into the dictionary classes 








def init(data):
    data.img = Image.open("cmumap1.jpg")
    data.resizedImg = data.img.resize((data.width, data.height))
    data.picture = ImageTk.PhotoImage(data.img)
    data.txt1X = 20
    data.txt1Y = 20
    data.txt2X = 20
    data.txt2Y = 60


def texts(canvas,data):
    #MUST CHANGE TO create_text
    canvas.create_text(data.txt1X, data.txt1Y, fill = "blue", \
        text = "Directions", anchor = NW)
    canvas.create_text(data.txt2X, data.txt2Y, fill = "blue", \
        text = "Import Schedule", anchor = NW)

# def changeScreen(data, x, y):
#     #checks to see if user clicks on the two text buttons
#     if((x >= data.txt1X and x <= data.txt1X + 30 and y >= data.txt1Y and \
#         y <= data.txt1Y + 30) or (x >= data.txt2X and x <= data.txt2X + 30 and \
#         y >= data.txt2Y and y <= data.txt2Y + 30)):
#         page1.run()
#     pass

    

def drawSquare(data):
    pass

def mousePressed(event, data):
    # use event.x and event.y
    #changeScreen(data, event.x, event.y)
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    canvas.create_image(0, 0,anchor = NW, image = data.picture)
    canvas.create_text(data.width/2 + 60, 20, fill = "maroon", \
    font = "Times 30 bold", text= "Carnegie Mellon University")
    texts(canvas, data)
    
#mapImg = cv2.imread("cmumap.png")
#img = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarry(mapImg))
#canvas.create_image(0,0,anchor = NW, image = img)
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    #height, width, no_channels = data.picture.shape
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(810, 580)