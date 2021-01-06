from tkinter import Label, Canvas, Button, Tk


class ViewGUI2D:
    def __init__(self, master_grid):
        self.master = Tk()
        self.master_grid = master_grid
        self.master.title("2D grid editor")

        # Big title
        self.label = Label(self.master, text="Artistic Representation of Reader Response - Andrew Chen",
                           font=("Courier", 24))
        self.label.grid(row=0, column=0, columnspan=9, pady=10)

        background_color = 'white smoke'

        # Canvas titles
        self.labelXZ = Label(self.master, text="XZ View", font=("Courier", 14))
        self.labelYZ = Label(self.master, text="YZ View", font=("Courier", 14))
        self.labelXY = Label(self.master, text="XY View", font=("Courier", 14))
        self.labelXZ.grid(row=1, column=0, columnspan=3)
        self.labelYZ.grid(row=1, column=3, columnspan=3)
        self.labelXY.grid(row=1, column=6, columnspan=3)

        # Canvas XZ
        self.canvas_XZ = Canvas(self.master, bg="white", height=360, width=360, background=background_color,
                                highlightthickness=1, highlightbackground="black")
        self.canvas_XZ.grid(row=2, column=0, rowspan=3, columnspan=3, padx=20, pady=10)
        self.set_canvas(self.canvas_XZ)

        # Canvas YZ
        self.canvas_YZ = Canvas(self.master, bg="white", height=360, width=360, background=background_color,
                                highlightthickness=1, highlightbackground="black")
        self.canvas_YZ.grid(row=2, column=3, rowspan=3, columnspan=3, padx=20, pady=10)
        self.set_canvas(self.canvas_YZ)

        # Canvas XY
        self.canvas_XY = Canvas(self.master, bg="white", height=360, width=360, background=background_color,
                                highlightthickness=1, highlightbackground="black")
        self.canvas_XY.grid(row=2, column=6, rowspan=3, columnspan=3, padx=20, pady=10)
        self.set_canvas(self.canvas_XY)

        # Bind painting
        self.canvas_XZ.bind("<B1-Motion>", self.paint(self.canvas_XZ))
        self.canvas_YZ.bind("<B1-Motion>", self.paint(self.canvas_YZ))
        self.canvas_XY.bind("<B1-Motion>", self.paint(self.canvas_XY))

        # Reset buttons
        self.reset_button_XZ = Button(self.master, text="Clear", command=self.reset_canvas(self.canvas_XZ))
        self.reset_button_YZ = Button(self.master, text="Clear", command=self.reset_canvas(self.canvas_YZ))
        self.reset_button_XY = Button(self.master, text="Clear", command=self.reset_canvas(self.canvas_XY))
        self.reset_button_XZ.grid(row=5, column=1, ipadx=5, ipady=5)
        self.reset_button_YZ.grid(row=5, column=4, ipadx=5, ipady=5)
        self.reset_button_XY.grid(row=5, column=7, ipadx=5, ipady=5)

        # Finish button
        self.finish_button = Button(self.master, text="Finish", command=self.finish)  # TODO command to export grid
        self.finish_button.grid(row=6, column=5, ipady=5)

        # Pixelated view button
        self.pixelate_button = Button(self.master, text="Pixelate", command=self.pixelate)
        self.pixelate_button.grid(row=6, column=3, ipady=5)

        self.master.mainloop()

    def finish(self):
        self.set_2dgrids()
        self.master.destroy()

    def set_2dgrids(self):
        XZ_pixelated_matrix = self.get_pixelated_matrix(self.canvas_XZ)
        YZ_pixelated_matrix = self.get_pixelated_matrix(self.canvas_YZ)
        XY_pixelated_matrix = self.get_pixelated_matrix(self.canvas_XY)

        for i in range(18):
            for j in range(18):
                self.master_grid.XZ[i + 1][j + 1] = XZ_pixelated_matrix[i][j]
                self.master_grid.YZ[i + 1][j + 1] = YZ_pixelated_matrix[i][j]
                self.master_grid.XY[i + 1][j + 1] = XY_pixelated_matrix[i][j]

    def reset_canvas(self, canvas):  # for button presses
        def ret():
            canvas.delete('all')
            for i in range(18):
                canvas.create_line(i * 20, 0, i * 20, 360)
                canvas.create_line(0, i * 20, 360, i * 20)

        return ret

    def set_canvas(self, canvas):  # for clearing the canvas
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

    def pixelate(self):
        self.pixelate_canvas(self.canvas_XZ)
        self.pixelate_canvas(self.canvas_YZ)
        self.pixelate_canvas(self.canvas_XY)

    def pixelate_canvas(self, canvas):
        pixelated_matrix = self.get_pixelated_matrix(canvas)
        self.set_canvas(canvas)
        for i in range(18):
            for j in range(18):
                if (pixelated_matrix[i][j]):
                    canvas.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill='black')

    def get_pixelated_matrix(self, canvas):
        pixelated_matrix = [[False for i in range(18)] for j in range(18)]
        for i in range(18):
            for j in range(18):
                if (self.pixel_is_black(canvas, i * 20 + 10, j * 20 + 10)):
                    pixelated_matrix[i][j] = True
        return pixelated_matrix

    def pixel_is_black(self, canvas, x, y):
        ids = canvas.find_overlapping(x, y, x, y)
        if len(ids) > 0:
            index = ids[-1]
            color = canvas.itemcget(index, "fill")
            color = color.upper()
            if color != '':
                return True
        return False
