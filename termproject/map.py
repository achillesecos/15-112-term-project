# Basic Animation Framework
import module_manager
module_manager.review()
from tkinter import *
import cv2
from PIL import Image, ImageTk
from dijkstra import *
import math



graph = Graph()

def nodeDistance(self,othernode):
    return math.sqrt((self.x - othernode.x)**2 - (self.y - othernode.y)**2)

class Node:
    #coordinates of a node
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #distance between two nodes



    

    def __hash__(self):
        return hash((self.x,self.y))


graph.addEdge(Node(0,0), Node(20,20), nodeDistance(Node(0,0), Node(20,20)))
#place each node













####################################
# customize these functions
####################################

def init(data):
    data.img = Image.open("cmumap.png")
    data.resizedImg = data.img.resize((data.width, data.height))
    data.picture = ImageTk.PhotoImage(data.img)

def mousePressed(event, data):
    # use event.x and event.y

    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    canvas.create_image(0, 0,anchor = NW, image = data.picture)
    
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

run(1050, 850)