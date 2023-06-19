import math

import numpy as np
from models.vertex import Vertex


@staticmethod
def vectorModule(vertex: Vertex) -> float | int:
    """
    This method calculate the module of a vector

    :param vertex: The vector

    :return: The module of the vector
    """
    return math.sqrt(math.pow(vertex.x, 2) + math.pow(vertex.y, 2) + math.pow(vertex.z, 2))


@staticmethod
def dotProduct(vertex1: Vertex, vertex2: Vertex | float | int) -> Vertex | float | int:
    """
    This method calculate the dot product between two vectors

    :param vertex1: The first vector
    :param vertex2: The second vector or a scalar

    :return: The result of the dot product

    :note: If one of the vectors is a scalar, the result will be a vector
    """
    if isinstance(vertex2, float) or isinstance(vertex2, int):
        return Vertex(vertex1.x * vertex2, vertex1.y * vertex2, vertex1.z * vertex2)
    elif isinstance(vertex1, float) or isinstance(vertex1, int):
        return Vertex(vertex1 * vertex2.x, vertex1 * vertex2.y, vertex1 * vertex2.z)
    else:
        return vertex1.x * vertex2.x + vertex1.y * vertex2.y + vertex1.z * vertex2.z


@staticmethod
def dotVector(vertex1: Vertex, vertex2: Vertex) -> float | int:
    """
    This method calculate the dot product between two vectors

    :param vertex1: The first vector
    :param vertex2: The second vector

    :return: The result of the dot product
    """
    return vertex1.x * vertex2.x + vertex1.y * vertex2.y + vertex1.z * vertex2.z


@staticmethod
def normalizeVector(vertex: Vertex, module: float):
    return Vertex(vertex.x/module, vertex.y/module, vertex.z/module)


@staticmethod
def matrixMultiplication(matrix1: list, matrix2: list) -> list:
    """
    This method multiply two matrix

    :param matrix1(list): The first matrix
    :param matrix2(list): The second matrix

    :return: The result of the multiplication
    """
    if type(matrix1) is None:
        raise TypeError("matrix1 must be a list, but is NoneType")
    elif type(matrix2) is None:
        raise TypeError("matrix2 must be a list, but is NoneType")

    return np.matmul(matrix1, matrix2).tolist()


@staticmethod
def normalVector(vertex1: Vertex, vertex2: Vertex) -> Vertex:
    """
    This method calculate the normal vector of two vectors

    :param vertex1: The first vector
    :param vertex2: The second vector

    :return: The normal vector
    """
    return Vertex(vertex2.x - vertex1.x, vertex2.y - vertex1.y, vertex2.z - vertex1.z)


@staticmethod
def crossProduct(vertex1: Vertex, vertex2: Vertex) -> Vertex:
    """
    This method calculate the cross product between two vectors

    :param vertex1: The first vector
    :param vertex2: The second vector

    :return: The result of the cross product
    """
    return Vertex(
        vertex1.y * vertex2.z - vertex1.z * vertex2.y,
        vertex1.z * vertex2.x - vertex1.x * vertex2.z,
        vertex1.x * vertex2.y - vertex1.y * vertex2.x
    )


@staticmethod
def vectorsDistance(vertex1: Vertex, vertex2: Vertex) -> float | int:
    """
    This method calculate the distance between two vectors

    :param vertex1: The first vector
    :param vertex2: The second vector

    :return: The distance between the two vectors
    """
    return math.sqrt(math.pow(vertex2.x - vertex1.x, 2) + math.pow(vertex2.y - vertex1.y, 2) + math.pow(vertex2.z - vertex1.z, 2))
