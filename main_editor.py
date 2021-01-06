import json

import grid_handler as gd
import gui_handler as gui_handler

master_grid = gd.master_grids()  # initializes the grid
gui_handler.grid_editor_GUI(master_grid)  # show grid editor GUI
master_grid.set_XYZ_grid()  # Calculates the 3D grid given the 2D grid

# Saves 3D grid
with open("grids/Most Recent Save.json", 'w') as f:
    json.dump(master_grid.XYZ, f)
