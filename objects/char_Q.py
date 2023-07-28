from models.vertex import Vertex
from models.object import Object

# The model of Q
VERTEX_1 = Vertex(x=0.0, y=0.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.0, y=0.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=0.3333333333333333, y=0.2, z=-0.5, id=2)
VERTEX_4 = Vertex(x=0.6666666666666666, y=0.2, z=-0.5, id=3)
VERTEX_5 = Vertex(x=0.3333333333333333, y=0.7032258064516129, z=-0.5, id=4)
VERTEX_6 = Vertex(x=0.6666666666666666, y=0.7032258064516129, z=-0.5, id=5)
VERTEX_7 = Vertex(x=0.0, y=0.9032258064516129, z=-0.5, id=6)
VERTEX_8 = Vertex(x=1.0, y=0.9032258064516129, z=-0.5, id=7)
VERTEX_9 = Vertex(x=0.3333333333333333, y=0.9032258064516129, z=-0.5, id=8)
VERTEX_10 = Vertex(x=0.6666666666666666, y=0.9032258064516129, z=-0.5, id=9)
VERTEX_11 = Vertex(x=0.3333333333333333, y=1.0, z=-0.5, id=10)
VERTEX_12 = Vertex(x=0.6666666666666666, y=1.0, z=-0.5, id=11)
VERTEX_13 = Vertex(x=0.0, y=0.0, z=0.5, id=12)
VERTEX_14 = Vertex(x=1.0, y=0.0, z=0.5, id=13)
VERTEX_15 = Vertex(x=0.3333333333333333, y=0.2, z=0.5, id=14)
VERTEX_16 = Vertex(x=0.6666666666666666, y=0.2, z=0.5, id=15)
VERTEX_17 = Vertex(x=0.3333333333333333, y=0.7032258064516129, z=0.5, id=16)
VERTEX_18 = Vertex(x=0.6666666666666666, y=0.7032258064516129, z=0.5, id=17)
VERTEX_19 = Vertex(x=0.0, y=0.9032258064516129, z=0.5, id=18)
VERTEX_20 = Vertex(x=1.0, y=0.9032258064516129, z=0.5, id=19)
VERTEX_21 = Vertex(x=0.3333333333333333, y=0.9032258064516129, z=0.5, id=20)
VERTEX_22 = Vertex(x=0.6666666666666666, y=0.9032258064516129, z=0.5, id=21)
VERTEX_23 = Vertex(x=0.3333333333333333, y=1.0, z=0.5, id=22)
VERTEX_24 = Vertex(x=0.6666666666666666, y=1.0, z=0.5, id=23)

vertices = [
    VERTEX_1,
    VERTEX_2,
    VERTEX_3,
    VERTEX_4,
    VERTEX_5,
    VERTEX_6,
    VERTEX_7,
    VERTEX_8,
    VERTEX_9,
    VERTEX_10,
    VERTEX_11,
    VERTEX_12,
    VERTEX_13,
    VERTEX_14,
    VERTEX_15,
    VERTEX_16,
    VERTEX_17,
    VERTEX_18,
    VERTEX_19,
    VERTEX_20,
    VERTEX_21,
    VERTEX_22,
    VERTEX_23,
    VERTEX_24,
]

faces = [[12, 13, 19, 21, 23, 22, 20, 18], [0, 6, 8, 10, 11, 9, 7, 1], [18, 6, 0, 12], [12, 0, 1, 13], [13, 1, 7, 19], [19, 7, 9, 21], [21, 9, 11, 23], [
    23, 11, 10, 22], [22, 10, 8, 20], [20, 8, 6, 18], [14, 2, 3, 15], [15, 3, 5, 17], [17, 5, 4, 16], [16, 4, 2, 14], [14, 15, 17, 16], [2, 4, 5, 3]]

# v 1.0 1.0 -0.5
# v 2.0 1.0 -0.5
# v 1.3333333333333333 1.2 -0.5
# v 1.6666666666666665 1.2 -0.5
# v 1.3333333333333333 1.7032258064516128 -0.5
# v 1.6666666666666665 1.7032258064516128 -0.5
# v 1.0 1.903225806451613 -0.5
# v 2.0 1.903225806451613 -0.5
# v 1.3333333333333333 1.903225806451613 -0.5
# v 1.6666666666666665 1.903225806451613 -0.5
# v 1.3333333333333333 2.0 -0.5
# v 1.6666666666666665 2.0 -0.5
# v -1.0 0.0 0.5
# v 0.0 0.0 0.5
# v -0.6666666666666667 0.2 0.5
# v -0.33333333333333337 0.2 0.5
# v -0.6666666666666667 0.7032258064516129 0.5
# v -0.33333333333333337 0.7032258064516129 0.5
# v -1.0 0.9032258064516129 0.5
# v 0.0 0.9032258064516129 0.5
# v -0.6666666666666667 0.9032258064516129 0.5
# v -0.33333333333333337 0.9032258064516129 0.5
# v -0.6666666666666667 1.0 0.5
# v -0.33333333333333337 1.0 0.5

# f 13 14 20 22 24 23 21 19
# f 1 7 9 11 12 10 8 2
# f 19 7 1 13
# f 13 1 2 14
# f 14 2 8 20
# f 20 8 10 22
# f 22 10 12 24
# f 24 12 11 23
# f 23 11 9 21
# f 21 9 7 19
# f 15 3 4 16
# f 16 4 6 18
# f 18 6 5 17
# f 17 5 3 15
# f 15 16 18 17 hole
# f 3 5 6 4 hole
