import tkinter as tk
from core.camera import Camera

from models.scene import Scene


class GUI:
    def __init__(self, width: int, height: int, root: tk.Tk):

        self.width = width
        self.height = height
        self.root = root

        self.frontal_canvas: tk.Canvas = self._create_canvas(
            "Frontal view", 0, 0)

        self.top_canvas: tk.Canvas = self._create_canvas("Top view", 0, 1)

        self.side_candas: tk.Canvas = self._create_canvas("Side view", 1, 0)

        self.isometric_canvas: tk.Canvas = self._create_canvas(
            "Isometric view", 1, 1)

        self.scene: Scene = None

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        if type(width).__name__ == "int":
            self.__width = width
        else:
            raise TypeError(
                "width must be a int, but is {}".format(type(width)))

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        if type(height).__name__ == "int":
            self.__height = height
        else:
            raise TypeError(
                "height must be a int, but is {}".format(type(height)))

    @property
    def root(self) -> tk.Tk:
        return self.__root

    @root.setter
    def root(self, root: tk.Tk):
        if type(root).__name__ == "Tk":
            self.__root = root
        else:
            raise TypeError(
                "root must be a Tk, but is {}".format(type(root)))

    @property
    def frontal_canvas(self) -> tk.Canvas:
        return self.__frontal_canvas

    @frontal_canvas.setter
    def frontal_canvas(self, frontal_canvas: tk.Canvas):
        if type(frontal_canvas).__name__ == "Canvas":
            self.__frontal_canvas = frontal_canvas
        else:
            raise TypeError(
                "frontal_canvas must be a Canvas, but is {}".format(type(frontal_canvas)))

    @property
    def top_canvas(self) -> tk.Canvas:
        return self.__top_canvas

    @top_canvas.setter
    def top_canvas(self, top_canvas: tk.Canvas):
        if type(top_canvas).__name__ == "Canvas":
            self.__top_canvas = top_canvas
        else:
            raise TypeError(
                "top_canvas must be a Canvas, but is {}".format(type(top_canvas)))

    @property
    def side_candas(self) -> tk.Canvas:
        return self.__side_candas

    @side_candas.setter
    def side_candas(self, side_candas: tk.Canvas):
        if type(side_candas).__name__ == "Canvas":
            self.__side_candas = side_candas
        else:
            raise TypeError(
                "side_candas must be a Canvas, but is {}".format(type(side_candas)))

    @property
    def isometric_canvas(self) -> tk.Canvas:
        return self.__isometric_canvas

    @isometric_canvas.setter
    def isometric_canvas(self, isometric_canvas: tk.Canvas):
        if type(isometric_canvas).__name__ == "Canvas":
            self.__isometric_canvas = isometric_canvas
        else:
            raise TypeError(
                "isometric_canvas must be a Canvas, but is {}".format(type(isometric_canvas)))

    @property
    def scene(self) -> Scene:
        return self.__scene

    @scene.setter
    def scene(self, scene: Scene):
        if type(scene).__name__ == "Scene" or scene == None:
            self.__scene = scene
        else:
            raise TypeError(
                "scene must be a Scene, but is {}".format(type(scene)))

    def _create_canvas(self, label_text: str, row: int, column: int) -> tk.Canvas:
        """
        This is a private method to create a canvas with the given label text.

        :param label_text: The text to display on the canvas
        :param row: The row to place the canvas in
        :param column: The column to place the canvas in

        :return: The frame containing the canvas
        """
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=self.width,
                           height=self.height, bg='black')

        canvas.pack()

        # Draw vertical line in the middle
        canvas.create_line(
            self.width / 2, 0, self.width / 2, self.height, fill="gray")

        # Draw horizontal line cutting through the middle like a plane
        canvas.create_line(0, self.height / 2, self.width,
                           self.height / 2, fill="gray", dash=(4, 4))

        label = tk.Label(frame, text=label_text)
        label.pack()
        frame.grid(row=row, column=column)

        return frame.winfo_children()[0]

    def getCanvasReferences(self) -> tuple[tk.Canvas]:
        """
        This method returns the reference for all canvas in gui

        :return: tuple[tk.Canvas] The reference for all canvas in gui
        the order is: `frontal, top, side and  isometric`

        """
        return self.frontal_canvas, self.top_canvas, self.side_candas, self.isometric_canvas

    def make_scene(self, scene: 'Scene') -> None:
        """
        This method creates a scene in the gui and draws it if the scene contains objects

        :param scene: The scene to draw

        :return: None
        """

        if scene is None:

            camera = Camera(
                viewPort=[-self.width/2, self.width, -self.height/2, self.height/2])

            self.scene = Scene(camera=camera, objects=[])

            return
        elif type(scene).__name__ != "Scene":
            raise TypeError(
                "scene must be a Communist Scene, but is Capitalist {}".format(type(scene)))
        else:
            self.scene = scene
        self.draw_scene()

    def draw_scene(self, size_dot: int = 4, color: str = 'white') -> None:
        """
        This method draws the scene in the gui

        :param size_dot: The size of the vertexes
        :param color: The color of the vertexes and edges

        :return: None
        """

        if self.scene.objects.__len__() == 0:
            return

        # iterate over all objects in scene
        for object in self.scene.objects:

            # get the faces of the object
            faces = object.face_objects

            if faces is not None:
                # variable to iterate over the faces
                he = None

                for face in faces:
                    # if the face is not visible, skip it
                    if not face.visible:
                        continue

                    # get the first half-edge of the face
                    he = face.half_edge

                    # until the next half-edge is the first half-edge of the face
                    while True:
                        # draw the edge
                        self.frontal_canvas.create_line(he.origin.x, he.origin.y,
                                                        he.next.origin.x, he.next.origin.y, fill=color)
                        self.top_canvas.create_line(he.origin.x, he.origin.z,
                                                    he.next.origin.x, he.next.origin.z, fill=color)
                        self.side_candas.create_line(he.origin.y, he.origin.z,
                                                     he.next.origin.y, he.next.origin.z, fill=color)
                        self.isometric_canvas.create_line(he.origin.x_screen, he.origin.y_screen,
                                                          he.next.origin.x_screen, he.next.origin.y_screen, fill=color)
                        # draw the vertex(dots)
                        self.frontal_canvas.create_oval(he.origin.x-size_dot, he.origin.y-size_dot,
                                                        he.origin.x+size_dot, he.origin.y+size_dot, fill=color)

                        self.top_canvas.create_oval(he.origin.x-size_dot, he.origin.z-size_dot,
                                                    he.origin.x+size_dot, he.origin.z+size_dot, fill=color)

                        self.side_candas.create_oval(he.origin.y-size_dot, he.origin.z-size_dot,
                                                     he.origin.y+size_dot, he.origin.z+size_dot, fill=color)

                        self.isometric_canvas.create_oval(he.origin.x_screen-size_dot, he.origin.y_screen-size_dot,
                                                          he.origin.x_screen+size_dot, he.origin.y_screen+size_dot, fill=color)

                        # iterate over the half-edge
                        he = he.next
                        if he == face.half_edge:
                            break
