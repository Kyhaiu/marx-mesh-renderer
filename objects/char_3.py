from models.vertex import Vertex

# The model of 3
VERTEX_1 = Vertex(x=0.0, y=0.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.0, y=0.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=0.0, y=0.22142857142857142, z=-0.5, id=2)
VERTEX_4 = Vertex(x=0.6666666666666666, y=0.22142857142857142, z=-0.5, id=3)
VERTEX_5 = Vertex(x=0.0, y=0.44285714285714284, z=-0.5, id=4)
VERTEX_6 = Vertex(x=0.6666666666666666, y=0.44285714285714284, z=-0.5, id=5)
VERTEX_7 = Vertex(x=0.8064516129032258, y=0.44285714285714284, z=-0.5, id=6)
VERTEX_8 = Vertex(x=1.0, y=0.44285714285714284, z=-0.5, id=7)
VERTEX_9 = Vertex(x=1.0, y=0.5714285714285714, z=-0.5, id=8)
VERTEX_10 = Vertex(x=0.0, y=0.6642857142857143, z=-0.5, id=9)
VERTEX_11 = Vertex(x=0.6666666666666666, y=0.6642857142857143, z=-0.5, id=10)
VERTEX_12 = Vertex(x=0.6666666666666666, y=0.7714285714285715, z=-0.5, id=11)
VERTEX_13 = Vertex(x=0.0, y=0.7785714285714286, z=-0.5, id=12)
VERTEX_14 = Vertex(x=0.0, y=1.0, z=-0.5, id=13)
VERTEX_15 = Vertex(x=1.0, y=0.9928571428571429, z=-0.5, id=14)
VERTEX_16 = Vertex(x=0.0, y=0.0, z=0.5, id=15)
VERTEX_17 = Vertex(x=1.0, y=0.0, z=0.5, id=16)
VERTEX_18 = Vertex(x=0.0, y=0.22142857142857142, z=0.5, id=17)
VERTEX_19 = Vertex(x=0.6666666666666666, y=0.22142857142857142, z=0.5, id=18)
VERTEX_20 = Vertex(x=0.0, y=0.44285714285714284, z=0.5, id=19)
VERTEX_21 = Vertex(x=0.6666666666666666, y=0.44285714285714284, z=0.5, id=20)
VERTEX_22 = Vertex(x=0.8064516129032258, y=0.44285714285714284, z=0.5, id=21)
VERTEX_23 = Vertex(x=1.0, y=0.44285714285714284, z=0.5, id=22)
VERTEX_24 = Vertex(x=1.0, y=0.5714285714285714, z=0.5, id=23)
VERTEX_25 = Vertex(x=0.0, y=0.6642857142857143, z=0.5, id=24)
VERTEX_26 = Vertex(x=0.6666666666666666, y=0.6642857142857143, z=0.5, id=25)
VERTEX_27 = Vertex(x=0.6666666666666666, y=0.7714285714285715, z=0.5, id=26)
VERTEX_28 = Vertex(x=0.0, y=0.7785714285714286, z=0.5, id=27)
VERTEX_29 = Vertex(x=0.0, y=1.0, z=0.5, id=28)
VERTEX_30 = Vertex(x=1.0, y=0.9928571428571429, z=0.5, id=29)

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
    VERTEX_27,
    VERTEX_28,
    VERTEX_29,
    VERTEX_30,
]

faces = [
    [15, 16, 22, 21, 23, 29, 28, 27, 26, 25, 24, 19, 20, 18, 17],
    [0, 2, 3, 5, 4, 9, 10, 11, 12, 13, 14, 8, 6, 7, 1],
    [17, 2, 0, 15],
    [15, 0, 1, 16],
    [16, 1, 7, 22],
    [22, 7, 6, 21],
    [21, 6, 8, 23],
    [23, 8, 14, 29],
    [29, 14, 13, 28],
    [28, 13, 12, 27],
    [27, 12, 11, 26],
    [26, 11, 10, 25],
    [25, 10, 9, 24],
    [24, 9, 4, 19],
    [19, 4, 5, 20],
    [20, 5, 3, 18],
    [18, 3, 2, 17]
]

# v 1.0 1.0 -0.5
# v 2.0 1.0 -0.5
# v 1.0 1.2214285714285715 -0.5
# v 1.6666666666666665 1.2214285714285715 -0.5
# v 1.0 1.4428571428571428 -0.5
# v 1.6666666666666665 1.4428571428571428 -0.5
# v 1.8064516129032258 1.4428571428571428 -0.5
# v 2.0 1.4428571428571428 -0.5
# v 2.0 1.5714285714285714 -0.5
# v 1.0 1.6642857142857141 -0.5
# v 1.6666666666666665 1.6642857142857141 -0.5
# v 1.6666666666666665 1.7714285714285714 -0.5
# v 1.0 1.7785714285714285 -0.5
# v 1.0 2.0 -0.5
# v 2.0 1.9928571428571429 -0.5
# v -1.0 0.0 0.5
# v 0.0 0.0 0.5
# v -1.0 0.22142857142857142 0.5
# v -0.33333333333333337 0.22142857142857142 0.5
# v -1.0 0.44285714285714284 0.5
# v -0.33333333333333337 0.44285714285714284 0.5
# v -0.19354838709677424 0.44285714285714284 0.5
# v 0.0 0.44285714285714284 0.5
# v 0.0 0.5714285714285714 0.5
# v -1.0 0.6642857142857143 0.5
# v -0.33333333333333337 0.6642857142857143 0.5
# v -0.33333333333333337 0.7714285714285715 0.5
# v -1.0 0.7785714285714286 0.5
# v -1.0 1.0 0.5
# v 0.0 0.9928571428571429 0.5

# f 16 17 23 22 24 30 29 28 27 26 25 20 21 19 18
# f 1 3 4 6 5 10 11 12 13 14 15 9 7 8 2
# f 18 3 1 16
# f 16 1 2 17
# f 17 2 8 23
# f 23 8 7 22
# f 22 7 9 24
# f 24 9 15 30
# f 30 15 14 29
# f 29 14 13 28
# f 28 13 12 27
# f 27 12 11 26
# f 26 11 10 25
# f 25 10 5 20
# f 20 5 6 21
# f 21 6 4 19
# f 19 4 3 18
