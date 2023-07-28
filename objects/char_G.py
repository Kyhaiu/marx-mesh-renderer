from models.vertex import Vertex
from models.object import Object

# The model of G
VERTEX_1 = Vertex(x=0.0, y=0.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.0, y=0.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=1.0, y=0.22142857142857142, z=-0.5, id=2)
VERTEX_4 = Vertex(x=0.3333333333333333, y=0.22857142857142856, z=-0.5, id=3)
VERTEX_5 = Vertex(x=0.3333333333333333, y=0.45, z=-0.5, id=4)
VERTEX_6 = Vertex(x=0.8064516129032258, y=0.45, z=-0.5, id=5)
VERTEX_7 = Vertex(x=1.0, y=0.5714285714285714, z=-0.5, id=6)
VERTEX_8 = Vertex(x=0.3333333333333333, y=0.6714285714285714, z=-0.5, id=7)
VERTEX_9 = Vertex(x=0.6666666666666666, y=0.6714285714285714, z=-0.5, id=8)
VERTEX_10 = Vertex(x=0.3333333333333333, y=0.7785714285714286, z=-0.5, id=9)
VERTEX_11 = Vertex(x=0.6559139784946236, y=0.7785714285714286, z=-0.5, id=10)
VERTEX_12 = Vertex(x=0.0, y=1.0, z=-0.5, id=11)
VERTEX_13 = Vertex(x=1.0, y=1.0, z=-0.5, id=12)
VERTEX_14 = Vertex(x=0.0, y=0.0, z=0.5, id=13)
VERTEX_15 = Vertex(x=1.0, y=0.0, z=0.5, id=14)
VERTEX_16 = Vertex(x=1.0, y=0.22142857142857142, z=0.5, id=15)
VERTEX_17 = Vertex(x=0.3333333333333333, y=0.22857142857142856, z=0.5, id=16)
VERTEX_18 = Vertex(x=0.3333333333333333, y=0.45, z=0.5, id=17)
VERTEX_19 = Vertex(x=0.8064516129032258, y=0.45, z=0.5, id=18)
VERTEX_20 = Vertex(x=1.0, y=0.5714285714285714, z=0.5, id=19)
VERTEX_21 = Vertex(x=0.3333333333333333, y=0.6714285714285714, z=0.5, id=20)
VERTEX_22 = Vertex(x=0.6666666666666666, y=0.6714285714285714, z=0.5, id=21)
VERTEX_23 = Vertex(x=0.3333333333333333, y=0.7785714285714286, z=0.5, id=22)
VERTEX_24 = Vertex(x=0.6559139784946236, y=0.7785714285714286, z=0.5, id=23)
VERTEX_25 = Vertex(x=0.0, y=1.0, z=0.5, id=24)
VERTEX_26 = Vertex(x=1.0, y=1.0, z=0.5, id=25)


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
    VERTEX_25,
    VERTEX_26,
]

faces = [[13, 14, 15, 16, 17, 18, 19, 25, 24], [0, 11, 12, 6, 5, 4, 3, 2, 1], [13, 0, 1, 14], [14, 1, 2, 15], [15, 2, 3, 16], [16, 3, 4, 17], [17, 4, 5, 18], [
    18, 5, 6, 19], [19, 6, 12, 25], [25, 12, 11, 24], [24, 11, 0, 13], [20, 21, 23, 22], [7, 9, 10, 8], [22, 9, 7, 20], [20, 7, 8, 21], [21, 8, 10, 23], [23, 10, 9, 22]]

# v 1.0 1.0 -0.5
# v 2.0 1.0 -0.5
# v 2.0 1.2214285714285715 -0.5
# v 1.3333333333333333 1.2285714285714286 -0.5
# v 1.3333333333333333 1.45 -0.5
# v 1.8064516129032258 1.45 -0.5
# v 2.0 1.5714285714285714 -0.5
# v 1.3333333333333333 1.6714285714285713 -0.5
# v 1.6666666666666665 1.6714285714285713 -0.5
# v 1.3333333333333333 1.7785714285714285 -0.5
# v 1.6559139784946235 1.7785714285714285 -0.5
# v 1.0 2.0 -0.5
# v 2.0 2.0 -0.5
# v -1.0 0.0 0.5
# v 0.0 0.0 0.5
# v 0.0 0.22142857142857142 0.5
# v -0.6666666666666667 0.22857142857142856 0.5
# v -0.6666666666666667 0.45 0.5
# v -0.19354838709677424 0.45 0.5
# v 0.0 0.5714285714285714 0.5
# v -0.6666666666666667 0.6714285714285714 0.5
# v -0.33333333333333337 0.6714285714285714 0.5
# v -0.6666666666666667 0.7785714285714286 0.5
# v -0.34408602150537637 0.7785714285714286 0.5
# v -1.0 1.0 0.5
# v 0.0 1.0 0.5


# f 14 15 16 17 18 19 20 26 25
# f 1 12 13 7 6 5 4 3 2
# f 14 1 2 15
# f 15 2 3 16
# f 16 3 4 17
# f 17 4 5 18
# f 18 5 6 19
# f 19 6 7 20
# f 20 7 13 26
# f 26 13 12 25
# f 25 12 1 14

# f 21 22 24 23 hole
# f 8 10 11 9 hole

# f 23 10 8 21
# f 21 8 9 22
# f 22 9 11 24
# f 24 11 10 23
