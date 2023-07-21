from typing import List
from models.vertex import Vertex
from utils import pipeline
from utils.vectors_operations import matrixMultiplication


class Camera:

    def __init__(
        self,
        vrp: Vertex = Vertex(0, 0, 10),
        p: Vertex = Vertex(0, 0, -2),
        d: float | int = 20,
        viewPort: List[float] = [0, 225, 0, 225],
        window: List[float] = [-3, 3, -3, 3],
        projectionType: str = 'perspective',
    ):
        """
          This method initialize the camera

          Parameters:
            vrp (Vertex): The position of the camera
            p (Vertex): The focal point
            d (float): The distance between the camera and the focal point
            viewPort (list): The viewport (umin, umax, vmin, vmax)
            window (list): The window  (width, height)
            projectionType (str): The projection type (parallel or perspective)
        """

        # basic properties for camera
        self.p = p
        self.d = d
        self.vrp = vrp
        self.viewPort = viewPort
        self.window = window
        self.projectionType = projectionType

        # pipeline properties

        # transformation matrix from SRU to SRC
        self.srcMatrix: list = None
        # projection matrix
        self.projectionMatrix: list = None
        # transformation matrix from SRC to STR
        self.MjpMatrix: list = None

        # transformation matrix from SRU to STR
        self.MSruSrtMatrix: list = None

        self.calculateMatrices()

    def __str__(self) -> str:
        """
          This method returns the string representation of the camera

          Returns:
            string (str): The string representation of the camera
        """
        msg = "Camera(\n"
        msg += "\tvrp: {}\n".format(self.vrp)
        msg += "\tp: {}\n".format(self.p)
        msg += "\td: {}\n".format(self.d)
        msg += "\tviewPort:\n"
        msg += "\t\tumin: {}\n".format(self.viewPort[0])
        msg += "\t\tumax: {}\n".format(self.viewPort[1])
        msg += "\t\tvmin: {}\n".format(self.viewPort[2])
        msg += "\t\tvmax: {}\n".format(self.viewPort[3])
        msg += "\twindow:\n"
        msg += "\t\twidth:\n"
        msg += "\t\t\txmin: {}\n".format(self.window[0])
        msg += "\t\t\txmax: {}\n".format(self.window[1])
        msg += "\t\theight:\n"
        msg += "\t\t\tymin: {}\n".format(self.window[2])
        msg += "\t\t\tymax: {}\n".format(self.window[3])
        msg += "\tprojectionType: {}\n".format(self.projectionType)
        msg += "\tsrcMatrix: [\n"
        for row in self.srcMatrix:
            msg += "\t\t{}\n".format(row)
        msg += "\t]\n"
        msg += "\tprojectionMatrix: [\n"
        for row in self.projectionMatrix:
            msg += "\t\t{}\n".format(row)
        msg += "\t]\n"
        msg += "\tMjpMatrix: [\n"
        for row in self.MjpMatrix:
            msg += "\t\t{}\n".format(row)
        msg += "\t]\n"
        msg += "\tMSruSrtMatrix: [\n"
        for row in self.MSruSrtMatrix:
            msg += "\t\t{}\n".format(row)
        msg += "\t]\n"
        msg += ")"
        return msg
        # return f"VRP: {self.vrp}\nFocal Point: {self.p}\nDistance: {self.d}\nViewPort: {self.viewPort}\nWindow: {self.window}"

    @property
    def vrp(self) -> Vertex:
        """
          This method returns the vrp of the camera

          Returns:
            vrp (Vertex): The vrp of the camera
        """
        return self.__vrp

    @vrp.setter
    def vrp(self, vrp: Vertex) -> None:
        """
          This method sets the vrp of the camera

          Parameters:
            vrp (Vertex): The vrp of the camera
        """
        if type(vrp).__name__ == "Vertex":
            self.__vrp = vrp
        else:
            raise TypeError(
                "vrp must be a Vertex, but is {}".format(type(vrp)))

    @property
    def p(self) -> Vertex:
        """
          This method returns the focal point of the camera

          Returns:
            p (Vertex): The focal point of the camera
        """
        return self.__p

    @p.setter
    def p(self, p: Vertex) -> None:
        """
          This method sets the focal point of the camera

          Parameters:
            p (Vertex): The focal point of the camera
        """
        if type(p).__name__ == "Vertex":
            self.__p = p
        else:
            raise TypeError(
                "p must be a Vertex, but is {}".format(type(p)))

    @property
    def d(self) -> float:
        """
          This method returns the distance between the camera and the focal point

          Returns:
            d (float): The distance between the camera and the focal point
        """
        return self.__d

    @d.setter
    def d(self, d: float | int) -> None:
        """
          This method sets the distance between the camera and the focal point

          Parameters:
            d (float): The distance between the camera and the focal point
        """
        if type(d) is float or type(d) is int:
            self.__d = d
        else:
            raise TypeError(
                "d must be a float or int, but is {}".format(type(d)))

    @property
    def viewPort(self) -> List[float]:
        """
          This method returns the viewport of the camera

          Returns:
            viewPort (list): The viewport of the camera
        """
        return self.__viewPort

    @viewPort.setter
    def viewPort(self, viewPort: List[float]) -> None:
        """
          This method sets the viewport of the camera

          Parameters:
            viewPort (list): The viewport of the camera
        """
        if type(viewPort).__name__ == "list" or None:
            self.__viewPort = viewPort
        else:
            raise TypeError(
                "viewPort must be a list, but is {}".format(type(viewPort)))

    @property
    def window(self) -> List[float]:
        """
          This method returns the window of the camera

          Returns:
            window (list): The window of the camera
        """
        return self.__window

    @window.setter
    def window(self, window: List[float]) -> None:
        """
          This method sets the window of the camera

          Parameters:
            window (list): The window of the camera
        """
        if type(window).__name__ == "list" or None:
            self.__window = window
        else:
            raise TypeError(
                "window must be a list, but is {}".format(type(window)))

    @property
    def projectionType(self) -> str:
        """
          This method returns the projection type of the camera

          Returns:
            projectionType (str): The projection type of the camera
        """
        return self.__projectionType

    @projectionType.setter
    def projectionType(self, projectionType: str) -> None:
        """
          This method sets the projection type of the camera

          Parameters:
            projectionType (str): The projection type of the camera
        """
        if type(projectionType).__name__ == "str" and (
            projectionType == "frontal" or projectionType == "top" or
            projectionType == "side" or projectionType == "perspective"
        ):
            self.__projectionType = projectionType
        else:
            raise TypeError(
                "projectionType must be a str, but is {}".format(type(projectionType)))

    @property
    def srcMatrix(self) -> list | None:
        """
          This method returns the transformation matrix from SRU to SRC

          Returns:
            srcMatrix (list): The transformation matrix from SRU to SRC
        """
        return self.__srcMatrix

    @srcMatrix.setter
    def srcMatrix(self, srcMatrix: list) -> None:
        """
          This method sets the transformation matrix from SRU to SRC

          Parameters:
            srcMatrix (list): The transformation matrix from SRU to SRC
        """
        if type(srcMatrix).__name__ == "list" or srcMatrix == None:
            self.__srcMatrix = srcMatrix
        else:
            raise TypeError(
                "srcMatrix must be a list, but is {}".format(type(srcMatrix)))

    @property
    def projectionMatrix(self) -> list | None:
        """
          This method returns the projection matrix

          Returns:
            projectionMatrix (list): The projection matrix
        """
        return self.__projectionMatrix

    @projectionMatrix.setter
    def projectionMatrix(self, projectionMatrix: list) -> None:
        """
          This method sets the projection matrix

          Parameters:
            projectionMatrix (list): The projection matrix
        """
        if type(projectionMatrix).__name__ == "list" or projectionMatrix == None:
            self.__projectionMatrix = projectionMatrix
        else:
            raise TypeError(
                "projectionMatrix must be a list, but is {}".format(type(projectionMatrix)))

    @property
    def MjpMatrix(self) -> list | None:
        """
          This method returns the transformation matrix from SRC to STR

          Returns:
            MjpMatrix (list): The transformation matrix from SRC to STR
        """
        return self.__MjpMatrix

    @MjpMatrix.setter
    def MjpMatrix(self, MjpMatrix: list) -> None:
        """
          This method sets the transformation matrix from SRC to STR

          Parameters:
            MjpMatrix (list): The transformation matrix from SRC to STR
        """
        if type(MjpMatrix).__name__ == "list" or MjpMatrix == None:
            self.__MjpMatrix = MjpMatrix
        else:
            raise TypeError(
                "MjpMatrix must be a list, but is {}".format(type(MjpMatrix)))

    @property
    def MSruSrtMatrix(self) -> list | None:
        """
          This method returns the transformation matrix from SRU to STR

          Returns:
            MSruSrtMatrix (list): The transformation matrix from SRU to STR
        """
        return self.__MSruSrtMatrix

    @MSruSrtMatrix.setter
    def MSruSrtMatrix(self, MSruSrtMatrix: list) -> None:
        """
          This method sets the transformation matrix from SRU to STR

          Parameters:
            MSruSrtMatrix (list): The transformation matrix from SRU to STR
        """
        if isinstance(MSruSrtMatrix, list) or MSruSrtMatrix is None:
            self.__MSruSrtMatrix = MSruSrtMatrix
        else:
            raise TypeError(
                "MSruSrtMatrix must be a list, but is {}".format(type(MSruSrtMatrix)))

    def calculateMatrices(self) -> None:
        """
          This method calculates the transformation matrix from SRU to SRC, the projection matrix and the transformation matrix from SRC to STR
        """

        # Define the pipeline matrices
        self.srcMatrix = pipeline.calculateSrcMatrix(
            self.vrp, self.p, self.projectionType)
        self.projectionMatrix = pipeline.calculateProjectionMatrix(
            self.vrp, self.p, self.d, self.projectionType)
        self.MjpMatrix = pipeline.calculateMjpMatrix(
            [self.window[0], self.window[1]], [self.window[2], self.window[3]], [self.viewPort[0], self.viewPort[1]], [self.viewPort[2], self.viewPort[3]])

        # Calculate the transformation matrix from SRU to STR
        # Note that the order of the matrix multiplication is important
        # in this case the order is: MjpMatrix * projectionMatrix * srcMatrix
        # this is because the matrix multiplication is not commutative
        self.MSruSrtMatrix = matrixMultiplication(
            self.MjpMatrix, self.projectionMatrix)
        self.MSruSrtMatrix = matrixMultiplication(
            self.MSruSrtMatrix, self.srcMatrix)
