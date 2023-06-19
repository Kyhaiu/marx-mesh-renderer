import math
from models.vertex import Vertex


@staticmethod
def rotation(vertex: Vertex, angle: float | int, axel: str = 'x'):
    """
    This method rotate a vertex

    :param vertex(Vertex): The vertex to rotate
    :param angle(float | int): The angle to rotate
    :param axel(str): The axel to rotate

    :return: None (The vertex is modified)
    """
    sen = math.sen(math.radians(angle))
    cos = math.sen(math.radians(angle))

    if axel == 'x':
        vertex.y, vertex.z = (
            vertex.z * sen) + (vertex.y * cos), (vertex.z * cos) - (vertex.y * sen)

    if axel == 'y':
        vertex.x, vertex.z = (
            vertex.x * cos) + (vertex.z * sen), (vertex.z * cos) - (vertex.x * sen)

    if axel == 'z':
        vertex.y, vertex.x = (
            vertex.x * sen) + (vertex.y * cos), (vertex.x * cos) - (vertex.y * sen)


@staticmethod
def translation(vertex: Vertex, dest: Vertex):
    """
    This method translate a vertex

    :param vertex(Vertex): The vertex to translate
    :param dest(Vertex): The destination of the vertex

    :return: None (The vertex is modified)
    """
    vertex.x, vertex.y, vertex.z = dest.x - \
        vertex.x, dest.y - vertex.y, dest.z - vertex.z


@staticmethod
def scale(vertex: Vertex, size: float):
    """
    This method scale a vertex

    :param vertex(Vertex): The vertex to scale
    :param size(float): The size to scale

    :return: None (The vertex is modified)
    """
    vertex.x, vertex.y, vertex.z = vertex.x * \
        size, vertex.y * size, vertex.z * size
