# Basic Animation Framework
# import module_manager
# module_manager.review()
from tkinter import *
import cv2
from PIL import Image, ImageTk
from dijkstra import *
import math
#from page1 import *



graph = Graph()

def nodeDistance(self,othernode):
    return math.sqrt((self.x - othernode.x)**2 + (self.y - othernode.y)**2)

class Node:
    #coordinates of a node
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #distance between two nodes

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    

    def __hash__(self):
        return hash((self.x,self.y))


node1 = Node(758,150)
node2 = Node(702,262)
node3 = Node(686,247)
node4 = Node(752,287)
node5 = Node(653,149)
node6 = Node(640,110)
node7 = Node(668,328)
node8 = Node(629,314)
node9 = Node(615,272)
node10 = Node(605,245)
node11 = Node(647,231)
node12 = Node(617,345)
node13 = Node(585,358)
node14 = Node(613,452)
node15 = Node(619,470)
node16 = Node(610,473)
node17 = Node(600,457)
node18 = Node(562,365)
node19 = Node(546,292)
node20 = Node(537,267)
node21 = Node(512,197)
node22 = Node(539,295)
node23 = Node(549,453)
node24 = Node(561,488)
node25 = Node(531,498)
node26 = Node(519,463)
node27 = Node(493,391)
node28 = Node(466,321)
node29 = Node(463,309)
node30 = Node(442,250)
node31 = Node(433,220)
node32 = Node(427,190)
node33 = Node(400,231)
node34 = Node(393,201)
node35 = Node(372,214)
node36 = Node(361,204)
node37 = Node(386,245)
node38 = Node(395,266)
node39 = Node(415,326)
node40 = Node(455,363)
node41 = Node(419,336)
node42 = Node(443,406)
node43 = Node(454,436)
node44 = Node(462,460)
node45 = Node(469,479)
node46 = Node(472,485)
node47 = Node(483,516)
node48 = Node(355,279)
node49 = Node(413,448)
node50 = Node(422,474)
node51 = Node(391,483)
node52 = Node(383,460)
node53 = Node(374,462)
node54 = Node(362,494)
node55 = Node(352,332)
node56 = Node(312,307)
node57 = Node(283,277)
node58 = Node(301,332)
node59 = Node(279,360)
node60 = Node(277,371)
node61 = Node(299,437)
node62 = Node(355,318)
node63 = Node(313,482)
node64 = Node(316,490)
node65 = Node(321,506)
node66 = Node(302,494)
node67 = Node(302,575)
node68 = Node(287,536)
node69 = Node(266,540)
node70 = Node(245,480)
node71 = Node(254,465)
node72 = Node(224,389)
node73 = Node(190,342)
node74 = Node(340,93)
node75 = Node(258,7)
node76 = Node(439,420)



# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()
# node = Node()






#place each node
graph.addEdge(node1, node2, nodeDistance(node1, node2))
graph.addEdge(node1, node6, nodeDistance(node1, node6))
graph.addEdge(node2, node4, nodeDistance(node2, node4))
graph.addEdge(node2, node7, nodeDistance(node2, node7))
graph.addEdge(node2, node3, nodeDistance(node2, node3))
graph.addEdge(node3, node5, nodeDistance(node3, node5))
graph.addEdge(node5, node6, nodeDistance(node5, node6))
graph.addEdge(node5, node21, nodeDistance(node5, node21))
graph.addEdge(node6, node32, nodeDistance(node6, node32))
graph.addEdge(node3, node9, nodeDistance(node3, node9))
graph.addEdge(node9, node10, nodeDistance(node9, node10))
graph.addEdge(node10, node11, nodeDistance(node10, node11))
graph.addEdge(node10, node20, nodeDistance(node10, node20))
graph.addEdge(node9, node19, nodeDistance(node9, node19))
graph.addEdge(node9, node8, nodeDistance(node9, node8))
graph.addEdge(node8, node12, nodeDistance(node8, node12))
graph.addEdge(node7, node12, nodeDistance(node7, node12))
graph.addEdge(node12, node13, nodeDistance(node12, node13))
graph.addEdge(node13, node14, nodeDistance(node13, node14))
graph.addEdge(node14, node15, nodeDistance(node14, node15))
graph.addEdge(node15, node16, nodeDistance(node15, node16))
graph.addEdge(node16, node17, nodeDistance(node16, node17))
graph.addEdge(node17, node14, nodeDistance(node17, node14))
graph.addEdge(node16, node24, nodeDistance(node16, node24))
graph.addEdge(node19, node20, nodeDistance(node19, node20))
graph.addEdge(node19, node22, nodeDistance(node19, node22))
graph.addEdge(node20, node21, nodeDistance(node20, node21))
graph.addEdge(node22, node18, nodeDistance(node22, node18))
graph.addEdge(node18, node27, nodeDistance(node18, node27))
graph.addEdge(node22, node28, nodeDistance(node22, node28))
graph.addEdge(node28, node27, nodeDistance(node28, node27))
graph.addEdge(node26, node27, nodeDistance(node26, node27))
graph.addEdge(node26, node25, nodeDistance(node26, node25))
graph.addEdge(node26, node23, nodeDistance(node26, node23))
graph.addEdge(node23, node24, nodeDistance(node23, node24))
graph.addEdge(node24, node25, nodeDistance(node24, node25))
graph.addEdge(node28, node29, nodeDistance(node28, node29))
graph.addEdge(node29, node30, nodeDistance(node29, node30))
graph.addEdge(node30, node31, nodeDistance(node30, node31))
graph.addEdge(node31, node32, nodeDistance(node31, node32))

