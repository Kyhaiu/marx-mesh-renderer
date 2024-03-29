from models.vertex import Vertex

# problema em montar a malha

# lines = [

# "f 9 10 13 14 11 12 16 15",
# "f 1 7 8 4 3 6 5 2",
# "f 15 7 1 9",
# "f 9 1 2 10",
# "f 10 2 5 13",
# "f 13 5 6 14",
# "f 14 6 3 11",
# "f 11 3 4 12",
# "f 12 4 8 16",
# "f 16 8 7 15",
# ]

# result = []

# for line in lines:
#     elements = line.split()
#     transformed_elements = [int(elem) - 1 for elem in elements if elem.isdigit()]
#     result.append(transformed_elements)

# print(result) # print result


# The model of X
VERTEX_1 = Vertex(x=0.0, y=0.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=0.3333333333333333, y=0.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=0.6666666666666666, y=0.0, z=-0.5, id=2)
VERTEX_4 = Vertex(x=1.0, y=0.0, z=-0.5, id=3)
VERTEX_5 = Vertex(x=0.5053763440860215, y=0.2733812949640288, z=-0.5, id=4)
VERTEX_6 = Vertex(x=0.3118279569892473, y=0.49640287769784175, z=-0.5, id=5)
VERTEX_7 = Vertex(x=0.6989247311827957, y=0.49640287769784175, z=-0.5, id=6)
VERTEX_8 = Vertex(x=0.5053763440860215, y=0.7266187050359713, z=-0.5, id=7)
VERTEX_9 = Vertex(x=0.0, y=1.0, z=-0.5, id=8)
VERTEX_10 = Vertex(x=0.3333333333333333, y=1.0, z=-0.5, id=9)
VERTEX_11 = Vertex(x=0.6666666666666666, y=1.0, z=-0.5, id=10)
VERTEX_12 = Vertex(x=1.0, y=1.0, z=-0.5, id=11)
VERTEX_13 = Vertex(x=0.0, y=0.0, z=0.5, id=12)
VERTEX_14 = Vertex(x=0.3333333333333333, y=0.0, z=0.5, id=13)
VERTEX_15 = Vertex(x=0.6666666666666666, y=0.0, z=0.5, id=14)
VERTEX_16 = Vertex(x=1.0, y=0.0, z=0.5, id=15)
VERTEX_17 = Vertex(x=0.5053763440860215, y=0.2733812949640288, z=0.5, id=16)
VERTEX_18 = Vertex(x=0.3118279569892473, y=0.49640287769784175, z=0.5, id=17)
VERTEX_19 = Vertex(x=0.6989247311827957, y=0.49640287769784175, z=0.5, id=18)
VERTEX_20 = Vertex(x=0.5053763440860215, y=0.7266187050359713, z=0.5, id=19)
VERTEX_21 = Vertex(x=0.0, y=1.0, z=0.5, id=20)
VERTEX_22 = Vertex(x=0.3333333333333333, y=1.0, z=0.5, id=21)
VERTEX_23 = Vertex(x=0.6666666666666666, y=1.0, z=0.5, id=22)
VERTEX_24 = Vertex(x=1.0, y=1.0, z=0.5, id=23)

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

faces = [

    [12, 13, 16, 14, 15, 18, 23, 22, 19, 21, 20, 17],
    [0, 5, 8, 9, 7, 10, 11, 6, 3, 2, 4, 1],
    [17, 5, 8, 20],
    [20, 8, 9, 21],
    [21, 9, 7, 19],
    [19, 7, 10, 22],
    [22, 10, 11, 23],
    [23, 11, 6, 18],
    [18, 6, 3, 15],
    [15, 3, 2, 14],
    [14, 2, 4, 16],
    [16, 4, 1, 13],
    [13, 1, 0, 12],
    [12, 0, 5, 17]
]


# v 0.0 0.0 -0.5
# v 0.3333333333333333 0.0 -0.5
# v 0.6666666666666666 0.0 -0.5
# v 1.0 0.0 -0.5
# v 0.5053763440860215 0.2733812949640288 -0.5
# v 0.3118279569892473 0.49640287769784175 -0.5
# v 0.6989247311827957 0.49640287769784175 -0.5
# v 0.5053763440860215 0.7266187050359713 -0.5
# v 0.0 1.0 -0.5
# v 0.3333333333333333 1.0 -0.5
# v 0.6666666666666666 1.0 -0.5
# v 1.0 1.0 -0.5
# v 0.0 0.0 0.5
# v 0.3333333333333333 0.0 0.5
# v 0.6666666666666666 0.0 0.5
# v 1.0 0.0 0.5
# v 0.5053763440860215 0.2733812949640288 0.5
# v 0.3118279569892473 0.49640287769784175 0.5
# v 0.6989247311827957 0.49640287769784175 0.5
# v 0.5053763440860215 0.7266187050359713 0.5
# v 0.0 1.0 0.5
# v 0.3333333333333333 1.0 0.5
# v 0.6666666666666666 1.0 0.5
# v 1.0 1.0 0.5

# f 13 14 17 15 16 19 24 23 20 22 21 18

# f 1 6 9 10 8 11 12 7 4 3 5 2
