from models.vertex import Vertex
from models.object import Object

# Create vertices
VERT_A = Vertex(30, 2, 25)
VERT_B = Vertex(35, 4, 20)
VERT_C = Vertex(25, 3, 18)
VERT_D = Vertex(20, 1, 23)
VERT_E = Vertex(30, 10, 22.5)

pyramid = Object([VERT_A, VERT_B, VERT_C, VERT_D, VERT_E], [
    [0, 1, 4],
    [1, 2, 4],
    [2, 3, 4],
    [3, 0, 4],
    [0, 3, 2, 1]
])


# from models.face import Face
# from models.halfedge import HalfEdge
# from models.vertex import Vertex

# # Create vertices
# VERT_A = Vertex(30, 2, 25)
# VERT_B = Vertex(35, 4, 20)
# VERT_C = Vertex(25, 3, 18)
# VERT_D = Vertex(20, 1, 23)
# VERT_E = Vertex(30, 10, 22.5)

# # Create half-edges
# HE0 = HalfEdge()
# HE1 = HalfEdge()
# HE2 = HalfEdge()
# HE3 = HalfEdge()
# HE4 = HalfEdge()
# HE5 = HalfEdge()
# HE6 = HalfEdge()
# HE7 = HalfEdge()
# HE8 = HalfEdge()
# HE9 = HalfEdge()
# HE10 = HalfEdge()
# HE11 = HalfEdge()
# HE12 = HalfEdge()
# HE13 = HalfEdge()
# HE14 = HalfEdge()
# HE15 = HalfEdge()

# # Create FACEs
# FACE0 = Face()
# FACE1 = Face()
# FACE2 = Face()
# FACE3 = Face()
# FACE4 = Face()

# # Set face references
# FACE0.half_edge = HE0
# FACE1.half_edge = HE3
# FACE2.half_edge = HE6
# FACE3.half_edge = HE9
# FACE4.half_edge = HE12

# # Set origin references
# HE0.origin = VERT_E
# HE1.origin = VERT_A
# HE2.origin = VERT_B
# HE3.origin = VERT_E
# HE4.origin = VERT_B
# HE5.origin = VERT_C
# HE6.origin = VERT_E
# HE7.origin = VERT_C
# HE8.origin = VERT_D
# HE9.origin = VERT_E
# HE10.origin = VERT_D
# HE11.origin = VERT_A
# HE12.origin = VERT_A
# HE13.origin = VERT_D
# HE14.origin = VERT_C
# HE15.origin = VERT_B

# # Set FACE references
# HE0.face = FACE0
# HE1.face = FACE0
# HE2.face = FACE0
# HE3.face = FACE1
# HE4.face = FACE1
# HE5.face = FACE1
# HE6.face = FACE2
# HE7.face = FACE2
# HE8.face = FACE2
# HE9.face = FACE3
# HE10.face = FACE3
# HE11.face = FACE3
# HE12.face = FACE4
# HE13.face = FACE4
# HE14.face = FACE4
# HE15.face = FACE4

# # Set twin references
# HE0.twin = HE11
# HE1.twin = HE15
# HE2.twin = HE3
# HE3.twin = HE2
# HE4.twin = HE14
# HE5.twin = HE6
# HE6.twin = HE5
# HE7.twin = HE13
# HE8.twin = HE9
# HE9.twin = HE8
# HE10.twin = HE12
# HE11.twin = HE0
# HE12.twin = HE10
# HE13.twin = HE7
# HE14.twin = HE4
# HE15.twin = HE1

# # Set next references
# HE0.next = HE1
# HE1.next = HE2
# HE2.next = HE0
# HE3.next = HE4
# HE4.next = HE5
# HE5.next = HE3
# HE6.next = HE7
# HE7.next = HE8
# HE8.next = HE6
# HE9.next = HE10
# HE10.next = HE11
# HE11.next = HE9
# HE12.next = HE13
# HE13.next = HE14
# HE14.next = HE15
# HE15.next = HE12

# # set previous references
# HE0.prev = HE2
# HE1.prev = HE0
# HE2.prev = HE1
# HE3.prev = HE5
# HE4.prev = HE3
# HE5.prev = HE4
# HE6.prev = HE8
# HE7.prev = HE6
# HE8.prev = HE7
# HE9.prev = HE11
# HE10.prev = HE9
# HE11.prev = HE10
# HE12.prev = HE15
# HE13.prev = HE12
# HE14.prev = HE13
# HE15.prev = HE14

# # Set vertex references
# VERT_A.half_edge = HE1
# VERT_B.half_edge = HE2
# VERT_C.half_edge = HE5
# VERT_D.half_edge = HE8
# VERT_E.half_edge = HE0
