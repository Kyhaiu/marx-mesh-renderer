import logging
import math
from models.face import Face
from models.halfedge import HalfEdge
from models.vertex import Vertex
from utils.vectors_operations import matrixMultiplication


class Object:

    def __init__(self, vertices: list[Vertex], faces: list[list[int]]):
        """
        Creates an object from a list of vertices and faces

        :param vertices: list of vertices
        :param faces: list containing the indexes of the vertices that form a face
        """

        self.vertexes_object, self.half_edges, self.face_objects = self.create_mesh(
            vertices, faces)

    @property
    def vertexes_object(self) -> list[Vertex]:
        return self.__vertexes_object

    @vertexes_object.setter
    def vertexes_object(self, vertexes_object: list[Vertex]):
        if type(vertexes_object).__name__ == "list":
            self.__vertexes_object = vertexes_object
        else:
            raise TypeError(
                "vertexes_object must be a list, but is {}".format(type(vertexes_object)))

    @property
    def half_edges(self) -> list[HalfEdge]:
        return self.__half_edges

    @half_edges.setter
    def half_edges(self, half_edges: list[HalfEdge]):
        if type(half_edges).__name__ == "list":
            self.__half_edges = half_edges
        else:
            raise TypeError(
                "half_edges must be a list, but is {}".format(type(half_edges)))

    @property
    def face_objects(self) -> list[Face]:
        return self.__face_objects

    @face_objects.setter
    def face_objects(self, face_objects: list[Face]):
        if type(face_objects).__name__ == "list":
            self.__face_objects = face_objects
        else:
            raise TypeError(
                "face_objects must be a list, but is {}".format(type(face_objects)))

    def create_mesh(self, vertices: list[Vertex], faces: list[list[int]]) -> tuple[list[Vertex], list[HalfEdge], list[Face]]:
        """
        Creates a mesh from a list of vertices and faces

        :param vertices: list of vertices
        :param faces: list containing the indexes of the vertices that form a face

        :return: tuple containing the vertex objects, half-edge objects and face objects
        """

        vertex_objects = []
        face_objects = []
        half_edges = []

        # Create vertex objects
        for i, vertex_coords in enumerate(vertices):
            vertex = Vertex(vertex_coords.x, vertex_coords.y,
                            vertex_coords.z, id='v' + str(i+1))
            vertex_objects.append(vertex)

        # Create face objects
        for i in range(len(faces)):
            face = Face(id='f' + str(i))
            face_objects.append(face)

        # Create half-edge objects
        k = 0
        for i, face in enumerate(faces):
            num_vertices = len(face)
            face_half_edges = []

            for j in range(num_vertices):
                half_edge = HalfEdge(id='e' + str(k))
                half_edges.append(half_edge)
                face_half_edges.append(half_edge)
                k += 1

            # Connect half-edges within the face
            for j in range(num_vertices):
                half_edge: HalfEdge = face_half_edges[j]

                half_edge.origin = vertex_objects[face[j]]
                if half_edge.origin.half_edge is None:
                    # Associate the vertex with the half-edge
                    vertex_objects[face[j]].half_edge = half_edge

                half_edge.next = face_half_edges[(j + 1) % num_vertices]
                half_edge.prev = face_half_edges[(j - 1) % num_vertices]
                half_edge.twin = None  # To be connected later
                half_edge.face = face_objects[i]

            # Associate the first half-edge with the face
            face_objects[i].half_edge = face_half_edges[0]

        # Connect twin half-edges
        for i in range(len(half_edges)):
            half_edge = half_edges[i]

            if half_edge.twin is None:
                for j in range(i + 1, len(half_edges)):
                    twin_half_edge = half_edges[j]

                    if twin_half_edge.origin == half_edge.next.origin and \
                            twin_half_edge.next.origin == half_edge.origin:

                        half_edge.twin = twin_half_edge
                        twin_half_edge.twin = half_edge
                        break

        return vertex_objects, half_edges, face_objects

    def apply_transformation(self, matrix: list[list[float]]) -> None:
        """
        Applies a transformation matrix to the object itself

        :param matrix: transformation matrix
        # """
        for i, vertex in enumerate(self.vertexes_object):
            matrix_vertex = [[vertex.x], [vertex.y], [vertex.z], [vertex.h]]
            matrix_result = matrixMultiplication(matrix, matrix_vertex)

            vertex.x = float(matrix_result[0][0])
            vertex.y = float(matrix_result[1][0])
            vertex.z = float(matrix_result[2][0])
            vertex.h = float(matrix_result[3][0])

    def _rotate(self, angle: float, axis: str) -> None:
        """
        Rotates the object itself

        :param angle: rotation angle
        :param axis: rotation axis
        """
        if axis == 'x':
            matrix = [
                [1, 0, 0, 0],
                [0, math.cos(angle), -math.sin(angle), 0],
                [0, math.sin(angle), math.cos(angle), 0],
                [0, 0, 0, 1]
            ]
        elif axis == 'y':
            matrix = [
                [math.cos(angle), 0, math.sin(angle), 0],
                [0, 1, 0, 0],
                [-math.sin(angle), 0, math.cos(angle), 0],
                [0, 0, 0, 1]
            ]
        elif axis == 'z':
            matrix = [
                [math.cos(angle), -math.sin(angle), 0, 0],
                [math.sin(angle), math.cos(angle), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]

        self.apply_transformation(matrix)

    def _translate(self, x: float, y: float, z: float):
        """
        Translates the object itself

        :param x: translation in x
        :param y: translation in y
        :param z: translation in z
        """
        matrix = [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]

        self.apply_transformation(matrix)

    def _scale(self, x: float, y: float, z: float):
        """
        Scales the object itself

        :param x: scale in x
        :param y: scale in y
        :param z: scale in z
        """
        matrix = [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ]

        self.apply_transformation(matrix)

    def _shear(self, x: float, y: float, z: float):
        """
        Shears the object itself

        :param x: shear in x
        :param y: shear in y
        :param z: shear in z
        """
        matrix = [
            [1, x, x, 0],
            [y, 1, y, 0],
            [z, z, 1, 0],
            [0, 0, 0, 1]
        ]

        self.apply_transformation(matrix)
