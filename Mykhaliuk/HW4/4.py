#Is it possible to place a round stage with radius R in a square hall of square S 
#so that there is a passage was at least K from the wall to the stage?​
from tkinter import *

root = Tk()
root.title("homework 4.4")

#Label
radiusLabel = Label(root, text="Enter the radius: ")
radiusLabel.grid(row=0,column=0)

squareLabel = Label(root, text="Enter square size: ")
squareLabel.grid(row=0,column=1)

kvalueLabel = Label(root, text="Enter K:")
kvalueLabel.grid(row=2,column=1)

resaultLabel = Label(root, text="Resault:")
resaultLabel.grid(row=6, column=0)

#Entering the radius&squareSide&K&resault
radiusEntry = Entry(root)
radiusEntry.grid(row=1, column=0)

squareSideEntry = Entry(root)
squareSideEntry.grid(row=1,column=1)

kvalueEntry = Entry(root)
kvalueEntry.grid(row=3,column=1)

resaultEntry = Entry(root, width=50)
resaultEntry.grid(row=7, column=0)

#Canvas 
canvas = Canvas(width=400,height=400, bg="#cedbd2")
canvas.grid(row=5,column=0)

#Drawing the circle
def circle():
    canvas.delete('circle')
    resaultEntry.delete(0, END)
    x=200
    y=200
    r = 0
    if radiusEntry.get():
        r = int(radiusEntry.get())
    id = canvas.create_oval(x-r,y-r,x+r,y+r,tags='circle')
    return id

#Drawing the square 
def square():
    canvas.delete('square')
    resaultEntry.delete(0, END)
    x=200
    y=200
    s = 0
    if squareSideEntry.get():
        s = int(squareSideEntry.get())/2
    id = canvas.create_rectangle(x-s, y-s, x+s, y+s, tags='square')
    return id

#resault func
def resault():
    canvas.delete('line')
    resaultEntry.delete(0, END)
    x=200
    y=200
    realk=(int(squareSideEntry.get()) - int(radiusEntry.get())*2)/2 
    kv = int(kvalueEntry.get())
    halfaSide = int(squareSideEntry.get())/2
    id = canvas.create_line(x+halfaSide-kv, y, x+halfaSide, y, tags='line')
    if kv <=0: clear()
    elif kv <= realk:
        resault_p = (kv, "passage is possible, with", realk - kv, "space units extra")
        resaultEntry.insert(0, resault_p)
    else:
        resault_p = (kv, "passage is not possible with", realk - kv, "space units off")
        resaultEntry.insert(0, resault_p)     
    return id

#clearing 
def clear():
    radiusEntry.delete(0, END)
    squareSideEntry.delete(0, END)
    kvalueEntry.delete(0, END)
    resaultEntry.delete(0, END)
    canvas.delete('all')

#Calling the function for drawing buttons
radiusButton = Button(root, text="Create circle", command=circle)
radiusButton.grid(row=3,column=0)

squareSideButton = Button(root, text="Create square", command=square)
squareSideButton.grid(row=4,column=0)

resaultButton = Button(root, text='Resault', command=resault)
resaultButton.grid(row=4,column=1)

clearButton = Button(root, text="Clear", command=clear)
clearButton.grid(row=7,column=1)

root.mainloop()