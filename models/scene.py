import logging
from core.camera import Camera
from models.object import Object
from models.vertex import Vertex
from utils.geometric_transformation import translation
from utils.pipeline import normalize_by_homogeneous_coordinate
from utils.vectors_operations import matrixMultiplication


class Scene:
    def __init__(self, camera: Camera = None, objects: list[Object] = []):

        if camera is None:
            self.camera = Camera()

        else:
            self.camera = camera

        self.objects = objects
        self.selected_object = None

    def __str__(self) -> str:
        msg = "Scene(\n"
        msg += "\tcamera: {}\n".format(self.camera)
        msg += "\tobjects: [\n"
        for object in self.objects:
            msg += "\t\t{}\n".format(object)
        msg += "\t]\n"
        msg += "\tselected_object: {}\n".format(self.selected_object)
        msg += ")"
        return msg

    @property
    def camera(self) -> Camera:
        return self.__camera

    @camera.setter
    def camera(self, camera: Camera):
        if type(camera).__name__ == "Camera":
            self.__camera = camera
        else:
            raise TypeError(
                "camera must be a Camera, but is {}".format(type(camera)))

    @property
    def objects(self) -> list[Object]:
        return self.__objects

    @objects.setter
    def objects(self, objects: list[Object]):
        if type(objects).__name__ == "list":
            self.__objects = objects
        else:
            raise TypeError(
                "objects must be a list, but is {}".format(type(objects)))

    @property
    def selected_object(self) -> Object:
        return self.__selected_object

    @selected_object.setter
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

        # apply the pipeline in the object

        # get the matrix to convert from SRU to SRT
        mSruSrtMatrix = self.camera.MSruSrtMatrix

        for vertex in object.vertexes_object:
            # convert the vertex from SRU to SRT
            aux = matrixMultiplication(
                mSruSrtMatrix, [[vertex.x_screen], [vertex.y_screen], [vertex.z_screen], [vertex.h_screen]])

            vertex.x_screen = aux[0][0]
            vertex.y_screen = aux[1][0]
            vertex.z_screen = aux[2][0]
            vertex.h_screen = aux[3][0]

            normalize_by_homogeneous_coordinate(vertex)

        for face in object.face_objects:
            face.visibility_test(self.camera.vrp)

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
            self.__camera.vrp = self.__camera.vrp._replace(
                param_name=param_name, param_value=param_value)
        elif param_name == "angle":
            self.__camera.angle = param_value
        elif param_name == "near":
            self.__camera.near = param_value
        elif param_name == "far":
            self.__camera.far = param_value
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
