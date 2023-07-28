from models.face import Face
from models.halfedge import HalfEdge
from models.object import Object
from models.vertex import Vertex

# this a cube object that is used for debugging
VERT_A = Vertex(id='A', x=-1, y=-1, z=-1)
VERT_B = Vertex(id='B', x=1, y=-1, z=-1)
VERT_C = Vertex(id='C', x=1, y=-1, z=1)
VERT_D = Vertex(id='D', x=-1, y=-1, z=1)
VERT_E = Vertex(id='E', x=-1, y=1, z=-1)
VERT_F = Vertex(id='F', x=1, y=1, z=-1)
VERT_G = Vertex(id='G', x=1, y=1, z=1)
VERT_H = Vertex(id='H', x=-1, y=1, z=1)

vertices = [
    VERT_A,  # 0
    VERT_B,  # 1
    VERT_C,  # 2
    VERT_D,  # 3
    VERT_E,  # 4
    VERT_F,  # 5
    VERT_G,  # 6
    VERT_H,  # 7
]

faces = [
    [2, 6, 7, 3],
    [0, 4, 5, 1],
    [3, 7, 4, 0],
    [0, 1, 2, 3],
    [2, 1, 5, 6],
    [6, 5, 4, 7],

    # anti-clockwise
    # [2, 3, 0, 1],  # front
    # [2, 6, 7, 3],  # bottom
    # [1, 0, 4, 5],  # top
    # [6, 2, 1, 5],  # right
    # [7, 6, 5, 4],  # back
    # [3, 7, 4, 0],  # left
    # clockwise
    # [2, 3, 7, 6],  # front - ok
    # [1, 5, 4, 0],  # back - ok
    # [3, 0, 4, 7],  # - ok
    # [2, 1, 5, 6],  # - ok
    # [6, 5, 4, 7],  # - ok
    # [3, 2, 1, 0]  # - ok
    # f 3 4 8 7
    # f 1 2 6 5
    # f 4 1 5 8
    # f 8 5 6 7
    # f 7 6 2 3
    # f 3 2 1 4
]


