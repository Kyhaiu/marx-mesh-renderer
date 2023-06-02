from typing import List
from models.vertex import Vertex
from utils import pipeline


class Camera:

    def __init__(
        self,
        vrp: Vertex,
        p: Vertex,
        d: float,
        viewPort: List[float, float],
        window: List[float, float],
        projectionType: str = 'parallel'
    ):
        """
          This method initialize the camera

          Parameters:
            vrp (Vertex): The position of the camera
            p (Vertex): The focal point
            d (float): The distance between the camera and the focal point
            viewPort (list): The viewport
            window (list): The window
        """
        # basic properties for camera
        self.vrp = vrp
        self.p = p
        self.d = d
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

    def __str__(self) -> str:
        """
          This method returns the string representation of the camera

          Returns:
            string (str): The string representation of the camera
        """
        return f"VRP: {self.vrp}\nFocal Point: {self.p}\nDistance: {self.d}\nViewPort: {self.viewPort}\nWindow: {self.window}"

    def getVRP(self) -> Vertex:
        """
          This method returns the VRP

          Returns:
            vrp (Vertex): The VRP
        """
        return self.vrp

    def getFocalPoint(self) -> Vertex:
        """
          This method returns the focal point

          Returns:
            p (Vertex): The focal point
        """
        return self.p

    def getDistance(self) -> float:
        """
          This method returns the distance

          Returns:
            d (float): The distance
        """
        return self.d

    def getViewPort(self) -> List[float, float]:
        """
          This method returns the viewport

          Returns:
            viewPort (list): The viewport
        """
        return self.viewPort

    def getWindow(self) -> List[float, float]:
        """
          This method returns the window

          Returns:
            window (list): The window
        """
        return self.window

    def getProjectionType(self) -> str:
        """
          This method returns the projection type

          Returns:
            projectionType (str): The projection type
        """
        return self.projectionType

    def getSRCMatrix(self) -> list:
        """
          This method returns the SRC matrix used to convert from SRU objects to SRC object

          Returns:
            srcMatrix (list): The SRC matrix
        """
        return self.srcMatrix

    def getProjectionMatrix(self) -> list:
        """
          This method returns the projection matrix

          Returns:
            projectionMatrix (list): The projection matrix
        """
        return self.projectionMatrix

    def getMjpMatrix(self) -> list:
        """
          This method returns the Mjp matrix used to convert from SRC objects to STR objects

          Returns:
            MjpMatrix (list): The Mjp matrix
        """
        return self.MjpMatrix

    def setVRP(self, vrp: Vertex) -> None:
        """
          This method sets the VRP

          Parameters:
            vrp (Vertex): The VRP
        """
        self.vrp = vrp
        self.defineSRCMatrix()
        self.defineProjectionMatrix()

    def setFocalPoint(self, p: Vertex) -> None:
        """
          This method sets the focal point

          Parameters:
            p (Vertex): The focal point
        """
        self.p = p
        self.defineSRCMatrix()
        self.defineProjectionMatrix()

    def setDistance(self, d: float) -> None:
        """
          This method sets the distance

          Parameters:
            d (float): The distance
        """
        self.d = d
        self.defineProjectionMatrix()

    def setViewPort(self, viewPort: List[float, float]) -> None:
        """
          This method sets the viewport

          Parameters:
            viewPort (list): The viewport
        """
        self.viewPort = viewPort

    def setWindow(self, window: List[float, float]) -> None:
        """
          This method sets the window

          Parameters:
            window (list): The window
        """
        self.window = window

    def setProjectionType(self, projectionType: 'parallel' | 'perspective' = 'parallel') -> None:
        """
          This method sets the projection type

          Parameters:
            projectionType (str): The projection type
        """
        self.projectionType = projectionType
        self.defineProjectionMatrix()

    def defineSRCMatrix(self) -> None:
        """
          This method defines the SRC matrix

          Returns:
            This method don't return anything, but it defines the matrix to convert from SRU to SRC
        """

        self.srcMatrix = pipeline.transformSRUtoSRC(self.vrp, self.p)

    def defineProjectionMatrix(self) -> None:
        """
          This method defines the projection matrix

          Returns:
            This method don't return anything, but it defines the projection matrix
        """
        self.projectionMatrix = pipeline.projectionMatrix(
            self.vrp, self.p, self.d, self.projectionType)

    def defineMjpMatrix(self) -> None:
        """
          This method defines the Mjp matrix used to convert from SRC objects to STR objects

          Returns:
            This method don't return anything, but it defines the matrix to convert from SRC to STR
        """
        self.MjpMatrix = pipeline.transformSRCtoSRT(self.viewPort, self.window)
