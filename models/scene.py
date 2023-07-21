import logging
from core.camera import Camera
from models.object import Object
from models.vertex import Vertex
from utils.geometric_transformation import translation
from utils.pipeline import normalize_by_homogeneous_coordinate
from utils.vectors_operations import matrixMultiplication


class Scene:
    def __init__(self, perspective_camera: Camera = None, objects: list[Object] = []):

        if perspective_camera is None:
            self.perspective_camera = Camera(projectionType="perspective")
        else:
            self.perspective_camera = perspective_camera

        self.top_camera = Camera(vrp=Vertex(0, 10, 0), p=Vertex(
            0, 2, 0), d=10, projectionType="top")
        self.front_camera = Camera(projectionType="frontal")
        self.side_camera = Camera(vrp=Vertex(
            10, 0, 0), p=Vertex(2, 0, 0), d=10, projectionType="side")

        self.objects = objects
        self.selected_object = None

    def __str__(self) -> str:
        msg = "Scene(\n"
        msg += "\tcamera: {}\n".format(self.perspective_camera)
        msg += "\tobjects: [\n"
        for object in self.objects:
            msg += "\t\t{}\n".format(object)
        msg += "\t]\n"
        msg += "\tselected_object: {}\n".format(self.selected_object)
        msg += ")"
        return msg

    @ property
    def perspective_camera(self) -> Camera:
        return self.__perspective_camera

    @ perspective_camera.setter
    def perspective_camera(self, perspective_camera: Camera):
        if type(perspective_camera).__name__ == "Camera":
            self.__perspective_camera = perspective_camera
        else:
            raise TypeError(
                "camera must be a Camera, but is {}".format(type(perspective_camera)))

    @ property
    def top_camera(self) -> Camera:
        return self.__top_camera

    @ top_camera.setter
    def top_camera(self, top_camera: Camera):
        if type(top_camera).__name__ == "Camera":
            self.__top_camera = top_camera
        else:
            raise TypeError(
                "camera must be a Camera, but is {}".format(type(top_camera)))

    @ property
    def front_camera(self) -> Camera:
        return self.__front_camera

    @ front_camera.setter
    def front_camera(self, front_camera: Camera):
        if type(front_camera).__name__ == "Camera":
            self.__front_camera = front_camera
        else:
            raise TypeError(
                "camera must be a Camera, but is {}".format(type(front_camera)))

    @ property
    def side_camera(self) -> Camera:
        return self.__side_camera

    @ side_camera.setter
    def side_camera(self, side_camera: Camera):
        if type(side_camera).__name__ == "Camera":
            self.__side_camera = side_camera
        else:
            raise TypeError(
                "camera must be a Camera, but is {}".format(type(side_camera)))

    @ property
    def objects(self) -> list[Object]:
        return self.__objects

    @ objects.setter
    def objects(self, objects: list[Object]):
        if type(objects).__name__ == "list":
            self.__objects = objects
        else:
            raise TypeError(
                "objects must be a list, but is {}".format(type(objects)))

    @ property
    def selected_object(self) -> Object:
        return self.__selected_object

    @ selected_object.setter
    def selected_object(self, selected_object: Object):
        if type(selected_object).__name__ == "Object" or selected_object == None:
            self.__selected_object = selected_object
        else:
            raise TypeError(
                "selected_object must be a Object, but is {}".format(type(selected_object)))

    def addObject(self, object: Object) -> None:
        """
        This method add a object to the scene

        :param object(Object): The object to add

        :return: None
        """
        if type(object).__name__ != "Object":
            raise TypeError(
                "object must be a Object, but is {}".format(type(object)))

        self._draw(object)

        # append the object to the list of objects
        self.__objects.append(object)

    def removeObject(self, object_id: str) -> None:
        """
        This method remove a object from the scene

        :param object_id(str): The id of the object to remove

        :return: None
        """

        if type(object_id).__name__ != "str":
            raise TypeError(
                "object_id must be a str, but is {}".format(type(object_id)))
        elif object_id == "":
            raise ValueError("object_id must not be empty")

        # variable to check if the object was found
        found = False

        # TODO: add the debug message that contains info about the object removed

        for object in self.__objects:
            if object.id == object_id:
                found = True
                self.__objects.remove(object)
                del object
                break

        if not found:
            raise ValueError("object with id {} not found".format(object_id))

    def getObject(self, object_id: str) -> Object:
        """
        This method get a object from the scene

        :param object_id(str): The id of the object to get

        :return: The object
        """
        if type(object_id).__name__ != "str":
            raise TypeError(
                "object_id must be a str, but is {}".format(type(object_id)))
        elif object_id == "":
            raise ValueError("object_id must not be empty")

        # variable to check if the object was found
        found = False

        # TODO: add the debug message that contains info about the object found

        for object in self.__objects:
            if object.id == object_id:
                found = True
                return object

        if not found:
            raise ValueError("object with id {} not found".format(object_id))

    def saveScene(self, file_path: str, file_name: str = 'letter to comrade.cmrd') -> None:
        pass

    def loadScene(self, file_path: str, file_name: str = 'letter to comrade.cmrd') -> None:
        pass

    def changeCameraSettings(self, param_name: str, param_value: float | int) -> None:
        if type(param_name).__name__ != "str":
            raise TypeError(
                "param_name must be a str, but is {}".format(type(param_name)))
        elif param_name == "":
            raise ValueError("param_name must not be empty")
        elif type(param_value).__name__ != "int" and type(param_value).__name__ != "float":
            raise TypeError(
                "param_value must be a int or float, but is {}".format(type(param_value)))
        # the following elifs are for the camera settings

        # TODO: add more camera settings. Like disable wire frames, color, shading, etc.
        # TODO: add the debug message that contains info about the camera settings changed

        # x, y, z are the coordinates of the camera (VRP)
        # angle is the angle of the camera (VPN)
        # fov is the field of view of the camera

        # we don't make a 3D cut in this project so we don't need the near and far planes
        # near is the near plane of the camera
        # far is the far plane of the camera
        if param_name == "x" or param_name == "y" or param_name == "z":
            self.__perspective_camera.vrp = self.__perspective_camera.vrp._replace(
                param_name=param_name, param_value=param_value)
        elif param_name == "angle":
            self.__perspective_camera.angle = param_value
        elif param_name == "near":
            self.__perspective_camera.near = param_value
        elif param_name == "far":
            self.__perspective_camera.far = param_value
        else:
            raise ValueError("param name {} not found".format(param_name))

    def changeObjectSettings(self, object_id: str, param_name: str, param_value: float | int) -> None:

        if type(object_id).__name__ != "str":
            raise TypeError(
                "object_id must be a str, but is {}".format(type(object_id)))
        elif object_id == "":
            raise ValueError("object_id must not be empty")
        elif type(param_name).__name__ != "str":
            raise TypeError(
                "param_name must be a str, but is {}".format(type(param_name)))
        elif param_name == "":
            raise ValueError("param_name must not be empty")
        elif type(param_value).__name__ != "int" and type(param_value).__name__ != "float":
            raise TypeError(
                "param_value must be a int or float, but is {}".format(type(param_value)))
        else:
            object_ref = self.getObject(object_id)

            # TODO: add more object settings. Like disable wire frames, color, shading, etc.
            # TODO: add the debug message that contains info about the object settings changed
            if param_name == "rotation":
                # apply rotation in the object
                object_ref._rotate(param_value, 'y')
            elif param_name == "translation":
                # apply translation in the object
                object_ref._translate(param_value, 'y')
            elif param_name == "scale":
                # apply scale in the object
                object_ref._scale(param_value, 'y')
            elif param_name == "shear":
                # apply shear in the object
                object_ref._shear(param_value, 'y')
            else:
                raise ValueError("param name {} not found".format(param_name))

    def select_object(self, x: int | float, y: int | float, canvas_name: str):
        """
        This method select a object from the scene

        :param x(int | float): The x coordinate of the click
        :param y(int | float): The y coordinate of the click

        :return: None
        """

        # expand the click to get objects near the click
        radius_click = 50
        found = False

        for object in self.__objects:
            # check if the object is near the click
            if self.is_near(x, y, radius_click, canvas_name, object):
                # if the object is near the click, select the object
                self.selected_object = object
                found = True
                break
        # if no object was found, deselect the object
        if not found:
            self.selected_object = None

    def is_near(self, x: int | float, y: int | float, radius_click: int | float, canvas_name: str, object: Object):
        """
        This method check if the scene is near the click

        :param x(int | float): The x coordinate of the click
        :param y(int | float): The y coordinate of the click
        :param radius_click(int | float): The radius of the click
        :param canvas_name(str): The name of the canvas

        :return: True if the scene is near the click, False otherwise
        """

        if canvas_name == 'side':
            for vertex in object.vertexes_object:
                # check if the vertex is near the click
                distance = ((x - vertex.z_side) ** 2 +
                            (y - vertex.y_side) ** 2) ** 0.5
                if distance <= radius_click:
                    return True
            return False
        elif canvas_name == 'frontal':
            for vertex in object.vertexes_object:
                # check if the vertex is near the click
                distance = ((x - vertex.x_front) ** 2 +
                            (y - vertex.y_front) ** 2) ** 0.5
                if distance <= radius_click:
                    return True
            return False
        elif canvas_name == 'top':
            for vertex in object.vertexes_object:
                # check if the vertex is near the click
                distance = ((x - vertex.x_top) ** 2 +
                            (y - vertex.z_top) ** 2) ** 0.5
                if distance <= radius_click:
                    return True
            return False

    def redraw_object(self) -> None:
        """
        This method redraw the selected object

        :return: None
        """

        if self.selected_object is None:
            raise ValueError("selected_object is None")

        # apply the pipeline in the object
        self._draw(self.selected_object)

    def _draw(self, object: Object) -> None:
        """
        This method draw the object

        :param object(Object): The object to draw

        :return: None
        """

        # get the matrix to convert from SRU to SRT in the views
        perspective_mSruSrtMatrix = self.perspective_camera.MSruSrtMatrix
        top_mSruSrtMatrix = self.top_camera.MSruSrtMatrix
        front_mSruSrtMatrix = self.front_camera.MSruSrtMatrix
        side_mSruSrtMatrix = self.side_camera.MSruSrtMatrix

        for vertices in object.vertexes_object:
            aux = matrixMultiplication(
                perspective_mSruSrtMatrix, [[vertices.x], [vertices.y], [vertices.z], [vertices.h]])

            vertices.x_screen = aux[0][0]
            vertices.y_screen = aux[1][0]
            vertices.z_screen = aux[2][0]
            vertices.h_screen = aux[3][0]

            aux = None
            aux = matrixMultiplication(
                top_mSruSrtMatrix, [[vertices.x], [vertices.y], [vertices.z], [vertices.h]])

            vertices.x_top = aux[0][0]
            vertices.z_top = aux[1][0]
            # this is 0 because we can ignore the y coordinate in top view
            vertices.y_top = aux[2][0]
            vertices.h_top = aux[3][0]

            aux = None
            aux = matrixMultiplication(
                front_mSruSrtMatrix, [[vertices.x], [vertices.y], [vertices.z], [vertices.h]])

            vertices.x_front = aux[0][0]
            vertices.y_front = aux[1][0]
            # we can ignore the z coordinate in front view
            vertices.z_front = aux[2][0]
            vertices.h_front = aux[3][0]

            aux = None
            aux = matrixMultiplication(
                side_mSruSrtMatrix, [[vertices.x], [vertices.y], [vertices.z], [vertices.h]])

            vertices.z_side = aux[0][0]
            vertices.y_side = aux[1][0]
            # we can ignore the x coordinate in side view
            vertices.x_side = aux[2][0]
            vertices.h_side = aux[3][0]

            # normalize the vertex by the homogeneous coordinate
            normalize_by_homogeneous_coordinate(vertices)

        for face in object.face_objects:
            face.visibility_test(self.perspective_camera.vrp)

    def update(self) -> None:
        """
        This method update the scene

        :return: None
        """

        # apply the pipeline in the objects
        for object in self.objects:
            self._draw(object)
