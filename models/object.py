import math
from models.face import Face
from models.halfedge import HalfEdge
from models.vertex import Vertex
from utils.vectors_operations import matrixMultiplication


class Object:

    def __init__(self, vertices: list[Vertex], faces: list[list[int]], half_edges: list[HalfEdge] = None):
        """
        Creates an object from a list of vertices and faces

        :param vertices: list of vertices
        :param faces: list containing the indexes of the vertices that form a face
        """

        if vertices is not None and faces is not None and half_edges is not None:
            self.vertexes_object = vertices
            self.half_edges = half_edges
            self.face_objects = faces
        else:
            self.vertexes_object, self.half_edges, self.face_objects = self.create_mesh(
                vertices, faces)

        self.geometric_center: Vertex = None

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
                            vertex_coords.z, id=vertex_coords.id if vertex_coords.id is not None else 'v' +
                            str(i))
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

    def define_geometric_center(self, view_name: str) -> None:
        """
        Defines the geometric center of object (in screen coordinates)

        :return: None
        """
        sum_x = 0
        sum_y = 0
        sum_z = 0

        if view_name == 'top':
            for vertices in self.vertexes_object:
                sum_x += vertices.x_top
                sum_y += vertices.y_top
                sum_z += vertices.z_top
        elif view_name == 'side':
            for vertices in self.vertexes_object:
                sum_x += vertices.x_side
                sum_y += vertices.y_side
                sum_z += vertices.z_side
        else:
            for vertices in self.vertexes_object:
                sum_x += vertices.x_front
                sum_y += vertices.y_front
                sum_z += vertices.z_front

        n = len(self.vertexes_object)
        self.geometric_center = Vertex(sum_x/n, sum_y/n, sum_z/n)

    def _rotate(self, angle_1: float, angle_2: float, axis_1: str, axis_2: str) -> None:
        """
        Rotates the object itself

        :param angle: rotation angle
        :param axis: rotation axis
        """
        if axis_1 == 'x':
            matrix = [
                [1, 0, 0, 0],
                [0, math.cos(angle_1), -math.sin(angle_1), 0],
                [0, math.sin(angle_1), math.cos(angle_1), 0],
                [0, 0, 0, 1]
            ]
        elif axis_1 == 'y':
            matrix = [
                [math.cos(angle_1), 0, math.sin(angle_1), 0],
                [0, 1, 0, 0],
                [-math.sin(angle_1), 0, math.cos(angle_1), 0],
                [0, 0, 0, 1]
            ]
        elif axis_1 == 'z':
            matrix = [
                [math.cos(angle_1), -math.sin(angle_1), 0, 0],
                [math.sin(angle_1), math.cos(angle_1), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]

        if axis_2 == 'x':
            matrix_2 = [
                [1, 0, 0, 0],
                [0, math.cos(angle_2), -math.sin(angle_2), 0],
                [0, math.sin(angle_2), math.cos(angle_2), 0],
                [0, 0, 0, 1]
            ]
        elif axis_2 == 'y':
            matrix_2 = [
                [math.cos(angle_2), 0, math.sin(angle_2), 0],
                [0, 1, 0, 0],
                [-math.sin(angle_2), 0, math.cos(angle_2), 0],
                [0, 0, 0, 1]
            ]
        elif axis_2 == 'z':
            matrix_2 = [
                [math.cos(angle_2), -math.sin(angle_2), 0, 0],
                [math.sin(angle_2), math.cos(angle_2), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]

        matrix = matrixMultiplication(matrix, matrix_2)

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

    def create_half_edges(self, vertices, faces):
        # Criar uma lista de half-edges
        half_edges = [HalfEdge(i) for i in range(len(faces) * len(faces[0]))]

        # Criar uma lista de vértices
        vertices_list = [Vertex(i, *vertex_coords)
                         for i, vertex_coords in enumerate(vertices)]

        # Lista para armazenar as faces
        processed_faces = []

        # Preencher os dados de half-edge
        for i, face_vertices in enumerate(faces):
            num_vertices = len(face_vertices)

            processed_face = []
            for j in range(num_vertices):
                v1 = face_vertices[j]
                v2 = face_vertices[(j + 1) % num_vertices]

                # Encontrar a próxima meia-aresta e vértice correspondente
                next_half_edge = half_edges[i *
                                            num_vertices + (j + 1) % num_vertices]
                next_vertex = vertices_list[v2]

                # Configurar a meia-aresta atual
                half_edges[i * num_vertices + j].origin = vertices_list[v1]
                half_edges[i * num_vertices + j].face = i
                half_edges[i * num_vertices + j].next = next_half_edge
                half_edges[i * num_vertices + j].prev = half_edges[i *
                                                                   num_vertices + (j - 1) % num_vertices]

                # Configurar a referência do vértice para uma das meia-arestas associadas
                vertices_list[v1].edge = half_edges[i * num_vertices + j]

                # Procurar pela meia-aresta gêmea
                twin_found = False
                for k in range(len(half_edges)):
                    if half_edges[k].origin == next_vertex and half_edges[k].next.origin == vertices_list[v1]:
                        half_edges[i * num_vertices + j].twin = half_edges[k]
                        half_edges[k].twin = half_edges[i * num_vertices + j]
                        twin_found = True
                        break

                # Se não encontrar a meia-aresta gêmea, criá-la
                if not twin_found:
                    twin_half_edge = HalfEdge(len(half_edges))
                    twin_half_edge.origin = next_vertex
                    twin_half_edge.twin = half_edges[i * num_vertices + j]
                    half_edges[i * num_vertices + j].twin = twin_half_edge
                    half_edges.append(twin_half_edge)

                processed_face.append(half_edges[i * num_vertices + j])

            processed_faces.append(processed_face)

        return vertices_list, half_edges, processed_faces
