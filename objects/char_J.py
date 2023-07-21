from models.vertex import Vertex
from models.object import Object

# The model of J
VERTEX_1 = Vertex(x=1.3333333333333333, y=1.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.817204301075269, y=1.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=2.0, y=1.1285714285714286, z=-0.5, id=2)
VERTEX_4 = Vertex(x=1.3333333333333333, y=1.2214285714285715, z=-0.5, id=3)
VERTEX_5 = Vertex(x=1.6666666666666665, y=1.2285714285714286, z=-0.5, id=4)
VERTEX_6 = Vertex(x=1.0, y=1.6714285714285713, z=-0.5, id=5)
VERTEX_7 = Vertex(x=1.3333333333333333, y=1.6714285714285713, z=-0.5, id=6)
VERTEX_8 = Vertex(x=1.3333333333333333, y=1.7785714285714285, z=-0.5, id=7)
VERTEX_9 = Vertex(x=1.6666666666666665, y=1.7785714285714285, z=-0.5, id=8)
VERTEX_10 = Vertex(x=1.0, y=2.0, z=-0.5, id=9)
VERTEX_11 = Vertex(x=2.0, y=2.0, z=-0.5, id=10)
VERTEX_12 = Vertex(x=-0.6666666666666667, y=0.0, z=0.5, id=11)
VERTEX_13 = Vertex(x=-0.18279569892473113, y=0.0, z=0.5, id=12)
VERTEX_14 = Vertex(x=0.0, y=0.12857142857142856, z=0.5, id=13)
VERTEX_15 = Vertex(x=-0.6666666666666667, y=0.22142857142857142, z=0.5, id=14)
VERTEX_16 = Vertex(x=-0.33333333333333337, y=0.22857142857142856, z=0.5, id=15)
VERTEX_17 = Vertex(x=-1.0, y=0.6714285714285714, z=0.5, id=16)
VERTEX_18 = Vertex(x=-0.6666666666666667, y=0.6714285714285714, z=0.5, id=17)
VERTEX_19 = Vertex(x=-0.6666666666666667, y=0.7785714285714286, z=0.5, id=18)
VERTEX_20 = Vertex(x=-0.33333333333333337, y=0.7785714285714286, z=0.5, id=19)
VERTEX_21 = Vertex(x=-1.0, y=1.0, z=0.5, id=20)
VERTEX_22 = Vertex(x=0.0, y=1.0, z=0.5, id=21)

J = Object(
    vertices=[
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
    ],
    faces=[
        [11, 12, 13, 21, 20, 16, 17, 18, 19, 15, 14],
        [0, 3, 4, 8, 7, 5, 9, 10, 2, 1],
        [11, 14, 3, 0],
        [11, 0, 1, 12],
        [12, 1, 2, 13],
        [13, 2, 10, 21],
        [21, 10, 9, 20],
        [20, 9, 5, 16],
        [16, 5, 6, 17],
        [17, 6, 7, 18],
        [18, 7, 8, 19],
        [19, 8, 4, 15],
        [15, 4, 3, 14],
    ],
)

# v 1.3333333333333333 1.0 -0.5
# v 1.817204301075269 1.0 -0.5
# v 2.0 1.1285714285714286 -0.5
# v 1.3333333333333333 1.2214285714285715 -0.5
# v 1.6666666666666665 1.2285714285714286 -0.5
# v 1.0 1.6714285714285713 -0.5
# v 1.3333333333333333 1.6714285714285713 -0.5
# v 1.3333333333333333 1.7785714285714285 -0.5
# v 1.6666666666666665 1.7785714285714285 -0.5
# v 1.0 2.0 -0.5
# v 2.0 2.0 -0.5
# v -0.6666666666666667 0.0 0.5
# v -0.18279569892473113 0.0 0.5
# v 0.0 0.12857142857142856 0.5
# v -0.6666666666666667 0.22142857142857142 0.5
# v -0.33333333333333337 0.22857142857142856 0.5
# v -1.0 0.6714285714285714 0.5
# v -0.6666666666666667 0.6714285714285714 0.5
# v -0.6666666666666667 0.7785714285714286 0.5
# v -0.33333333333333337 0.7785714285714286 0.5
# v -1.0 1.0 0.5
# v 0.0 1.0 0.5

# f 12 13 14 22 21 17 18 19 20 16 15
# f 1 4 5 9 8 7 6 10 11 3 2

# f 12 15 4 1
# f 12 1 2 13
# f 13 2 3 14
# f 14 3 11 22
# f 22 11 10 21
# f 21 10 6 17
# f 17 6 7 18
# f 18 7 8 19
# f 19 8 9 20
# f 20 9 5 16
# f 16 5 4 15
