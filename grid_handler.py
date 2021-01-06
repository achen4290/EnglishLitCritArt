from random import shuffle


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

    def set_XYZ_grid(self):
        self.XYZ = [[[True for i in range(20)] for j in range(20)] for k in range(20)]
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

        # factoring in edges, but not removing them
        for i in range(20):
            XZ_count[0][i] += 2
            XZ_count[i][0] += 2
            XZ_count[19][i] += 2
            XZ_count[i][19] += 2
            YZ_count[0][i] += 2
            YZ_count[i][0] += 2
            YZ_count[19][i] += 2
            YZ_count[i][19] += 2
            XY_count[0][i] += 2
            XY_count[i][0] += 2
            XY_count[19][i] += 2
            XY_count[i][19] += 2

        # adding face points
        for i in range(1, 19):
            for j in range(1, 19):
                if self.XYZ[0][i][j]:
                    YZ_count[i][j] += 2
                    face_points.append([0, i, j])
                    face_points.append([19, i, j])
                if self.XYZ[i][0][j]:
                    XZ_count[i][j] += 2
                    face_points.append([i, 0, j])
                    face_points.append([i, 19, j])
                if self.XYZ[i][j][0]:
                    XY_count[i][j] += 2
                    face_points.append([i, j, 0])
                    face_points.append([i, j, 19])

        # adding body points
        for i in range(1, 19):
            for j in range(1, 19):
                for k in range(1, 19):
                    if self.XYZ[i][j][k]:
                        XZ_count[i][k] += 1
                        YZ_count[j][k] += 1
                        XY_count[i][j] += 1
                        body_points.append([i][j][k])

        shuffle(face_points)
        shuffle(body_points)
        points = face_points + body_points

        for p in points:
            x, y, z = p
            if XZ_count[x][z] > 1 and YZ_count[y][z] > 1 and XY_count[x][y] > 1:
                self.XYZ[x][y][z] = False
                XZ_count[x][z] -= 1
                YZ_count[y][z] -= 1
                XY_count[x][y] -= 1
