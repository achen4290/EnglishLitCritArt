import json
from os import walk

import gui_handler as gui_handler
import plot_handler as ph

_, _, filenames = next(walk('grids'))
selection = ['']
gui_handler.grid_plotter_GUI(filenames, selection)
grid = []
with open('grids/' + selection[0][0] + '.json', 'r') as f:
    grid = json.load(f)
ph.plot_grid(grid)
