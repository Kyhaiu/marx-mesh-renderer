import math
from models.vertex import Vertex


@staticmethod
def rotation(vertex: Vertex, angle: float, axel: str):
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

    return Vertex(vertex.x, vertex.y, vertex.z)


@staticmethod
def translation(vertex: Vertex, dest: Vertex):
    vertex.x, vertex.y, vertex.z = dest.x - \
        vertex.x, dest.y - vertex.y, dest.z - vertex.z
    return Vertex(vertex.x, vertex.y, vertex.z)


@staticmethod
def scale(vertex: Vertex, size: float):
    vertex.x, vertex.y, vertex.z = vertex.x * \
        size, vertex.y * size, vertex.z * size
    return Vertex(vertex.x, vertex.y, vertex.z)
