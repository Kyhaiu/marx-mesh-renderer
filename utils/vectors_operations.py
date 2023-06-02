import math

import numpy as np
from models.vertex import Vertex


@staticmethod
def vectorModule(vertex: Vertex):
    return math.sqrt(math.pow(vertex.x, 2) + math.pow(vertex.y, 2) + math.pow(vertex.z, 2))


@staticmethod
def dotProduct(vertex1: Vertex, vertex2: Vertex | float) -> Vertex | float:
    """
      This method calculate the dot product between two vectors
      ---

      Parameters:
        vertex1 (Vertex): The first vector
        vertex2 (Vertex | float): The second vector/scalar

      Returns:
        Vertex | float: The result of the dot product.

        If the second parameter is a vector, the result is a scalar
        otherwise, the result is a vector, because the dot product
        between a vector and a scalar is a vector
    """
    if isinstance(vertex2, float) or isinstance(vertex2, int):
        return Vertex(vertex1.x * vertex2, vertex1.y * vertex2, vertex1.z * vertex2)
    elif isinstance(vertex1, float) or isinstance(vertex1, int):
        return Vertex(vertex1 * vertex2.x, vertex1 * vertex2.y, vertex1 * vertex2.z)
    else:
        return vertex1.x * vertex2.x + vertex1.y * vertex2.y + vertex1.z * vertex2.z


@staticmethod
def dotVector(vertex1: Vertex, vertex2: Vertex):
    return vertex1.x * vertex2.x + vertex1.y * vertex2.y + vertex1.z * vertex2.z


@staticmethod
def normalizeVector(vertex: Vertex, module: float):
    return Vertex(vertex.x/module, vertex.y/module, vertex.z/module)


@staticmethod
def matrixMultiplication(matrix1: list, matrix2: list):
    return np.matmul(matrix1, matrix2)


@staticmethod
def normalVector(vertex1: Vertex, vertex2: Vertex):
    return Vertex(vertex2.x - vertex1.x, vertex2.y - vertex1.y, vertex2.z - vertex1.z)


@staticmethod
def crossProduct(vertex1: Vertex, vertex2: Vertex):
    return Vertex(
        vertex1.y * vertex2.z - vertex1.z * vertex2.y,
        vertex1.z * vertex2.x - vertex1.x * vertex2.z,
        vertex1.x * vertex2.y - vertex1.y * vertex2.x
    )


@staticmethod
def vectorsDistance(vertex1: Vertex, vertex2: Vertex):
    return math.sqrt(math.pow(vertex2.x - vertex1.x, 2) + math.pow(vertex2.y - vertex1.y, 2) + math.pow(vertex2.z - vertex1.z, 2))