def make_debug():
    VERT_A = Vertex(id='A', x=-1, y=-1, z=-1)
    VERT_B = Vertex(id='B', x=1, y=-1, z=-1)
    VERT_C = Vertex(id='C', x=1, y=-1, z=1)
    VERT_D = Vertex(id='D', x=-1, y=-1, z=1)
    VERT_E = Vertex(id='E', x=-1, y=1, z=-1)
    VERT_F = Vertex(id='F', x=1, y=1, z=-1)
    VERT_G = Vertex(id='G', x=1, y=1, z=1)
    VERT_H = Vertex(id='H', x=-1, y=1, z=1)

    vertices = [
        VERT_A,  # 0
        VERT_B,  # 1
        VERT_C,  # 2
        VERT_D,  # 3
        VERT_E,  # 4
        VERT_F,  # 5
        VERT_G,  # 6
        VERT_H,  # 7
    ]

    faces = [
        [2, 6, 7, 3],
        [0, 4, 5, 1],
        [3, 7, 4, 0],
        [0, 1, 2, 3],
        [2, 1, 5, 6],
        [6, 5, 4, 7],

        # anti-clockwise
        # [2, 3, 0, 1],  # front
        # [2, 6, 7, 3],  # bottom
        # [1, 0, 4, 5],  # top
        # [6, 2, 1, 5],  # right
        # [7, 6, 5, 4],  # back
        # [3, 7, 4, 0],  # left
        # clockwise
        # [2, 3, 7, 6],  # front - ok
        # [1, 5, 4, 0],  # back - ok
        # [3, 0, 4, 7],  # - ok
        # [2, 1, 5, 6],  # - ok
        # [6, 5, 4, 7],  # - ok
        # [3, 2, 1, 0]  # - ok
        # f 3 4 8 7
        # f 1 2 6 5
        # f 4 1 5 8
        # f 8 5 6 7
        # f 7 6 2 3
        # f 3 2 1 4
    ]

    # Half-edge	|Origin	|Twin	|Incident face	|Next	|Prev
    # e0	v2	e16	f0	e1	e3
    # e1	v6	e23	f0	e2	e0
    # e2	v7	e8	f0	e3	e1
    # e3	v3	e12	f0	e0	e2
    # e4	v1	e14	f1	e5	e7
    # e5	v0	e10	f1	e6	e4
    # e6	v4	e21	f1	e7	e5
    # e7	v5	e18	f1	e4	e6
    # e8	v3	e2	f2	e9	e11
    # e9	v7	e22	f2	e10	e8
    # e10	v4	e5	f2	e11	e9
    # e11	v0	e13	f2	e8	e10
    # e12	v2	e3	f3	e13	e15
    # e13	v3	e11	f3	e14	e12
    # e14	v0	e4	f3	e15	e13
    # e15	v1	e17	f3	e12	e14
    # e16	v6	e0	f4	e17	e19
    # e17	v2	e15	f4	e18	e16
    # e18	v1	e7	f4	e19	e17
    # e19	v5	e20	f4	e16	e18
    # e20	v6	e19	f5	e21	e23
    # e21	v5	e6	f5	e22	e20
    # e22	v4	e9	f5	e23	e21
    # e23	v7	e1	f5	e20	e22

    # Vertex	|Coordinate	|Incident edge
    # v1	(-1, -1, 0)	e5
    # v2	(1, -1, 0)	e4
    # v3	(1, -1, 0)	e0
    # v4	(-1, -1, 0)	e3
    # v5	(-1, 1, 0)	e6
    # v6	(1, 1, 0)	e7
    # v7	(1, 1, 0)	e1
    # v8	(-1, 1, 0)	e2

    e0 = HalfEdge(id='e0')
    e1 = HalfEdge(id='e1')
    e2 = HalfEdge(id='e2')
    e3 = HalfEdge(id='e3')
    e4 = HalfEdge(id='e4')
    e5 = HalfEdge(id='e5')
    e6 = HalfEdge(id='e6')
    e7 = HalfEdge(id='e7')
    e8 = HalfEdge(id='e8')
    e9 = HalfEdge(id='e9')
    e10 = HalfEdge(id='e10')
    e11 = HalfEdge(id='e11')
    e12 = HalfEdge(id='e12')
    e13 = HalfEdge(id='e13')
    e14 = HalfEdge(id='e14')
    e15 = HalfEdge(id='e15')
    e16 = HalfEdge(id='e16')
    e17 = HalfEdge(id='e17')
    e18 = HalfEdge(id='e18')
    e19 = HalfEdge(id='e19')
    e20 = HalfEdge(id='e20')
    e21 = HalfEdge(id='e21')
    e22 = HalfEdge(id='e22')
    e23 = HalfEdge(id='e23')

    f0 = Face(id='f0')
    f1 = Face(id='f1')
    f2 = Face(id='f2')
    f3 = Face(id='f3')
    f4 = Face(id='f4')
    f5 = Face(id='f5')

    e0.origin = VERT_C
    e0.twin = e16
    e0.face = f0
    e0.next = e1
    e0.prev = e3

    e1.origin = VERT_G
    e1.twin = e23
    e1.face = f0
    e1.next = e2
    e1.prev = e0

    e2.origin = VERT_H
    e2.twin = e8
    e2.face = f0
    e2.next = e3
    e2.prev = e1

    e3.origin = VERT_D
    e3.twin = e12
    e3.face = f0
    e3.next = e0
    e3.prev = e2

    e4.origin = VERT_B
    e4.twin = e18
    e4.face = f1
    e4.next = e5
    e4.prev = e7

    e5.origin = VERT_A
    e5.twin = e10
    e5.face = f1
    e5.next = e6
    e5.prev = e4

    e6.origin = VERT_E
    e6.twin = e21
    e6.face = f1
    e6.next = e7
    e6.prev = e5

    e7.origin = VERT_F
    e7.twin = e5
    e7.face = f1
    e7.next = e4
    e7.prev = e6

    e8.origin = VERT_D
    e8.twin = e2
    e8.face = f2
    e8.next = e9
    e8.prev = e11

    e9.origin = VERT_H
    e9.twin = e22
    e9.face = f2
    e9.next = e10
    e9.prev = e8

    e10.origin = VERT_E
    e10.twin = e5
    e10.face = f2
    e10.next = e11
    e10.prev = e9

    e11.origin = VERT_A
    e11.twin = e9
    e11.face = f2
    e11.next = e8
    e11.prev = e10

    e12.origin = VERT_C
    e12.twin = e3
    e12.face = f3
    e12.next = e13
    e12.prev = e15

    e13.origin = VERT_D
    e13.twin = e11
    e13.face = f3
    e13.next = e14
    e13.prev = e12

    e14.origin = VERT_A
    e14.twin = e4
    e14.face = f3
    e14.next = e15
    e14.prev = e13

    e15.origin = VERT_B
    e15.twin = e13
    e15.face = f3
    e15.next = e12
    e15.prev = e14

    e16.origin = VERT_G
    e16.twin = e0
    e16.face = f4
    e16.next = e17
    e16.prev = e19

    e17.origin = VERT_C
    e17.twin = e15
    e17.face = f4
    e17.next = e18
    e17.prev = e16

    e18.origin = VERT_B
    e18.twin = e7
    e18.face = f4
    e18.next = e19
    e18.prev = e17

    e19.origin = VERT_F
    e19.twin = e16
    e19.face = f4
    e19.next = e16
    e19.prev = e18

    e20.origin = VERT_G
    e20.twin = e19
    e20.face = f5
    e20.next = e21
    e20.prev = e23

    e21.origin = VERT_F
    e21.twin = e6
    e21.face = f5
    e21.next = e22
    e21.prev = e20

    e22.origin = VERT_E
    e22.twin = e9
    e22.face = f5
    e22.next = e23
    e22.prev = e21

    e23.origin = VERT_H
    e23.twin = e20
    e23.face = f5
    e23.next = e20
    e23.prev = e22

    half_edges = [
        e0,
        e1,
        e2,
        e3,
        e4,
        e5,
        e6,
        e7,
        e8,
        e9,
        e10,
        e11,
        e12,
        e13,
        e14,
        e15,
        e16,
        e17,
        e18,
        e19,
        e20,
        e21,
        e22,
        e23,
    ]

    f0.half_edge = e0
    f1.half_edge = e4
    f2.half_edge = e8
    f3.half_edge = e12
    f4.half_edge = e16
    f5.half_edge = e20

    VERT_A.half_edge = e5
    VERT_B.half_edge = e4
    VERT_C.half_edge = e0
    VERT_D.half_edge = e3
    VERT_E.half_edge = e6
    VERT_F.half_edge = e7
    VERT_G.half_edge = e1
    VERT_H.half_edge = e2

    return Object(
        vertices=vertices,
        faces=[
            f0,
            f1,
            f2,
            f3,
            f4,
            f5,
        ],
        half_edges=half_edges,
    )

    # Bottom-left-back
    # v -1 -1 -1
    # # Bottom-right-back
    # v 1 -1 -1
    # # Bottom-right-front
    # v 1 -1  1
    # # Bottom-left-front
    # v -1 -1  1
    # # Top-left-back
    # v -1  1 -1
    # # Top-right-back
    # v 1  1 -1
    # # Top-right-front
    # v 1  1  1
    # # Top-left-front
    # v -1  1  1

    # Front Face
    # f 3 7 8 4
    # Back Face
    # f 2 1 5 6
    # Left Face
    # f 4 8 5 1
    # Bottom Face
    # f 3 4 1 2
    # Right Face
    # f 7 3 2 6
    # Top Face
    # f 7 6 5 8