graph.addEdge(node60, node72, nodeDistance(node60, node72))
graph.addEdge(node65, node64, nodeDistance(node65, node64))
graph.addEdge(node64, node63, nodeDistance(node64, node63))
graph.addEdge(node64, node66, nodeDistance(node64, node66))
graph.addEdge(node60, node61, nodeDistance(node60, node61))
graph.addEdge(node63, node53, nodeDistance(node63, node53))
graph.addEdge(node49, node51, nodeDistance(node49, node51))
graph.addEdge(node51, node50, nodeDistance(node51, node50))
graph.addEdge(node44, node50, nodeDistance(node44, node50))
graph.addEdge(node43, node49, nodeDistance(node43, node49))
graph.addEdge(node49, node52, nodeDistance(node49, node52))
graph.addEdge(node51, node52, nodeDistance(node51, node52))
graph.addEdge(node52, node53, nodeDistance(node52, node53))
graph.addEdge(node51, node54, nodeDistance(node51, node54))
graph.addEdge(node54, node65, nodeDistance(node54, node65))
graph.addEdge(node32, node34, nodeDistance(node32, node34))
graph.addEdge(node31, node33, nodeDistance(node31, node33))
graph.addEdge(node29, node39, nodeDistance(node29, node39))
graph.addEdge(node28, node41, nodeDistance(node28, node41))
graph.addEdge(node28, node40, nodeDistance(node28, node40))
graph.addEdge(node27, node40, nodeDistance(node27, node40))
graph.addEdge(node27, node42, nodeDistance(node27, node42))
graph.addEdge(node72, node71, nodeDistance(node72, node71))
graph.addEdge(node26, node45, nodeDistance(node26, node45))
graph.addEdge(node25, node47, nodeDistance(node25, node47))
graph.addEdge(node47, node46, nodeDistance(node47, node46))
graph.addEdge(node46, node45, nodeDistance(node46, node45))
graph.addEdge(node45, node44, nodeDistance(node45, node44))
graph.addEdge(node44, node43, nodeDistance(node44, node43))
graph.addEdge(node43, node42, nodeDistance(node43, node42))
graph.addEdge(node42, node40, nodeDistance(node42, node40))
graph.addEdge(node73, node72, nodeDistance(node73, node72))
graph.addEdge(node42, node41, nodeDistance(node42, node41))
graph.addEdge(node40, node41, nodeDistance(node40, node41))
graph.addEdge(node39, node41, nodeDistance(node39, node41))
graph.addEdge(node38, node39, nodeDistance(node38, node39))
graph.addEdge(node38, node37, nodeDistance(node38, node37))
graph.addEdge(node37, node33, nodeDistance(node37, node33))
graph.addEdge(node37, node35, nodeDistance(node37, node35))
graph.addEdge(node35, node34, nodeDistance(node35, node34))
graph.addEdge(node57, node73, nodeDistance(node57, node73))
graph.addEdge(node35, node36, nodeDistance(node35, node36))
graph.addEdge(node38, node48, nodeDistance(node38, node48))
graph.addEdge(node48, node62, nodeDistance(node48, node62))
graph.addEdge(node62, node55, nodeDistance(node62, node55))
graph.addEdge(node35, node57, nodeDistance(node35, node57))
graph.addEdge(node35, node57, nodeDistance(node35, node57))
graph.addEdge(node56, node57, nodeDistance(node56, node57))
graph.addEdge(node57, node58, nodeDistance(node57, node58))
graph.addEdge(node58, node59, nodeDistance(node58, node59))
graph.addEdge(node59, node60, nodeDistance(node59, node60))
graph.addEdge(node70, node71, nodeDistance(node70, node71))
graph.addEdge(node70, node69, nodeDistance(node70, node69))
graph.addEdge(node69, node68, nodeDistance(node69, node68))
graph.addEdge(node68, node67, nodeDistance(node68, node67))
graph.addEdge(node47, node67, nodeDistance(node47, node67))
graph.addEdge(node36, node74, nodeDistance(node36, node74))
graph.addEdge(node74, node75, nodeDistance(node74, node75))
graph.addEdge(node42, node76, nodeDistance(node42, node76))
graph.addEdge(node76, node49, nodeDistance(node76, node49))
graph.addEdge(node49, node50, nodeDistance(node49, node50))

