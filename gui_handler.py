from tkinter import Label, Canvas


class ViewGUI2D:
    def __init__(self, master):
        self.master = master
        master.title("2D grid editor")

        # Big title
        self.label = Label(master, text="Artistic Representation of Reader Response - Andrew Chen",
                           font=("Courier", 24))
        self.label.grid(row=0, column=0, columnspan=9, pady=10)

        background_color = 'white smoke'

        # Canvas titles
        self.labelXZ = Label(master, text="XZ View", font=("Courier",14))
        self.labelYZ = Label(master, text="YZ View", font=("Courier", 14))
        self.labelXY = Label(master, text="XY View", font=("Courier", 14))
        self.labelXZ.grid(row=1,column=0,columnspan=3)
        self.labelYZ.grid(row=1, column=3, columnspan=3)
        self.labelXY.grid(row=1, column=6, columnspan=3)

        # Canvas XZ
        self.canvasXZ = Canvas(master, bg="white", height=360, width=360, background=background_color,
                               highlightthickness=1, highlightbackground="black")
        self.canvasXZ.grid(row=2, column=0, rowspan=3, columnspan=3, padx=20, pady=20)
        self.reset_canvas(self.canvasXZ)

        # Canvas YZ
        self.canvasYZ = Canvas(master, bg="white", height=360, width=360, background=background_color,
                               highlightthickness=1, highlightbackground="black")
        self.canvasYZ.grid(row=2, column=3, rowspan=3, columnspan=3, padx=20, pady=20)
        self.reset_canvas(self.canvasYZ)

        # Canvas XY
        self.canvasXY = Canvas(master, bg="white", height=360, width=360, background=background_color,
                               highlightthickness=1, highlightbackground="black")
        self.canvasXY.grid(row=2, column=6, rowspan=3, columnspan=3, padx=20, pady=20)
        self.reset_canvas(self.canvasXY)

        # Reset buttons


        # Bind painting
        self.canvasXZ.bind("<B1-Motion>", self.paint(self.canvasXZ))
        self.canvasYZ.bind("<B1-Motion>", self.paint(self.canvasYZ))
        self.canvasXY.bind("<B1-Motion>", self.paint(self.canvasXY))

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def reset_canvas(self, canvas):
        canvas.delete('all')
        for i in range(18):
            canvas.create_line(i * 20, 0, i * 20, 360)
            canvas.create_line(0, i * 20, 360, i * 20)

    def paint(self, canvas):
        def ret(event):
            radius = 10
            x1, y1 = (event.x - radius), (event.y - radius)
            x2, y2 = (event.x + radius), (event.y + radius)
            canvas.create_oval(x1, y1, x2, y2, fill='black')
        return ret