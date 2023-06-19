from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.halfedge import HalfEdge


class Vertex:

    def __init__(self, x: float, y: float, z: float, h: float = 1.0, half_edge: 'HalfEdge' = None, id: str | int = None):
        # x, y, z, h are the coordinates of the vertex
        # half_edge is the half_edge that starts from this vertex
        # id is the id of the vertex

        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.half_edge = half_edge
        self.id = id

        # x_screen, y_screen, z_screen, h_screen are the coordinates of the vertex in the screen
        self.x_screen = x
        self.y_screen = y
        self.z_screen = z
        self.h_screen = h

    def __repr__(self) -> str:
        return "{} :({:.3f}, {:.3f}, {:.3f}, {:.3f})".format(self.id, self.x, self.y, self.z, self.h)

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        if type(x) is float or type(x) is int:
            self.__x = x
        else:
            raise TypeError(
                "x must be a float or int, but is {}".format(type(x)))

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        if type(y) is float or type(y) is int:
            self.__y = y
        else:
            raise TypeError(
                "y must be a float or int, but is {}".format(type(y)))

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float):
        if type(z) is float or type(z) is int:
            self.__z = z
        else:
            raise TypeError(
                "z must be a float or int, but is {}".format(type(z)))

    @property
    def h(self) -> float:
        return self.__h

    @h.setter
    def h(self, h: float):
        if type(h) is float or type(h) is int:
            self.__h = h
        else:
            raise TypeError(
                "h must be a float or int, but is {}".format(type(h)))

    @property
    def x_screen(self) -> float:
        return self.__x_screen

    @x_screen.setter
    def x_screen(self, x_screen: float):
        if type(x_screen) is float or type(x_screen) is int or x_screen is None:
            self.__x_screen = x_screen
        else:
            raise TypeError(
                "x_screen must be a float, int or None, but is {}".format(type(x_screen)))

    @property
    def y_screen(self) -> float:
        return self.__y_screen

    @y_screen.setter
    def y_screen(self, y_screen: float):
        if type(y_screen) is float or type(y_screen) is int or y_screen is None:
            self.__y_screen = y_screen
        else:
            raise TypeError(
                "y_screen must be a float, int or None, but is {}".format(type(y_screen)))

    @property
    def z_screen(self) -> float:
        return self.__z_screen

    @z_screen.setter
    def z_screen(self, z_screen: float):
        if type(z_screen) is float or type(z_screen) is int or z_screen is None:
            self.__z_screen = z_screen
        else:
            raise TypeError(
                "z_screen must be a float, int or None, but is {}".format(type(z_screen)))

    @property
    def half_edge(self) -> 'HalfEdge':
        return self.__half_edge

    @half_edge.setter
    def half_edge(self, half_edge: 'HalfEdge'):
        if type(half_edge).__name__ == 'HalfEdge' or half_edge is None:
            self.__half_edge = half_edge
        else:
            raise TypeError(
                "half_edge must be a HalfEdge or None, but is {}".format(type(half_edge)))

    @property
    def id(self) -> str | int:
        return self.__id

    @id.setter
    def id(self, id: str | int):
        if type(id) is str or type(id) is int or id is None:
            self.__id = id
        else:
            raise TypeError(
                "id must be a str, int or None, but is {}".format(type(id)))

    def _replace(self, param_name: str, param_value: float | int | 'HalfEdge', screen_coordinates: bool = False) -> None:
        """
        This function is used to replace the value of a parameter of the vertex.

        :param param_name: The name of the parameter to be replaced.
        :param param_value: The new value of the parameter.

        :raises TypeError: If param_name is not a str or param_value is not a HalfEdge, float or int.
        :raises ValueError: If param_name is not 'x', 'y', 'z', 'h' or 'half_edge'.
        """
        if screen_coordinates:

            if type(param_name) is str and (type(param_value).__name__ == 'HalfEdge' or type(param_value) is float or type(param_value) is int):
                if param_name == 'x':
                    self.x = param_value
                elif param_name == 'y':
                    self.y = param_value
                elif param_name == 'z':
                    self.z = param_value
                elif param_name == 'h':
                    self.h = param_value
                elif param_name == 'half_edge':
                    self.half_edge = param_value
                else:
                    raise ValueError(
                        "param_name must be 'x', 'y', 'z', 'h' or 'half_edge', but is {}".format(param_name))
            else:
                raise TypeError(
                    "param_name must be a str and param_value must be a HalfEdge, float or int, but are {} and {}".format(type(param_name), type(param_value)))
        else:
            if type(param_name) is str and (type(param_value) is float or type(param_value) is int):
                if param_name == 'x':
                    self.x_screen = param_value
                elif param_name == 'y':
                    self.y_screen = param_value
                elif param_name == 'z':
                    self.z_screen = param_value
                elif param_name == 'h':
                    self.h_screen = param_value
                else:
                    raise ValueError(
                        "param_name must be 'x', 'y', 'z' or 'h', but is {}".format(param_name))
            else:
                raise TypeError(
                    "param_name must be a str and param_value must be a float or int, but are {} and {}".format(type(param_name), type(param_value)))