#print(dijkstra(graph,node1,node10))



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
    set1 = set(getIntersectionNodes(node1))
    set2 = set(getIntersectionNodes(node2))
    return set1.intersection(set2)
    

#user inputs the different classes
#we need to order them in order of time
#iterate throughthem and add them into the dictionary classes 


def getNearestNode(graph, x, y):
    minVal = float('inf')
    desiredNode = None
    for node in graph.graph.keys():
        if math.sqrt((node.x - x)**2 + (node.y - y)**2) \
        < minVal:
            minVal = math.sqrt((node.x - x)**2 + \
            (node.y - y)**2)
            desiredNode = node
    return desiredNode, minVal



def init(data):
    data.img = Image.open("cmumap1.jpg")
    data.resizedImg = data.img.resize((data.width, data.height))
    data.picture = ImageTk.PhotoImage(data.img)
    data.txt1X = 20
    data.txt1Y = 30
    data.txt2X = 20
    data.txt2Y = 170
    data.graph = graph
    data.previous = dijkstra(graph, node1, node75)[1]
    data.start = node1
    data.end = node75
    data.bound = 15


def texts(canvas,data):
    #MUST CHANGE TO create_text
    canvas.create_text(data.txt1X, data.txt1Y, fill = "blue", \
        text = "Directions", font = "Times 25 bold", anchor = NW)
    canvas.create_text(data.txt1X, data.txt1Y + 50, fill = 'blue', \
        text = "Select a start and end point", font = 'Times 15', anchor = NW)
    canvas.create_text(data.txt2X, data.txt2Y, fill = "blue", \
        text = "Import Schedule", font= "Times 25 bold", anchor = NW)
    canvas.create_text(data.txt2X, data.txt2Y + 50, fill = 'blue', \
        text = "Click here to import your schedule", font = 'Times 15', anchor = NW)

# def changeScreen(data, x, y):
#     #checks to see if user clicks on the two text buttons
#     if((x >= data.txt1X and x <= data.txt1X + 30 and y >= data.txt1Y and \
#         y <= data.txt1Y + 30) or (x >= data.txt2X and x <= data.txt2X + 30 and \
#         y >= data.txt2Y and y <= data.txt2Y + 30)):
#         page1.run()
#     pass

    
def drawPath(canvas, previous, start, end):
    while previous[end] != None:
        canvas.create_line(end.x,end.y,previous[end].x, \
            previous[end].y, fill = 'blue', width = 3)
        end = previous[end]
        print(previous)

def resetButton(canvas, data):
    canvas.create_rectangle(data.txt1X, data.txt1Y + 70, data.txt1X + 30, \
        data.txt1Y + 100, outline = 'blue')
    canvas.create_text(data.txt1X + 20, data.txt1Y + 80, fill = 'blue', \
        text = "Reset", anchor = NW)



def mousePressed(event, data):
    # use event.x and event.y
    #changeScreen(data, event.x, event.y)
    desiredNode, minDistance = getNearestNode(data.graph, event.x, event.y)
    if minDistance <= data.bound:
        print(getNearestNode(data.graph, event.x, event.y))

    if event.x >= data.txt1X and event.x <= data.txt2X + 70 and \
    event.y >= data.txt1Y and event.txt2Y <= data.txt2Y + 70:
        data.start = None
        data.end = None

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    canvas.create_image(0, 0,anchor = NW, image = data.picture)
    canvas.create_text(data.width/2 + 60, 20, fill = "maroon", \
    font = "Times 30 bold", text= "Carnegie Mellon University")
    texts(canvas, data)
    drawPath(canvas, data.previous, data.start, data.end)
    resetButton(canvas,data)
    
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