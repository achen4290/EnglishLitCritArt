import grid_handler as gd
import gui_handler as gui_handler
import plot_handler as pd

master_grid = gd.master_grids()  # initializes the grid
my_gui = gui_handler.ViewGUI2D(master_grid)  # Pops up GUI to set the grid
master_grid.set_XYZ_grid()  # Calculates the 3D grid given the 2D grid
pd.plot_grid(master_grid)  # Plots the 3D grid
