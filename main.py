import tkinter as TK

import grid_handler as gd
import gui_handler as gui_handler

master_grid = gd.empty_grid()

root = TK.Tk()
my_gui = gui_handler.ViewGUI2D(root)
root.mainloop()
