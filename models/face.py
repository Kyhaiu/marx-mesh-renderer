from models.halfedge import HalfEdge
from models.vertex import Vertex
from utils.vectors_operations import crossProduct, dotProduct, normalizeVector, vectorModule


class Face:

    def __init__(self, half_edge: 'HalfEdge' = None, visible: bool = True, id: str | int = None):
        self.half_edge = half_edge
        self.vertices = None
        self.visible = visible
        self.id = id
        self.centroid = None

    def __repr__(self) -> str:
        repr = "Face(\n"
        repr += "\tid: {}\n".format(self.id)
        repr += "\thalf_edge: {}\n".format(self.half_edge.id)
        repr += "\tvertices: (\n"
        for row in self.vertices:
            repr += "\t\tv "
            repr += "{} {} {}\n".format(row.x, row.y, row.z)
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
                self.vertices = self.get_vertices()
        else:
            raise TypeError(
                "half_edge must be a HalfEdge or None, but is {}".format(type(half_edge)))

    @property
    def vertices(self) -> list['Vertex']:
        return self.__vertices

    @vertices.setter
    def vertices(self, vertices: list['Vertex']):
        if (type(vertices).__name__ == "list" and len(vertices) >= 3) or vertices is None:
            self.__vertices = vertices

            # Calculate the centroid of the face
            # using the follow formula:
            # (x1 + x2 + x3 + ... + xn) / n
            if vertices is not None:
                x = 0
                y = 0
                z = 0
                for vertex in vertices:
                    x += vertex.x
                    y += vertex.y
                    z += vertex.z
                self.centroid = Vertex(x / len(vertices),
                                       y / len(vertices),
                                       z / len(vertices))
        else:
            if len(vertices) < 3:
                raise ValueError(
                    "face must have at least 3 vertex to be a face, but has {}".format(len(vertices)))
            else:
                raise TypeError(
                    "vertices must be a list, but is {}".format(type(vertices)))

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

    def get_vertices(self) -> list['Vertex']:
        vertices = []
        half_edge = self.half_edge
        while True:
            vertices.append(half_edge.origin)
            half_edge = half_edge.next
            if half_edge == self.half_edge:
                break
        return vertices

    def get_normal(self) -> Vertex:
        """
        Calculates the normal vector of the face.
        """

        # Get the vertices of the face
        v1, v2, v3, *_ = self.vertices

        # Get the vectors of the face
        # A
        v1v2 = Vertex(v2.x - v1.x, v2.y - v1.y, v2.z - v1.z)
        # B
        v1v3 = Vertex(v3.x - v1.x, v3.y - v1.y, v3.z - v1.z)

        # Calculate the cross product of the vectors
        # |A x B|
        normal = crossProduct(v1v2, v1v3)

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
        camera_to_face = Vertex(self.centroid.x - camera.x, self.centroid.y - camera.y,
                                self.centroid.z - camera.z)

        # Get the module of the vector
        camera_to_face_module = vectorModule(camera_to_face)
        # Normalize the vector
        camera_to_face = normalizeVector(camera_to_face, camera_to_face_module)

        # Check if the dot product between the normal vector and the vector from the camera to the face is positive
        # If it is, the face is visible to the camera
        self.visible = dotProduct(normal, camera_to_face) > 0
