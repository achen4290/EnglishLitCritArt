import plotly.graph_objects as go


def plot_grid(master_grid_3D):
    cubes = []
    for a in range(20):
        for b in range(20):
            for c in range(20):
                if master_grid_3D[a][b][c]:
                    cubes.append(
                        go.Mesh3d(
                            x=[a, a, a + 1, a + 1, a, a, a + 1, a + 1],
                            y=[b, b + 1, b + 1, b, b, b + 1, b + 1, b],
                            z=[c, c, c, c, c + 1, c + 1, c + 1, c + 1],
                            color='black',
                            i=[7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6],
                            j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                            k=[0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2]
                        )
                    )

    fig = go.Figure(data=cubes)
    fig.show()
