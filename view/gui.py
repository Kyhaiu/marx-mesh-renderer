import math
import os
import sys
import tkinter as tk
import pickle

from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from core.camera import Camera
from models.object import Object
from models.scene import Scene
from utils.letter_selector import get_letter
from PIL import Image, ImageTk


class GUI:
    def __init__(self, width: int, height: int, root: tk.Tk):

        self.width = width
        self.height = height
        self.root = root

        self.components: list[tk.Button] = []

        self.frontal_canvas: tk.Canvas = self._create_canvas(
            "Frontal view", 1, 1)

        self.top_canvas: tk.Canvas = self._create_canvas("Top view", 1, 2)

        self.side_canvas: tk.Canvas = self._create_canvas("Side view", 2, 1)

        self.perspective: tk.Canvas = self._create_canvas(
            "Perspective view", 2, 2)

        self.scene: Scene = Scene()

        self._selected_object_canvas: Object = None
        self._click_x = 0
        self._click_y = 0

        self._offset_x = 0
        self._offset_y = 0

        self._dragging = False

        self._operation_selected = 'translation'

        self._clicked_canvas_name = None

        self._create_components()

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
    def side_canvas(self) -> tk.Canvas:
        return self.__side_candas

    @side_canvas.setter
    def side_canvas(self, side_canvas: tk.Canvas):
        if type(side_canvas).__name__ == "Canvas":
            self.__side_candas = side_canvas
        else:
            raise TypeError(
                "side_canvas must be a Canvas, but is {}".format(type(side_canvas)))

    @property
    def perspective(self) -> tk.Canvas:
        return self.__isometric_canvas

    @perspective.setter
    def perspective(self, perspective: tk.Canvas):
        if type(perspective).__name__ == "Canvas":
            self.__isometric_canvas = perspective
        else:
            raise TypeError(
                "perspective must be a Canvas, but is {}".format(type(perspective)))

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

    @property
    def _selected_object_canvas(self) -> Object:
        return self.__selected_object_canvas

    @_selected_object_canvas.setter
    def _selected_object_canvas(self, selected_object_canvas: Object):
        if type(selected_object_canvas).__name__ == "Object" or selected_object_canvas == None:
            self.__selected_object_canvas = selected_object_canvas
        else:
            raise TypeError(
                "selected_object_canvas must be a Object, but is {}".format(type(selected_object_canvas)))

    @property
    def _click_x(self) -> int | float:
        return self.__click_x

    @_click_x.setter
    def _click_x(self, click_x: int | float):
        if type(click_x).__name__ == "int" or type(click_x).__name__ == "float":
            self.__click_x = click_x
        else:
            raise TypeError(
                "click_x must be a float or int, but is {}".format(type(click_x)))

    @property
    def _click_y(self) -> int:
        return self.__click_y

    @_click_y.setter
    def _click_y(self, click_y: float | int):
        if type(click_y).__name__ == "int" or type(click_y).__name__ == "float":
            self.__click_y = click_y
        else:
            raise TypeError(
                "click_y must be a float or int, but is {}".format(type(click_y)))

    @property
    def _offset_x(self) -> float | int:
        return self.__offset_x

    @_offset_x.setter
    def _offset_x(self, offset_x: float | int):
        if type(offset_x).__name__ == "float" or type(offset_x).__name__ == "int":
            self.__offset_x = offset_x
        else:
            raise TypeError(
                "offset_x must be a float or int, but is {}".format(type(offset_x)))

    @property
    def _offset_y(self) -> int | float:
        return self.__offset_y

    @_offset_y.setter
    def _offset_y(self, offset_y: float | int):
        if type(offset_y).__name__ == "float" or type(offset_y).__name__ == "int":
            self.__offset_y = offset_y
        else:
            raise TypeError(
                "offset_y must be a float or int, but is {}".format(type(offset_y)))

    @property
    def _dragging(self) -> bool:
        return self.__dragging

    @_dragging.setter
    def _dragging(self, dragging: bool):
        if type(dragging).__name__ == "bool":
            self.__dragging = dragging
        else:
            raise TypeError(
                "dragging must be a bool, but is {}".format(type(dragging)))

    @property
    def _operation_selected(self) -> str:
        return self.__operation_selected

    @_operation_selected.setter
    def _operation_selected(self, operation: str):
        if type(operation).__name__ == "str" or operation == None:
            self.__operation_selected = operation
        else:
            raise TypeError(
                "canvas_clicked_name must be a str, but is {}".format(type(operation)))

    @property
    def _clicked_canvas_name(self) -> str:
        return self.__clicked_canvas_name

    @_clicked_canvas_name.setter
    def _clicked_canvas_name(self, clicked_canvas: tk.Canvas):
        if type(clicked_canvas).__name__ == "str" or clicked_canvas == None:
            self.__clicked_canvas_name = clicked_canvas
        else:
            raise TypeError(
                "clicked_canvas must be a str, but is {}".format(type(clicked_canvas)))

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

        label = tk.Label(frame, text=label_text)
        label.pack()
        frame.grid(row=row, column=column)

        if label_text == "Side view":
            canvas.bind("<Button-1>", self._mouse_click_side_view)
        elif label_text == "Frontal view":
            canvas.bind("<Button-1>", self._mouse_click_frontal_view)
        elif label_text == "Top view":
            canvas.bind("<Button-1>", self._mouse_click_top_view)

        canvas.bind("<B1-Motion>", self._mouse_motion)
        canvas.bind("<ButtonRelease-1>", self._mouse_release)

        return frame.winfo_children()[0]

    def _create_components(self) -> None:
        """
        This function has the purpose of creating the other components of GUI,
        like buttons, labels, text fields, menus, etc.

        :return: None
        """
        frame = tk.Frame(self.root)

        iconPath = os.path.abspath('./view/icons')

        addIcon = tk.PhotoImage(file=os.path.join(iconPath, "add.png"))
        removeIcon = tk.PhotoImage(file=os.path.join(iconPath, "delete.png"))
        clearIcon = tk.PhotoImage(file=os.path.join(iconPath, "reset.png"))
        saveIcon = tk.PhotoImage(file=os.path.join(iconPath, "export.png"))
        loadIcon = tk.PhotoImage(file=os.path.join(iconPath, "import.png"))
        moveIcon = tk.PhotoImage(file=os.path.join(iconPath, "move.png"))
        rotateIcon = tk.PhotoImage(file=os.path.join(iconPath, "rotate.png"))
        scaleIcon = tk.PhotoImage(file=os.path.join(iconPath, "scale.png"))
        shearIcon = tk.PhotoImage(file=os.path.join(iconPath, "shear.png"))

        scene_actions_label = tk.Label(frame, text="Scene actions")
        scene_actions_label.grid(
            row=0, column=0, columnspan=2, sticky="nsew")

        saveButton = tk.Button(frame, text="Save scene",
                               image=saveIcon, command=self._save_scene)
        saveButton.grid(row=1, column=0)

        loadButton = tk.Button(frame, text="Load scene",
                               image=loadIcon, command=self._load_scene)
        loadButton.grid(row=1, column=1)

        clearButton = tk.Button(frame, text="Clear scene",
                                image=clearIcon, command=self._clear_scene)
        clearButton.grid(row=2, column=0)

        addButton = tk.Button(frame, text="Add text",
                              image=addIcon, command=self._add_object)
        addButton.grid(row=3, column=0)

        removeButton = tk.Button(
            frame, text="Remove letter", image=removeIcon, command=self._remove_object)
        removeButton.grid(row=3, column=1)

        letters_actions_label = tk.Label(frame, text="Letters actions")
        letters_actions_label.grid(
            row=4, column=0, columnspan=2, sticky="nsew")

        moveButton = tk.Button(frame, text="Move letter",
                               image=moveIcon, command=self._move_object)
        moveButton.grid(row=5, column=0)

        rotateButton = tk.Button(
            frame, text="rotate letter", image=rotateIcon, command=self._rotate_object)
        rotateButton.grid(row=5, column=1)

        scaleButton = tk.Button(
            frame, text="Scale letter", image=scaleIcon, command=self._scale_object)
        scaleButton.grid(row=6, column=0)

        shearButton = tk.Button(
            frame, text="Shear letter", image=shearIcon, command=self._shear_object)
        shearButton.grid(row=6, column=1)

        addButton.image = addIcon  # Retain a reference to the image
        removeButton.image = removeIcon
        clearButton.image = clearIcon
        saveButton.image = saveIcon
        loadButton.image = loadIcon
        moveButton.image = moveIcon
        rotateButton.image = rotateIcon
        scaleButton.image = scaleIcon
        shearButton.image = shearIcon

        frame.grid(row=1, column=0)

        self.components.append(addButton)
        self.components.append(removeButton)
        self.components.append(clearButton)
        self.components.append(saveButton)
        self.components.append(loadButton)
        self.components.append(moveButton)
        self.components.append(rotateButton)
        self.components.append(scaleButton)
        self.components.append(shearButton)

        scene_settings_frame = tk.Frame(self.root)

        # Camera settings (VRP)
        vrp_label = tk.Label(scene_settings_frame, text="VRP")
        vrp_label.grid(row=0, column=0, columnspan=6, sticky="nsew")

        vrp_x_label = tk.Label(scene_settings_frame, text="X:")
        vrp_x_label.grid(row=1, column=0)
        self.vrp_x = tk.Entry(scene_settings_frame, width=5)
        self.vrp_x.grid(row=1, column=1)
        self.vrp_x.insert(0, self.scene.perspective_camera.vrp.x)
        self.vrp_x.bind("<FocusOut>", self._on_entry_change)

        vrp_y_label = tk.Label(scene_settings_frame, text="Y:")
        vrp_y_label.grid(row=1, column=2)
        self.vrp_y = tk.Entry(scene_settings_frame, width=5)
        self.vrp_y.grid(row=1, column=3)
        self.vrp_y.insert(0, self.scene.perspective_camera.vrp.y)
        self.vrp_y.bind("<FocusOut>", self._on_entry_change)

        vrp_z_label = tk.Label(scene_settings_frame, text="Z:")
        vrp_z_label.grid(row=1, column=4)
        self.vrp_z = tk.Entry(scene_settings_frame, width=5)
        self.vrp_z.grid(row=1, column=5)
        self.vrp_z.insert(0, self.scene.perspective_camera.vrp.z)
        self.vrp_z.bind("<FocusOut>", self._on_entry_change)

        focal_label = tk.Label(scene_settings_frame, text="Focal")
        focal_label.grid(row=2, column=0, columnspan=6, sticky="nsew")

        focal_x_label = tk.Label(scene_settings_frame, text="X:")
        focal_x_label.grid(row=3, column=0)
        self.focal_x = tk.Entry(scene_settings_frame, width=5)
        self.focal_x.grid(row=3, column=1)
        self.focal_x.insert(0, self.scene.perspective_camera.p.x)
        self.focal_x.bind("<FocusOut>", self._on_entry_change)

        focal_y_label = tk.Label(scene_settings_frame, text="Y:")
        focal_y_label.grid(row=3, column=2)
        self.focal_y = tk.Entry(scene_settings_frame, width=5)
        self.focal_y.grid(row=3, column=3)
        self.focal_y.insert(0, self.scene.perspective_camera.p.y)
        self.focal_y.bind("<FocusOut>", self._on_entry_change)

        focal_z_label = tk.Label(scene_settings_frame, text="Z:")
        focal_z_label.grid(row=3, column=4)
        self.focal_z = tk.Entry(scene_settings_frame, width=5)
        self.focal_z.grid(row=3, column=5)
        self.focal_z.insert(0, self.scene.perspective_camera.p.z)
        self.focal_z.bind("<FocusOut>", self._on_entry_change)

        # Window settings
        window_label = tk.Label(scene_settings_frame, text="Window")
        window_label.grid(row=4, column=0, columnspan=6, sticky="nsew")

        width_label = tk.Label(scene_settings_frame, text="Width:")
        width_label.grid(row=5, column=0)
        # Set the width to 10 characters
        self.width_entry = tk.Entry(scene_settings_frame, width=5)
        self.width_entry.grid(row=5, column=1)
        self.width_entry.bind("<FocusOut>", self._on_entry_change)
        self.width_entry.insert(0, self.scene.perspective_camera.window[1])

        height_label = tk.Label(scene_settings_frame, text="Height:")
        height_label.grid(row=5, column=2)
        self.height_entry = tk.Entry(scene_settings_frame, width=5)
        self.height_entry.grid(row=5, column=3)
        self.height_entry.bind("<FocusOut>", self._on_entry_change)
        self.height_entry.insert(0, self.scene.perspective_camera.window[3])

        # Light settings
        ila_label = tk.Label(scene_settings_frame, text="Ambient Light")
        ila_label.grid(row=6, column=0, columnspan=6, sticky="nsew")

        ila_label_r = tk.Label(scene_settings_frame, text="R:")
        ila_label_r.grid(row=7, column=0)
        self.ila_r = tk.Entry(scene_settings_frame, width=5)
        self.ila_r.grid(row=7, column=1)
        self.ila_r.bind("<FocusOut>", self._on_entry_change)

        ila_g_label = tk.Label(scene_settings_frame, text="G:")
        ila_g_label.grid(row=7, column=2)
        self.ila_g = tk.Entry(scene_settings_frame, width=5)
        self.ila_g.grid(row=7, column=3)
        self.ila_g.bind("<FocusOut>", self._on_entry_change)

        ila_b_label = tk.Label(scene_settings_frame, text="B:")
        ila_b_label.grid(row=7, column=4)
        self.ila_b = tk.Entry(scene_settings_frame, width=5)
        self.ila_b.grid(row=7, column=5)
        self.ila_b.bind("<FocusOut>", self._on_entry_change)

        ka_label = tk.Label(scene_settings_frame, text="Ambient Coefficient")
        ka_label.grid(row=8, column=0, columnspan=6, sticky="nsew")

        ka_r_label = tk.Label(scene_settings_frame, text="R:")
        ka_r_label.grid(row=9, column=0)
        self.ka_r = tk.Entry(scene_settings_frame, width=5)
        self.ka_r.grid(row=9, column=1)
        self.ka_r.bind("<FocusOut>", self._on_entry_change)

        ka_g_label = tk.Label(scene_settings_frame, text="G:")
        ka_g_label.grid(row=9, column=2)
        self.ka_g = tk.Entry(scene_settings_frame, width=5)
        self.ka_g.grid(row=9, column=3)
        self.ka_g.bind("<FocusOut>", self._on_entry_change)

        ka_b_label = tk.Label(scene_settings_frame, text="B:")
        ka_b_label.grid(row=9, column=4)
        self.ka_b = tk.Entry(scene_settings_frame, width=5)
        self.ka_b.grid(row=9, column=5)
        self.ka_b.bind("<FocusOut>", self._on_entry_change)

        il_label = tk.Label(scene_settings_frame, text="Light Intensity")
        il_label.grid(row=10, column=0, columnspan=6, sticky="nsew")

        il_r_label = tk.Label(scene_settings_frame, text="R:")
        il_r_label.grid(row=11, column=0)
        self.il_r = tk.Entry(scene_settings_frame, width=5)
        self.il_r.grid(row=11, column=1)
        self.il_r.bind("<FocusOut>", self._on_entry_change)

        il_g_label = tk.Label(scene_settings_frame, text="G:")
        il_g_label.grid(row=11, column=2)
        self.il_g = tk.Entry(scene_settings_frame, width=5)
        self.il_g.grid(row=11, column=3)
        self.il_g.bind("<FocusOut>", self._on_entry_change)

        il_b_label = tk.Label(scene_settings_frame, text="B:")
        il_b_label.grid(row=11, column=4)
        self.il_b = tk.Entry(scene_settings_frame, width=5)
        self.il_b.grid(row=11, column=5)
        self.il_b.bind("<FocusOut>", self._on_entry_change)

        scene_settings_frame.grid(row=2, column=0)

    def getCanvasReferences(self) -> tuple[tk.Canvas]:
        """
        This method returns the reference for all canvas in gui

        :return: tuple[tk.Canvas] The reference for all canvas in gui
        the order is: `frontal, top, side and  isometric`

        """
        return self.frontal_canvas, self.top_canvas, self.side_canvas, self.perspective

    def make_scene(self, scene: 'Scene') -> None:
        """
        This method creates a scene in the gui and draws it if the scene contains objects

        :param scene: The scene to draw

        :return: None
        """

        if scene is None:

            camera = Camera(
                viewPort=[-self.width/2, self.width/2, -self.height/2, self.height/2])

            self.scene = Scene(camera=camera, objects=[])

            return
        elif type(scene).__name__ != "Scene":
            raise TypeError(
                "scene must be a Communist Scene, but is Capitalist {}".format(type(scene)))
        else:
            self.scene = scene
        self.draw_scene()

    def draw_scene(self, size_dot: int = 2, color: str = 'white') -> None:
        """
        This method draws the scene in the gui

        :param size_dot: The size of the vertexes
        :param color: The color of the vertexes and edges

        :return: None
        """

        if self.scene.objects.__len__() == 0:
            return
        selected_one = False
        i = 1
        # iterate over all objects in scene
        for object in self.scene.objects:

            if object == self._selected_object_canvas:
                selected_one = True
            else:
                selected_one = False

            # get the faces of the object
            faces = object.face_objects

            # if i == 1:
            # print(faces[0].id)
            # print(faces[0].half_edge.origin, faces[0].half_edge.prev.origin,
            #       faces[0].half_edge.next.origin)

            he = None
            for face in faces:
                he = face.half_edge
                while True:
                    # draw the edge
                    self.frontal_canvas.create_line(he.origin.x_front, he.origin.y_front,
                                                    he.next.origin.x_front, he.next.origin.y_front, fill='red' if selected_one else color)
                    self.top_canvas.create_line(he.origin.x_top, he.origin.z_top,
                                                he.next.origin.x_top, he.next.origin.z_top, fill='red' if selected_one else color)
                    self.side_canvas.create_line(he.origin.z_side, he.origin.y_side,
                                                 he.next.origin.z_side, he.next.origin.y_side, fill='red' if selected_one else color)

                    self.frontal_canvas.create_oval(he.origin.x_front-size_dot, he.origin.y_front-size_dot,
                                                    he.origin.x_front+size_dot, he.origin.y_front+size_dot, fill=color)

                    self.top_canvas.create_oval(he.origin.x_top-size_dot, he.origin.z_top-size_dot,
                                                he.origin.x_top+size_dot, he.origin.z_top+size_dot, fill=color)

                    self.side_canvas.create_oval(he.origin.z_side-size_dot, he.origin.y_side-size_dot,
                                                 he.origin.z_side+size_dot, he.origin.y_side+size_dot, fill=color)

                    he = he.next
                    if he == face.half_edge:
                        break

            if faces is not None:

                # image_buffer = self.scene.image_buffer

                # Convert the pixel values to a valid color
                # Assuming pixel is a tuple of (R, G, B) values

                # Example for a colored image (3 channels - R, G, B):
                # for face in faces:
                #     if not face.visible:
                #         continue
                #     self.scene.scanline_fill(self.frontal_canvas, face)
                # for y, row in enumerate(image_buffer):
                #     for x, pixel in enumerate(row):
                #         color = f'#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}'

                #         self.perspective.create_rectangle(
                #             x-10, y-10, x+10, y+10, fill=color)

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

                        print('Drawing edge: ' + str(he.origin.id) +
                              ' -> ' + str(he.next.origin.id))
                        print('Origin: ', he.origin)
                        print('Next: ', he.next.origin)

                        self.perspective.create_line(he.origin.x_screen, he.origin.y_screen,
                                                     he.next.origin.x_screen, he.next.origin.y_screen, fill=color)

                        center_x = (he.origin.x_screen-size_dot +
                                    he.origin.x_screen+size_dot) / 2
                        center_y = (he.origin.y_screen-size_dot +
                                    he.origin.y_screen+size_dot) / 2

                        # self.perspective.create_oval(he.origin.x_screen-size_dot, he.origin.y_screen-size_dot,
                        #                              he.origin.x_screen+size_dot, he.origin.y_screen+size_dot, fill=color)

                        self.perspective.create_text(
                            center_x, center_y, text=he.origin.id, fill='red')

                        # iterate(counter clockwise) over the half-edge
                        he = he.next
                        if he == face.half_edge:
                            break

    def _mouse_click_frontal_view(self, event: tk.Event) -> None:
        '''
        This method is called when the user clicks on the frontal view

        :param event: The event of the click

        :return: None
        '''
        x = event.x
        y = event.y

        self.scene.select_object(x, y, 'frontal')
        # if the object is None, the update will be done in the redraw method (to deselect the object)
        if self.scene.selected_object is not None:
            self._selected_object_canvas = self.scene.selected_object
            self._clicked_canvas_name = 'frontal'

        self._redraw_selected_object(self.scene.selected_object)

        # The deselection of the object is done in the redraw method
        if self.scene.selected_object is not None:
            # if this happens, the object was selected
            # then we need to define the geometric center of the object
            self.__selected_object_canvas.define_geometric_center('frontal')

            self._click_x = x
            self._click_y = y

            self._offset_x = x - self.__selected_object_canvas.geometric_center.x_front
            self._offset_y = y - self.__selected_object_canvas.geometric_center.y_front

            # if self._offset_x > 10:
            self._dragging = True

    def _mouse_click_top_view(self, event: tk.Event) -> None:
        '''
        This method is called when the user clicks on the top view

        :param event: The event of the click

        :return: None
        '''
        x = event.x
        y = event.y

        self.scene.select_object(x, y, 'top')
        # if the object is None, the update will be done in the redraw method (to deselect the object)
        if self.scene.selected_object is not None:
            self._selected_object_canvas = self.scene.selected_object
            self._clicked_canvas_name = 'top'

        self._redraw_selected_object(self.scene.selected_object)

        # The deselection of the object is done in the redraw method
        if self.scene.selected_object is not None:
            # if this heappens, the object was selected
            # then we need to define the geometric center of the object
            self.__selected_object_canvas.define_geometric_center('top')

            self._click_x = x
            self._click_y = y

            self._offset_x = x - self.__selected_object_canvas.geometric_center.x_top
            self._offset_y = y - self.__selected_object_canvas.geometric_center.y_top

            self._dragging = True

    def _mouse_click_side_view(self, event: tk.Event) -> None:
        '''
        This method is called when the user clicks on the side view

        :param event: The event of the click

        :return: None
        '''
        x = event.x
        y = event.y

        self.scene.select_object(x, y, 'side')
        if self.scene.selected_object is not None:
            self._selected_object_canvas = self.scene.selected_object
            self._dragging = True
            self._clicked_canvas_name = 'side'

        self._redraw_selected_object(self.scene.selected_object)

        # The deselection of the object is done in the redraw method
        if self.scene.selected_object is not None:
            # if this heappens, the object was selected
            # then we need to define the geometric center of the object
            self.__selected_object_canvas.define_geometric_center('side')

            self._click_x = x
            self._click_y = y

            self._offset_x = x - self.__selected_object_canvas.geometric_center.x_side
            self._offset_y = y - self.__selected_object_canvas.geometric_center.y_side

            self._dragging = True

    def _redraw_selected_object(self, object: Object) -> None:
        '''
        This method redraws the selected object

        :param object: The object to redraw

        :return: None
        '''
        if object is None and self._selected_object_canvas is None:
            return

        if object is None and self._selected_object_canvas is not None:
            # deselect the object (redraw the selected one in white)

            for face in self._selected_object_canvas.face_objects:
                he = face.half_edge
                while True:
                    self.frontal_canvas.create_line(he.origin.x_front, he.origin.y_front,
                                                    he.next.origin.x_front, he.next.origin.y_front, fill='white')
                    self.top_canvas.create_line(he.origin.x_top, he.origin.z_top,
                                                he.next.origin.x_top, he.next.origin.z_top, fill='white')
                    self.side_canvas.create_line(he.origin.z_side, he.origin.y_side,
                                                 he.next.origin.z_side, he.next.origin.y_side, fill='white')

                    he = he.next
                    if he == face.half_edge:
                        break
            self._selected_object_canvas = None
        else:
            # draw the selected object in red
            for face in self._selected_object_canvas.face_objects:
                he = face.half_edge
                while True:
                    self.frontal_canvas.create_line(he.origin.x_front, he.origin.y_front,
                                                    he.next.origin.x_front, he.next.origin.y_front, fill='red')
                    self.top_canvas.create_line(he.origin.x_top, he.origin.z_top,
                                                he.next.origin.x_top, he.next.origin.z_top, fill='red')
                    self.side_canvas.create_line(he.origin.z_side, he.origin.y_side,
                                                 he.next.origin.z_side, he.next.origin.y_side, fill='red')

                    he = he.next
                    if he == face.half_edge:
                        break

    def _clear_scene(self) -> None:
        """
        This method clears the scene

        :return: None
        """
        self.scene.clear()

        self._update_canvas()

    def _save_scene(self) -> None:
        '''
        This method is called when the user clicks on the save scene button

        :return: None
        '''
        data = {
            'scene': self.scene,
        }

        file_directory = filedialog.askdirectory()

        if file_directory:
            file_name = filedialog.asksaveasfilename(
                initialdir=file_directory, title="Select file", filetypes=(("MRX files", "*.mrx"), ("All Files", "*.*")))
            if file_name:
                with open(file_name, 'wb') as file:
                    try:
                        pickle.dump(data, file)
                        messagebox.showinfo(
                            title="Success", message="The file was saved successfully")
                    except:
                        messagebox.showerror(
                            title="Error", message="An error occurred while saving the file")

    def _load_scene(self) -> None:
        '''
        This method is called when the user clicks on the load scene button

        :return: None
        '''
        file_directory = filedialog.askopenfilename()

        # validate if the file is a pickle file
        if file_directory.endswith('.mrx'):
            with open(file_directory, 'rb') as file:
                data = pickle.load(file)
                self.scene.clear()
                self._update_canvas()
                self.make_scene(data['scene'])
        else:
            # open a error window
            messagebox.showerror(
                title="Error", message="The file is not a pickle file")

    def on_validate_input(self, user_input: str) -> None:
        """
        This method is called when the user inputs a value in the entry

        :param user_input: The input of the user

        :return: True if the input is valid, False otherwise
        """
        if len(user_input) <= 10:  # Limit the input to 10 characters
            return True
        else:
            self.root.bell()  # Beep to indicate invalid input
            return False

    def _add_object(self) -> None:
        '''
        This method is called when the user clicks on the add object button

        :return: None
        '''
        user_input = simpledialog.askstring(
            "Input", "Enter with your string (Max 5 characters)")

        if user_input is not None and user_input != '' and len(user_input) < 5:
            # for each char in the input string add the corresponding object

            for i, char in enumerate(user_input):
                if i == len(user_input) - 1:
                    self.scene.addObject(get_letter(char, True))
                else:
                    self.scene.addObject(get_letter(char, False))

                self.draw_scene()
        else:
            if len(user_input) >= 5:
                messagebox.showerror(
                    title="Error", message="The string must have less than 5 characters")

    def _remove_object(self) -> None:
        '''
        This method is called when the user clicks on the remove object button

        :return: None
        '''
        print('removing object')

    def _move_object(self) -> None:
        '''
        This method is called when the user clicks on the move object button

        :return: None
        '''
        self._operation_selected = 'translation'

    def _rotate_object(self) -> None:
        '''
        This method is called when the user clicks on the rotate object button

        :return: None
        '''
        self._operation_selected = 'rotate'

        print('-'*50)

        self._update_canvas()

    def _scale_object(self) -> None:
        '''
        This method is called when the user clicks on the scale object button

        :return: None
        '''
        self._operation_selected = 'scale'

    def _shear_object(self) -> None:
        '''
        This method is called when the user clicks on the scale object button

        :return: None
        '''
        self._operation_selected = 'shear'

    def _update_canvas(self) -> None:
        '''
        This method updates the canvas

        :return: None
        '''
        # Clear all canvas items
        self.scene.update()

        self.frontal_canvas.delete("all")
        self.top_canvas.delete("all")
        self.side_canvas.delete("all")
        self.perspective.delete("all")

        self.draw_scene()

        self.frontal_canvas.update()
        self.top_canvas.update()
        self.side_canvas.update()
        self.perspective.update()

    def _mouse_motion(self, event: tk.Event) -> None:
        """
        This method is called when the user moves the mouse

        :param event: The event of the mouse motion

        :return: None
        """
        if self._dragging and self._selected_object_canvas is not None:
            x = event.x
            y = event.y

            delta_x = x - self._click_x
            delta_y = y - self._click_y

            if self._operation_selected == 'translation':
                # self._selected_object_canvas._translate(
                #     delta_x/50, delta_y/50, 0)

                if self._clicked_canvas_name == 'frontal':
                    self._selected_object_canvas._translate(
                        delta_x/100, delta_y/100, 0)
                elif self._clicked_canvas_name == 'top':
                    # the delta y is negative because the y axis is inverted
                    self._selected_object_canvas._translate(
                        delta_x/100, 0, -delta_y/100)
                elif self._clicked_canvas_name == 'side':
                    # the delta x is negative because the y axis is inverted
                    self._selected_object_canvas._translate(
                        0, delta_y/100, -delta_x/100)

            elif self._operation_selected == 'rotate':
                slower_factor = 0.01
                delta_angle_1 = slower_factor * math.atan2(delta_y, delta_x)
                delta_angle_2 = slower_factor * math.atan2(delta_x, delta_y)

                if self._clicked_canvas_name == 'frontal':
                    self._selected_object_canvas._rotate(
                        delta_angle_1, delta_angle_2, 'x', 'y')
                    # self._selected_object_canvas._rotate(
                    #     0.7854, 'y')
                elif self._clicked_canvas_name == 'top':
                    self._selected_object_canvas._rotate(
                        delta_angle_1, delta_angle_2, 'x', 'z')
                    # self._selected_object_canvas._rotate(
                    #     0.7854, 'x')
                    # self._selected_object_canvas._rotate(
                    #     0.7854, 'z')
                elif self._clicked_canvas_name == 'side':
                    self._selected_object_canvas._rotate(
                        delta_angle_1, delta_angle_2, 'z', 'y')
            elif self._operation_selected == 'scale':
                scale_factor = 0.01  # Adjust this value to control the scaling speed
                scale_x = 1 + scale_factor * delta_x
                scale_y = 1 + scale_factor * delta_y

                if self._clicked_canvas_name == 'frontal':
                    self._selected_object_canvas._scale(
                        scale_x, scale_x, 1)
                    self._selected_object_canvas._scale(
                        scale_y, scale_y, 1)
                elif self._clicked_canvas_name == 'top':
                    self._selected_object_canvas._scale(
                        scale_x, 1, scale_x)
                    self._selected_object_canvas._scale(
                        scale_y, 1, scale_y)
                elif self._clicked_canvas_name == 'side':
                    self._selected_object_canvas._scale(
                        1, scale_x, scale_x)
                    self._selected_object_canvas._scale(
                        1, scale_y, scale_y)
            elif self._operation_selected == 'shear':
                shear_factor = 0.01
                shear_x = shear_factor * delta_x
                shear_y = shear_factor * delta_y

                if self._clicked_canvas_name == 'frontal':
                    self._selected_object_canvas._shear(
                        shear_x, shear_x, 0)
                    self._selected_object_canvas._shear(
                        shear_y, shear_y, 0)
                elif self._clicked_canvas_name == 'top':
                    self._selected_object_canvas._shear(
                        shear_x, 0, shear_x)
                    self._selected_object_canvas._shear(
                        shear_y, 0, shear_y)
                elif self._clicked_canvas_name == 'side':
                    self._selected_object_canvas._shear(
                        0, shear_x, shear_x)
                    self._selected_object_canvas._shear(
                        0, shear_y, shear_y)

            self._click_x = x
            self._click_y = y

            self._update_canvas()

    def _mouse_release(self, event: tk.Event) -> None:
        """
        This function is called when the user releases the mouse

        :param event: The event of the mouse release

        :return: None
        """
        if self._dragging:
            self._dragging = False
        return

    def _on_entry_change(self, event: tk.Event) -> None:
        """
        This method is called when the user changes the value of a configuration

        :param event: The event of the entry change

        :return: None
        """
        if sys.getrecursionlimit() < 1000:
            return

        vrp_x = self.vrp_x.get()
        vrp_y = self.vrp_y.get()
        vrp_z = self.vrp_z.get()

        focal_x = self.focal_x.get()
        focal_y = self.focal_y.get()
        focal_z = self.focal_z.get()

        width = self.width_entry.get()
        height = self.height_entry.get()

        ila_r = self.ila_r.get()
        ila_g = self.ila_g.get()
        ila_b = self.ila_b.get()

        ka_r = self.ka_r.get()
        ka_g = self.ka_g.get()
        ka_b = self.ka_b.get()

        il_r = self.il_r.get()
        il_g = self.il_g.get()
        il_b = self.il_b.get()

        if vrp_x != '':
            self.scene.perspective_camera.vrp.x = float(vrp_x)
        if vrp_y != '':
            self.scene.perspective_camera.vrp.y = float(vrp_y)
        if vrp_z != '':
            self.scene.perspective_camera.vrp.z = float(vrp_z)

        if focal_x != '':
            self.scene.perspective_camera.p.x = float(focal_x)
        if focal_y != '':
            self.scene.perspective_camera.p.y = float(focal_y)
        if focal_z != '':
            self.scene.perspective_camera.p.z = float(focal_z)

        if width != '':
            self.scene.perspective_camera.window[0] = -float(width)
            self.scene.perspective_camera.window[1] = float(width)
        if height != '':
            self.scene.perspective_camera.window[2] = -float(height)
            self.scene.perspective_camera.window[3] = float(height)

        self.scene.perspective_camera.calculateMatrices()
        self._update_canvas()
        return
