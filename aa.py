from tkinter import *
root = Tk()
canvas = Canvas(root,width=200,height=200,bg="white")
canvas.grid()
firstRect = canvas.create_rectangle(0,0,10,10,fill="red")
secondRect = canvas.create_rectangle(5,5,15,15,fill="blue")

root.mainloop()