from random import shuffle, choice


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

class master_grids:
    def __init__(self):
        self.XYZ = empty_3Dgrid()
        self.XZ = [[False for i in range(20)] for j in range(20)]
        self.YZ = [[False for i in range(20)] for j in range(20)]
        self.XY = [[False for i in range(20)] for j in range(20)]

    def flip_list(self, list):
        new_list = [[False for i in range(20)] for j in range(20)]
        for i in range(20):
            for j in range(20):
                if list[i][j]:
                    new_list[i][19 - j] = True
        return new_list

    def set_XYZ_grid(self):
        self.XYZ = [[[True for i in range(20)] for j in range(20)] for k in range(20)]
        self.XZ = self.flip_list(self.XZ)
        self.YZ = self.flip_list(self.YZ)

        for i in range(1, 19):
            for j in range(1, 19):
                if not self.XZ[i][j]:
                    for k in range(20):
                        self.XYZ[i][k][j] = False
                if not self.YZ[i][j]:
                    for k in range(20):
                        self.XYZ[k][i][j] = False
                if not self.XY[i][j]:
                    for k in range(20):
                        self.XYZ[i][j][k] = False

        XZ_count = [[0 for i in range(20)] for j in range(20)]
        YZ_count = [[0 for i in range(20)] for j in range(20)]
        XY_count = [[0 for i in range(20)] for j in range(20)]

        face_points = []
        body_points = []

        # adding body points
        for i in range(1, 19):
            for j in range(1, 19):
                for k in range(1, 19):
                    if self.XYZ[i][j][k]:
                        XZ_count[i][k] += 1
                        YZ_count[j][k] += 1
                        XY_count[i][j] += 1
                        body_points.append([i, j, k])

        # adding face points
        for i in range(1, 19):
            for j in range(1, 19):
                if self.XYZ[0][i][j]:
                    if YZ_count[i][j] == 0:
                        self.XYZ[choice([0, 19])][i][j] = False
                    else:
                        self.XYZ[0][i][j] = False
                        self.XYZ[19][i][j] = False
                if self.XYZ[i][0][j]:
                    if XZ_count[i][j] == 0:
                        self.XYZ[i][choice([0, 19])][j] = False
                    else:
                        self.XYZ[i][0][j] = False
                        self.XYZ[i][19][j] = False
                if self.XYZ[i][j][0]:
                    if XY_count[i][j] == 0:
                        self.XYZ[i][j][choice([0, 19])] = False
                    else:
                        self.XYZ[i][j][0] = False
                        self.XYZ[i][j][19] = False

        shuffle(body_points)

        for p in body_points[0:int(len(body_points) / 3)]:
            x, y, z = p
            if XZ_count[x][z] > 1 and YZ_count[y][z] > 1 and XY_count[x][y] > 1:
                self.XYZ[x][y][z] = False
                XZ_count[x][z] -= 1
                YZ_count[y][z] -= 1
                XY_count[x][y] -= 1

    def count_cubes(self):
        x = 0
        for i in range(20):
            for j in range(20):
                for k in range(20):
                    if self.XYZ[i][j][k]:
                        x += 1
        return x
