import numpy as np

point_1 = np.array((0, 0))
point_2 = np.array((3, 3))

def dist(point_1, point_2):
    dist = np.sqrt(np.dot(point_1-point_2, point_1-point_2))
    print(dist)

dist(point_1, point_2)