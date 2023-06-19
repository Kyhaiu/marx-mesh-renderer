from models.vertex import Vertex
from utils.vectors_operations import crossProduct, dotProduct, dotVector, normalizeVector, vectorModule, vectorsDistance


@staticmethod
def calculateSrcMatrix(vrp: Vertex, focalPoint: Vertex):
    """
    This method transform the SRU to SRC

    :param vrp (Vertex): The position of the camera
    :param focalPoint (Vertex): The focal point

    :return transformationMatrix(list): The transformation matrix

    :note: The matrix it's something like this:

    make the transformation matrix

    | u1, u2, u3, -vrp.u |\n
    | v1, v2, v3, -vrp.v |\n
    | n1, n2, n3, -vrp.n |\n
    | 0,  0,  0,     1   |
    """

    # obtain the normal vector of vrp and focal point
    # n = vrp - focalPoint
    # nNormalized = n / |n|
    n = Vertex(vrp.x - focalPoint.x, vrp.y -
               focalPoint.y, vrp.z - focalPoint.z)
    nModule = vectorModule(n)
    nNormalized = normalizeVector(n, nModule)

    # define the canonical axis Y to be the up vector
    y = Vertex(0, 1, 0)

    # calculate the vector V
    # v = y - (y.n)n
    # vNormalized = v / |v|
    y1 = dotProduct(y, nNormalized)
    y1 = dotProduct(y1, nNormalized)
    v = Vertex(y.x - y1.x, y.y - y1.y, y.z - y1.z)
    vModule = vectorModule(v)
    vNormalized = normalizeVector(v, vModule)

    # calculate the vector U
    # û = nNormalized x vNormalized
    uNormalized = crossProduct(
        vNormalized, nNormalized)

    # make the transformation matrix
    # | u1, u2, u3, -vrp.u |
    # | v1, v2, v3, -vrp.v |
    # | n1, n2, n3, -vrp.n |
    # | 0,  0,  0,  1      |
    transformationMatrix = [
        [
            uNormalized.x, uNormalized.y, uNormalized.z,
            -dotVector(vrp, uNormalized)
        ],
        [
            vNormalized.x, vNormalized.y, vNormalized.z,
            -dotVector(vrp, vNormalized)
        ],
        [
            nNormalized.x, nNormalized.y, nNormalized.z,
            -dotVector(vrp, nNormalized)],
        [
            0, 0, 0, 1
        ]
    ]

    return transformationMatrix


@staticmethod
def calculateProjectionMatrix(vrp: Vertex, p: Vertex, d: float, perspective: str = 'parallel') -> list:
    """
    This method calculate the projection matrix

    :param perspective ('parallel' | 'perspective'): The perspective of the projection
    :param vrp (Vertex): The position of the camera
    :param p (Vertex): The focal point
    :param d (float): The distance between the camera and the focal point

    :return matrixP(list): The projection matrix

    :note: The matrix it's something like this:  

    | 1, 0, 0, 0 |\n
    | 0, 1, 0, 0 |\n
    | 0, 0, 0, 0 |\n
    | 0, 0, 0, 1 |
    """
    if perspective == 'parallel':

        projectionPlan = Vertex(
            vrp.x + (p.x - vrp.x) * (d / (vrp.z - p.z)),
            vrp.y + (p.y - vrp.y) * (d / (vrp.z - p.z)),
            vrp.z + (p.z - vrp.z) * (d / (vrp.z - p.z))
        )

        # Distance between the projection plan and the vrp
        dp = vectorsDistance(projectionPlan, vrp)

        # Distance between the projection plan and the p
        zvp = -dp

        # Zprp (Z coordinate of the point where the projection lines intersect the projection plane)
        # In this casa, the Zprp is 0. Because this point coincides with the origin of the SRC (0, 0, 0)
        zprp = 0

        matrixP = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -zvp/dp, zprp*(zvp/d)],
            [0, 0, -1/d, 0],
        ]
        return matrixP
    elif perspective == 'perspective':
        """ 
        If it's axonometric, then the projection matrix is:
          | 1 0 0 0 |
          | 0 1 0 0 |
          | 0 0 0 0 |
          | 0 0 0 1 |
        """
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ]


@staticmethod
def calculateMjpMatrix(x: list[float, float], y: list[float, float], u: list[float, float], v: list[float, float]):
    """
    This method transform the SRC to SRT

    :param x (list[float, float]): The x coordinates of the SRC
    :param y (list[float, float]): The y coordinates of the SRC
    :param u (list[float, float]): The u coordinates of the SRT
    :param v (list[float, float]): The v coordinates of the SRT


    :return: transformationMatrix(list): The transformation matrix

    :note: The matrix it's something like this:

    | (u2 - u1)/(x2 - x1), 0, 0, -x1 * ((u2 - u1)/(x2 - x1)) + u1 |\n
    | 0, (v2 - v1)/(y2 - y1), 0, -y1 * ((v2 - v1)/(y2 - y1)) + v1 |\n
    | 0, 0, 1, 0 |\n
    | 0, 0, 0, 1 |
    """

    """
      Maybe it'll be necessary to reflect the SRC in the Y axis,
      but only if the viewport has the origin in the top left corner
    """

    return [
        [
            (u[1] - u[0])/(x[1] - x[0]),
            0,
            0,
            -x[0] * ((u[1] - u[0])/(x[1] - x[0])) + u[0]
        ],
        [
            0,
            (v[0] - v[1])/(y[1] - y[0]),
            0,
            -y[0] * ((v[1] - v[0])/(y[1] - y[0])) + v[1]
        ],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]


@staticmethod
def normalize_by_homogeneous_coordinate(vertex: Vertex) -> None:
    """
    This method normalize the matrix by the homogeneous coordinate

    :param vertex: The vertex to be normalized

    :return: None (The vertex is normalized in place)
    """
    vertex.x_screen /= vertex.h_screen
    vertex.y_screen /= vertex.h_screen
    # vertex.z /= vertex.h
    vertex.h_screen /= vertex.h_screen
