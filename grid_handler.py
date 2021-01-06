def empty_3Dgrid():
    grid = [[[False for i in range(20)] for j in range(20)] for k in range(20)]
    for i in range(20):
        grid[0][0][i] = True
        grid[0][19][i] = True
        grid[19][0][i] = True
        grid[19][19][i] = True
        grid[0][i][0] = True
        grid[0][i][19] = True
        grid[19][i][0] = True
        grid[19][i][19] = True
        grid[i][0][0] = True
        grid[i][0][19] = True
        grid[i][19][0] = True
        grid[i][19][19] = True
    return grid


def preset_faces():
    # TODO - get grid for smile/frown/neutral
    pass


def preset_animals():
    # TODO - get grid for panda/cat/horse
    pass


def preset_braingames():
    # TODO - get grid for brain games
    pass


class master_grids:
    def __init__(self):
        self.XYZ = empty_3Dgrid()
        self.XZ = [[False for i in range(20)] for j in range(20)]
        self.YZ = [[False for i in range(20)] for j in range(20)]
        self.XY = [[False for i in range(20)] for j in range(20)]
