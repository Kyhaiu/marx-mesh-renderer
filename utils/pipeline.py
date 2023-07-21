from models.vertex import Vertex
from utils.vectors_operations import crossProduct, dotProduct, dotVector, normalizeVector, vectorModule, vectorsDistance


@staticmethod
def calculateSrcMatrix(vrp: Vertex, focalPoint: Vertex, projectionType: str):
    """
    This method transforms the SRU to SRC

    :param vrp (Vertex): The position of the camera
    :param focalPoint (Vertex): The focal point
    :param projectionType (str): The type of projection/view

    :return transformationMatrix (list): The transformation matrix

    :note: The matrix is structured as follows:

    | u1, u2, u3, -vrp.u |
    | v1, v2, v3, -vrp.v |
    | n1, n2, n3, -vrp.n |
    | 0,  0,  0,     1   |
    """

    # Obtain the normal vector of vrp and the focal point
    n = Vertex(vrp.x - focalPoint.x, vrp.y -
               focalPoint.y, vrp.z - focalPoint.z)
    nModule = vectorModule(n)
    nNormalized = normalizeVector(n, nModule)

    if projectionType == 'perspective' or projectionType == 'frontal':
        y = Vertex(0, 1, 0)
    elif projectionType == 'top':
        y = Vertex(0, 0, -1)
    elif projectionType == 'side':
        y = Vertex(0, 1, 0)

    # Define the canonical axis Y to be the up vector

    # Calculate the vector V
    y1 = dotProduct(y, nNormalized)
    y1 = dotProduct(y1, nNormalized)
    v = Vertex(y.x - y1.x, y.y - y1.y, y.z - y1.z)
    vModule = vectorModule(v)
    vNormalized = normalizeVector(v, vModule)

    # Calculate the vector U
    uNormalized = crossProduct(vNormalized, nNormalized)

    # Make the transformation matrix
    transformationMatrix = [
        [
            uNormalized.x, uNormalized.y, uNormalized.z, -
            dotVector(vrp, uNormalized)
        ],
        [
            vNormalized.x, vNormalized.y, vNormalized.z, -
            dotVector(vrp, vNormalized)
        ],
        [
            nNormalized.x, nNormalized.y, nNormalized.z, -
            dotVector(vrp, nNormalized)
        ],
        [
            0, 0, 0, 1
        ]
    ]

    return transformationMatrix


@staticmethod
def calculateProjectionMatrix(vrp: Vertex, p: Vertex, d: float, perspective: str = 'perspective') -> list:
    """
    This method calculate the projection matrix

    :param perspective ('top' | 'frontal' | 'profile' | 'perspective'): The perspective of the projection
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
    if perspective == 'perspective':

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
    elif perspective == 'frontal' or perspective == 'side' or perspective == 'top':
        """ 
        If it's frontal or side or top, then the projection matrix is:
          | 1 0 0 0 |
          | 0 1 0 0 |
          | 0 0 1 0 |
          | 0 0 0 1 |
        """
        return [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
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

    | (u_max - u_min)/(x_max - x_min), 0, 0, -x_min * ((u_max - u_min)/(x_max - x_min)) + u_min |\n
    | 0, (v_min - v_max)/(y_max - y_min), 0, y_min * ((v_max - v_min)/(y_max - y_min)) + v_max |\n
    | 0, 0, 1, 0 |\n
    | 0, 0, 0, 1 |
    """

    """
      Maybe it'll be necessary to reflect the SRC in the Y axis,
      but only if the viewport has the origin in the top left corner
    """

    u_max = u[1]
    u_min = u[0]
    v_max = v[1]
    v_min = v[0]
    x_max = x[1]
    x_min = x[0]
    y_max = y[1]
    y_min = y[0]

    return [
        [
            (u_max - u_min)/(x_max - x_min),
            0,
            0,
            -x_min * ((u_max - u_min)/(x_max - x_min)) + u_min
        ],
        [
            0,
            (v_max - v_min)/(y_max - y_min),
            0,
            -y_min * ((v_max - v_min)/(y_max - y_min)) + v_min
        ],
        [
            0, 0, 1, 0
        ],
        [
            0, 0, 0, 1
        ]
    ]


@staticmethod
def normalize_by_homogeneous_coordinate(vertex: Vertex) -> None:
    """
    This method normalize the matrix by the homogeneous coordinate

    :param vertex: The vertex to be normalized

    :return: None (The vertex is normalized in place)
    """
    # perspective coordinates we must ignore the z coordinate
    vertex.x_screen /= vertex.h_screen
    vertex.y_screen /= vertex.h_screen
    # vertex.z_screen /= vertex.h_screen
    vertex.h_screen /= vertex.h_screen

    # frontal coordinates we must ignore the z coordinate
    vertex.x_front /= vertex.h_front
    vertex.y_front /= vertex.h_front
    # vertex.z_front /= vertex.h_front
    vertex.h_front /= vertex.h_front

    # top coordinates we must ignore the y coordinate
    vertex.x_top /= vertex.h_top
    # vertex.y_top /= vertex.h_top
    vertex.z_top /= vertex.h_top
    vertex.h_top /= vertex.h_top

    # side coordinates we must ignore the x coordinate
    # vertex.x_side /= vertex.h_side
    vertex.y_side /= vertex.h_side
    vertex.z_side /= vertex.h_side
    vertex.h_side /= vertex.h_side
