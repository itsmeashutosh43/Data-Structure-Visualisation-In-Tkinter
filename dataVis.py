from tkinter import *
class DataStructures:

    def __init__(self,master):

        self.master=master
        self.frame = Frame(master,width=200, height=100)
        self.frame.grid()

        self.stackframe = Frame(master,width=200, height=100)
        self.stackframe.grid()

        self.queueframe = Frame(master,width=200, height=100)
        self.queueframe.grid()



    def homePage(self):
        stackButton = Button(
            self.frame, text="STACK",  command=self.selectStack)
        stackButton.pack(side=LEFT)

        queueButton = Button(self.frame, text="QUEUE", command=self.selectQueue)
        queueButton.pack(side=LEFT)

        canvas = Canvas(self.frame, width=400, height=250)
        canvas.pack()


        self.stackframe.grid_forget()
        self.queueframe.grid_forget()

    def selectQueue(self):
        print("Queue selected")
        #populate frame queue

        frame=self.frame

        self.queueframe.grid()

        canvasQueue = Canvas(self.stackframe, width=400, height=250)
        canvasQueue.pack()

        canvasQueue.create_rectangle(50, 25, 150, 75, fill="white")

        pushButton = Button(
            self.queueframe, text="PUSH", command=self.QueuePush)
        pushButton.pack(side=LEFT)

        popButton = Button(self.queueframe, text="POP", command=self.QueuePOP)
        popButton.pack(side=LEFT)

        frame.grid_forget()
        self.stackframe.grid_forget()



    def selectStack(self):
        print ("Slack sellected")
        # populate frame queue

        self.stackframe.grid()

        frame = self.frame
        frame.grid_forget()
        self.queueframe.grid_forget()

        canvasStack=Canvas(self.stackframe, width=400, height=250)
        canvasStack.pack()

        canvasStack.create_rectangle(50, 25, 150, 75, fill="white")

        pushButton = Button(
            self.stackframe, text="PUSH", command=self.StackPush)
        pushButton.pack(side=LEFT)

        popButton = Button(self.stackframe, text="POP", command=self.StackPOP)
        popButton.pack(side=LEFT)




    def StackPOP(self):
        print("StackPop operation to be shown")

    def StackPush(self):
        print("StackPush operation to be shown")

    def QueuePOP(self):
        print("QueuePop operation to be shown")

    def QueuePush(self):
        print("QueuePush operation to be shown")

root=Tk()

mainObject=DataStructures(root)
mainObject.homePage()


root.mainloop()
