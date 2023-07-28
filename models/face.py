from models.halfedge import HalfEdge
from models.vertex import Vertex
from utils.vectors_operations import crossProduct, dotProduct, normalizeVector, vectorModule


class Face:

    def __init__(self, half_edge: 'HalfEdge' = None, visible: bool = True, id: str | int = None):
        self.half_edge = half_edge
        self.edges = None
        self.visible = visible
        self.id = id
        self.centroid = None
        self.normal = None

    def __repr__(self) -> str:
        repr = "Face(\n"
        repr += "\tid: {}\n".format(self. id if self.id else '')
        repr += "\thalf_edge: {}\n".format(
            self.half_edge.id if self.half_edge else '')
        if self.vertices is not None:
            repr += "\tvertices: (\n"
            for row in self.vertices:
                repr += "\t\tv "
                repr += "{} {} {}\n".format(row.x if row.x else '',
                                            row.y if row.y else '', row.z if row.z else '')
            repr += "\t)\n"
        repr += "\tvisible: {}\n".format(self.visible)
        repr += ")\n"
        return repr

    @property
    def half_edge(self) -> 'HalfEdge':
        return self.__half_edge

    @half_edge.setter
    def half_edge(self, half_edge: 'HalfEdge'):
        if type(half_edge).__name__ == "HalfEdge" or half_edge is None:
            self.__half_edge = half_edge
            if half_edge is not None:
                # when half_edge is different from None, we can get the vertices
                self.edges = self.get_vertices()
        else:
            raise TypeError(
                "half_edge must be a HalfEdge or None, but is {}".format(type(half_edge)))

    @property
    def edges(self) -> list['HalfEdge']:
        return self.__edges

    @edges.setter
    def edges(self, edges: list['HalfEdge']):
        if (type(edges).__name__ == "list" and len(edges) >= 3) or edges is None:
            self.__edges = edges

            # Calculate the centroid of the face
            # using the follow formula:
            # (x1 + x2 + x3 + ... + xn) / n
            if edges is not None:
                x = 0
                y = 0
                z = 0
                for vertex in edges:
                    x += vertex.origin.x
                    y += vertex.origin.y
                    z += vertex.origin.z
                self.centroid = Vertex(x / len(edges),
                                       y / len(edges),
                                       z / len(edges))
        else:
            if len(edges) < 3:
                raise ValueError(
                    "face must have at least 3 vertex to be a face, but has {}".format(len(edges)))
            else:
                raise TypeError(
                    "vertices must be a list, but is {}".format(type(edges)))

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        if type(visible) is bool:
            self.__visible = visible
        else:
            raise TypeError(
                "visible must be a bool, but is {}".format(type(visible)))

    @property
    def id(self) -> str | int:
        return self.__id

    @id.setter
    def id(self, id: str | int):
        if type(id) is str or type(id) is int or id is None:
            self.__id = id
        else:
            raise TypeError(
                "id must be a str, int or None, but is {}".format(type(id)))

    @property
    def centroid(self) -> Vertex:
        return self.__centroid

    @centroid.setter
    def centroid(self, centroid: Vertex):
        if type(centroid).__name__ == "Vertex" or centroid is None:
            self.__centroid = centroid
        else:
            raise TypeError(
                "centroid must be a Vertex or None, but is {}".format(type(centroid)))

    @property
    def normal(self) -> Vertex:
        return self.__normal

    @normal.setter
    def normal(self, normal: Vertex):
        if type(normal).__name__ == "Vertex" or normal is None or type(normal) is float or type(normal) is int:
            self.__normal = normal
        else:
            raise TypeError(
                "normal must be a Vertex or None, but is {}".format(type(normal)))

    def get_vertices(self) -> list['HalfEdge']:
        vertices = []
        half_edge = self.half_edge
        while True:
            vertices.append(half_edge)
            half_edge = half_edge.next
            if half_edge == self.half_edge:
                break
        return vertices

    def is_counter_clockwise(self, origin: Vertex, prev: Vertex, next: Vertex) -> bool:
        """
        Checks if the vectors used to get the normal of face are in counter clockwise order.

        :return: True if the face is counter clockwise, False otherwise.
        """
        return 0.5 * ((next.x - origin.x) * (next.y - origin.y) -
                      (prev.x - origin.x) * (prev.y - origin.y)) > 0

    def get_normal(self) -> Vertex:
        """
        Calculates the normal vector of the face.
        """

        # Get the vertices of the face
        face_vertexes = self.get_vertices()
        # v1 = face_vertexes[0].origin
        # v2 = face_vertexes[0].next.origin
        # v3 = face_vertexes[0].prev.origin

        # walk through the half edges of the face until get a counter clockwise order
        for i in range(len(face_vertexes)):
            v1 = face_vertexes[i].origin
            v2 = face_vertexes[i].next.origin
            v3 = face_vertexes[i].prev.origin
            if self.is_counter_clockwise(v1, v2, v3):
                break

        print('--' * 10)
        print('v1 Half edge: ', v1.half_edge.id)
        print('v2 Half edge: ', v2.half_edge.id)
        print('v3 Half edge: ', v3.half_edge.id)
        print('Face: ', self.id)
        print('Vertices: ')
        for v in self.edges:
            print(v.origin)

        print('Vectors face:')
        print(v1, v2, v3)
        print('--' * 10)

        # Get the vectors of the face
        # A
        v1v2 = Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z)
        # B
        v1v3 = Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z)

        # Calculate the cross product of the vectors
        # |A x B|
        normal = crossProduct(v1v3, v1v2)

        # Get the module of the vector
        module = vectorModule(normal)

        # Normalize the vector
        normal = normalizeVector(normal, module)

        # Return the normal vector
        return normal

    def visibility_test(self, camera: 'Vertex') -> bool:
        """
        Checks if the face is visible to the camera.

        :param camera: The camera.

        :return: True if the face is visible to the camera, False otherwise.
        """

        # Get the normal vector of the face
        normal = self.get_normal()
        # Get the vector from the camera to the face
        camera_to_face = Vertex(self.edges[0].origin.x - camera.x, self.edges[0].origin.y - camera.y,
                                self.edges[0].origin.z - camera.z)

        # Get the module of the vector
        camera_to_face_module = vectorModule(camera_to_face)
        # Normalize the vector
        camera_to_face = normalizeVector(camera_to_face, camera_to_face_module)

        # Check if the dot product between the normal vector and the vector from the camera to the face is positive
        # If it is, the face is visible to the camera

        # idk why the test is inverted, but it works \_(o.o)_/
        # and yeah the letters ara in the correct order (anti-clockwise)
        self.visible = dotProduct(normal, camera_to_face) > 0

        self.normal = dotProduct(normal, camera_to_face)
