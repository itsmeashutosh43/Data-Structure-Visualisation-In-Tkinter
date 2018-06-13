from tkinter import *
from tkinter import messagebox


class DataStructures:

    def __init__(self,master):

        self.master=master
        self.frame = Frame(master,width=200, height=100)
        self.frame.grid()

        self.stackframe = Frame(master,width=200, height=100)
        self.stackframe.grid()

        self.queueframe = Frame(master,width=200, height=100)
        self.queueframe.grid()
        self.StackX2=100
        self.StackX1 = 25
        self.StackY2 = 200
        self.StackY1 = 100
        self.QueueX1 = 50
        self.QueueX2 = 150
        self.QueueY1 = 80
        self.QueueY2 = 150
        self.labelID=0
        self.fillk = 0

        self.fill=0

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.homePage)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)

    def About(self):
        pass





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

        self.canvasQueue = Canvas(self.queueframe, width=400, height=250)
        self.canvasQueue.pack()

        self.canvasQueue.create_rectangle(self.QueueX1, self.QueueY1, self.QueueX2, self.QueueY2, fill="white")

        pushButton = Button(
            self.queueframe, text="PUSH", command=self.QueuePush)
        pushButton.pack(side=LEFT)

        popButton = Button(self.queueframe, text="POP", command=self.QueuePOP)
        popButton.pack(side=LEFT)

        frame.grid_forget()
        self.stackframe.grid_forget()



    def selectStack(self):

        print(self.StackX1, self.StackY1, self.StackX2, self.StackY2)
        print ("Slack sellected")

        self.stackframe.grid()

        frame = self.frame
        frame.grid_forget()
        self.queueframe.grid_forget()

        self.canvasStack=Canvas(self.stackframe, width=400, height=250)
        self.canvasStack.pack()

        self.canvasStack.create_rectangle(self.StackX1, self.StackY1, self.StackX2, self.StackY2, fill="white")

        pushButton = Button(
            self.stackframe, text="PUSH", command=self.StackPush)
        pushButton.pack(side=LEFT)

        popButton = Button(self.stackframe, text="POP", command=self.StackPOP)
        popButton.pack(side=LEFT)

    def StackPOP(self):
        if self.fill<=0:
            self.fill=0
            messagebox.showerror("Error", "The stack is empty")
        else:
            self.canvasStack.delete(self.labelID)
            delY=self.StackY2-self.StackY1

            newCoordinateY1 = 0.2 * (self.fill)

            newCoordinateY2 = 0.2 * (self.fill-1)

            print (self.fill)
            self.canvasStack.create_rectangle(self.StackX1,   self.StackY1+(1-newCoordinateY1)*delY, self.StackX2,
                                              self.StackY1 + (1 - newCoordinateY2) * delY, fill="white")
            self.labelID = self.canvasStack.create_text((self.QueueX1 + self.QueueX2) / 2 - 35,
                                                        self.StackY1 + (1 - newCoordinateY2) * delY + 10,
                                                        text="sp", font=('Arial', '12', 'bold'))




        self.fill-=1
        print("StackPop operation to be shown")

    def StackPush(self):

        self.fillk = 0
        self.fill += 1
        print(self.fill)
        print("StackPush operation to be shown")

        #self.canvasStack.create_line()
        if self.fill >=6:
            self.fill=6
            messagebox.showerror("Error","The stack  is full")

        else:
            delY = self.StackY2 - self.StackY1

            newCoordinateY1 = 0.2 * (self.fill)
            self.canvasStack.create_rectangle(self.StackX1,self.StackY1+(1-newCoordinateY1)*delY, self.StackX2,
                                             self.StackY2, fill="blue")
            self.labelID = self.canvasStack.create_text((self.QueueX1 + self.QueueX2) / 2-35,
                                                        self.StackY1 + (1 - newCoordinateY1) * delY+10,
                                                        text="sp", font=('Arial', '12', 'bold'))

    def QueuePOP(self):
        print("QueuePop operation to be shown")
        if self.fill<=0:
            messagebox.showerror("Error", "The queue is empty")



        else:
            self.canvasQueue.delete(self.labelID)
            delX = self.QueueX2 - self.QueueX1

            newCoordinateX1 = 0.2 * (self.fill)


            print(self.fill)
            self.canvasQueue.create_rectangle(self.QueueX2 -(0.2*(self.fillk+1))* delX, self.QueueY1 ,
                                              self.QueueX2 -( 0.2 * (self.fillk ))*delX,
                                              self.QueueY2 , fill="white")
            #self.labelID=self.canvasQueue.create_text(self.QueueX2- (1 - newCoordinateX1) * delX,self.QueueY1,text="sp")
            self.fillk += 1
            self.labelID = self.canvasQueue.create_text(self.QueueX2 -(0.2*(self.fillk+1))* delX + 10,
                                                        (self.QueueY1 + self.QueueY2) / 2,
                                                        text="sp",font = ('Arial', '12','bold'))


        self.fill-=1

    def QueuePush(self):
        self.fillk = 0
        self.fill+=1
        print("QueuePush operation to be shown")
        if self.fill >=6:
            self.fill=5
            messagebox.showerror("Error","The queue  is full")

        else:

            delX = self.QueueX2 - self.QueueX1

            newCoordinateX1 = 0.2 * (self.fill)




            self.canvasQueue.create_rectangle(self.QueueX1+(1-newCoordinateX1)*delX,self.QueueY1, self.QueueX2,
                                             self.QueueY2, fill="blue")

            self.labelID = self.canvasQueue.create_text(self.QueueX2 - 10,
                                                        (self.QueueY1 + self.QueueY2) / 2,
                                                        text="sp",font = ('Arial', '12','bold'))




root=Tk()

mainObject=DataStructures(root)
mainObject.homePage()


root.mainloop()
