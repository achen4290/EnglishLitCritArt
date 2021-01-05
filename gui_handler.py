from tkinter import Label, Canvas


class ViewGUI2D:
    def __init__(self, master):
        self.master = master
        master.title("2D grid editor")

        self.label = Label(master, text="Artistic Representation of Reader Response - Andrew Chen")
        self.label.grid(row=0, column=0, columnspan=9)

        self.canvasXZ = Canvas(master, bg="white", height=360, width=360)
        self.canvasXZ.grid(row=1, column=0, rowspan=3, columnspan=3, padx=20)

        self.canvasYZ = Canvas(master, bg="white", height=360, width=360)
        self.canvasYZ.grid(row=1, column=3, rowspan=3, columnspan=3, padx=20)

        self.canvasXY = Canvas(master, bg="white", height=360, width=360)
        self.canvasXY.grid(row=1, column=6, rowspan=3, columnspan=3, padx=20)

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")
