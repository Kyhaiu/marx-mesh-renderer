from models.vertex import Vertex

# The model of 4
VERTEX_1 = Vertex(x=0.0, y=0.0, z=-0.5, id=0)
VERTEX_2 = Vertex(x=1.0, y=0.0, z=-0.5, id=1)
VERTEX_3 = Vertex(x=0.3333333333333333, y=0.0, z=-0.5, id=2)
VERTEX_4 = Vertex(x=0.6666666666666666, y=0.0, z=-0.5, id=3)
VERTEX_5 = Vertex(x=0.3333333333333333, y=0.4460431654676259, z=-0.5, id=4)
VERTEX_6 = Vertex(x=0.6666666666666666, y=0.4460431654676259, z=-0.5, id=5)
VERTEX_7 = Vertex(x=0.0, y=0.6690647482014388, z=-0.5, id=6)
VERTEX_8 = Vertex(x=0.6666666666666666, y=0.6690647482014388, z=-0.5, id=7)
VERTEX_9 = Vertex(x=0.6666666666666666, y=1.0, z=-0.5, id=8)
VERTEX_10 = Vertex(x=1.0, y=1.0, z=-0.5, id=9)
VERTEX_11 = Vertex(x=0.0, y=0.0, z=0.5, id=10)
VERTEX_12 = Vertex(x=1.0, y=0.0, z=0.5, id=11)
VERTEX_13 = Vertex(x=0.3333333333333333, y=0.0, z=0.5, id=12)
VERTEX_14 = Vertex(x=0.6666666666666666, y=0.0, z=0.5, id=13)
VERTEX_15 = Vertex(x=0.3333333333333333, y=0.4460431654676259, z=0.5, id=14)
VERTEX_16 = Vertex(x=0.6666666666666666, y=0.4460431654676259, z=0.5, id=15)
VERTEX_17 = Vertex(x=0.0, y=0.6690647482014388, z=0.5, id=16)
VERTEX_18 = Vertex(x=0.6666666666666666, y=0.6690647482014388, z=0.5, id=17)
VERTEX_19 = Vertex(x=0.6666666666666666, y=1.0, z=0.5, id=18)
VERTEX_20 = Vertex(x=1.0, y=1.0, z=0.5, id=19)

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
]

faces = [[10, 12, 14, 15, 13, 11, 19, 18, 17, 16], [0, 6, 7, 8, 9, 1, 3, 5, 4, 2], [16, 6, 0, 10], [10, 0, 2, 12], [
    12, 2, 4, 14], [14, 4, 5, 15], [15, 5, 3, 13], [13, 3, 1, 11], [11, 1, 9, 19], [19, 9, 8, 18], [18, 8, 7, 17], [17, 7, 6, 16]]

# v 1.0 1.0 -0.5
# v 2.0 1.0 -0.5
# v 1.3333333333333333 1.0 -0.5
# v 1.6666666666666665 1.0 -0.5
# v 1.3333333333333333 1.4460431654676258 -0.5
# v 1.6666666666666665 1.4460431654676258 -0.5
# v 1.0 1.6690647482014387 -0.5
# v 1.6666666666666665 1.6690647482014387 -0.5
# v 1.6666666666666665 2.0 -0.5
# v 2.0 2.0 -0.5
# v -1.0 0.0 0.5
# v 0.0 0.0 0.5
# v -0.6666666666666667 0.0 0.5
# v -0.33333333333333337 0.0 0.5
# v -0.6666666666666667 0.4460431654676259 0.5
# v -0.33333333333333337 0.4460431654676259 0.5
# v -1.0 0.6690647482014388 0.5
# v -0.33333333333333337 0.6690647482014388 0.5
# v -0.33333333333333337 1.0 0.5
# v 0.0 1.0 0.5

# f 11 13 15 16 14 12 20 19 18 17
# f 1 7 8 9 10 2 4 6 5 3
# f 17 7 1 11
# f 11 1 3 13
# f 13 3 5 15
# f 15 5 6 16
# f 16 6 4 14
# f 14 4 2 12
# f 12 2 10 20
# f 20 10 9 19
# f 19 9 8 18
# f 18 8 7 17
