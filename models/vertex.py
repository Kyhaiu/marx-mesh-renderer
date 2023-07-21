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

        # x_top, y_top, z_top, h_top are the coordinates of the vertex in the top view
        self.x_top = x
        self.y_top = y
        self.z_top = z
        self.h_top = h

        # x_front, y_front, z_front, h_front are the coordinates of the vertex in the front view
        self.x_front = x
        self.y_front = y
        self.z_front = z
        self.h_front = h

        # x_side, y_side, z_side, h_side are the coordinates of the vertex in the side view
        self.x_side = x
        self.y_side = y
        self.z_side = z
        self.h_side = h

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
    def h_screen(self) -> float:
        return self.__h_screen

    @h_screen.setter
    def h_screen(self, h_screen: float):
        if type(h_screen) is float or type(h_screen) is int or h_screen is None:
            self.__h_screen = h_screen
        else:
            raise TypeError(
                "h_screen must be a float, int or None, but is {}".format(type(h_screen)))

    @property
    def x_top(self) -> float:
        return self.__x_top

    @x_top.setter
    def x_top(self, x_top: float):
        if type(x_top) is float or type(x_top) is int or x_top is None:
            self.__x_top = x_top
        else:
            raise TypeError(
                "x_top must be a float, int or None, but is {}".format(type(x_top)))

    @property
    def y_top(self) -> float:
        return self.__y_top

    @y_top.setter
    def y_top(self, y_top: float):
        if type(y_top) is float or type(y_top) is int or y_top is None:
            self.__y_top = y_top
        else:
            raise TypeError(
                "y_top must be a float, int or None, but is {}".format(type(y_top)))

    @property
    def z_top(self) -> float:
        return self.__z_top

    @z_top.setter
    def z_top(self, z_top: float):
        if type(z_top) is float or type(z_top) is int or z_top is None:
            self.__z_top = z_top
        else:
            raise TypeError(
                "z_top must be a float, int or None, but is {}".format(type(z_top)))

    @property
    def h_top(self) -> float:
        return self.__h_top

    @h_top.setter
    def h_top(self, h_top: float):
        if type(h_top) is float or type(h_top) is int or h_top is None:
            self.__h_top = h_top
        else:
            raise TypeError(
                "h_top must be a float, int or None, but is {}".format(type(h_top)))

    @property
    def x_front(self) -> float:
        return self.__x_front

    @x_front.setter
    def x_front(self, x_front: float):
        if type(x_front) is float or type(x_front) is int or x_front is None:
            self.__x_front = x_front
        else:
            raise TypeError(
                "x_front must be a float, int or None, but is {}".format(type(x_front)))

    @property
    def y_front(self) -> float:
        return self.__y_front

    @y_front.setter
    def y_front(self, y_front: float):
        if type(y_front) is float or type(y_front) is int or y_front is None:
            self.__y_front = y_front
        else:
            raise TypeError(
                "y_front must be a float, int or None, but is {}".format(type(y_front)))

    @property
    def z_front(self) -> float:
        return self.__z_front

    @z_front.setter
    def z_front(self, z_front: float):
        if type(z_front) is float or type(z_front) is int or z_front is None:
            self.__z_front = z_front
        else:
            raise TypeError(
                "z_front must be a float, int or None, but is {}".format(type(z_front)))

    @property
    def h_front(self) -> float:
        return self.__h_front

    @h_front.setter
    def h_front(self, h_front: float):
        if type(h_front) is float or type(h_front) is int or h_front is None:
            self.__h_front = h_front
        else:
            raise TypeError(
                "h_front must be a float, int or None, but is {}".format(type(h_front)))

    @property
    def x_side(self) -> float:
        return self.__x_side

    @x_side.setter
    def x_side(self, x_side: float):
        if type(x_side) is float or type(x_side) is int or x_side is None:
            self.__x_side = x_side
        else:
            raise TypeError(
                "x_side must be a float, int or None, but is {}".format(type(x_side)))

    @property
    def y_side(self) -> float:
        return self.__y_side

    @y_side.setter
    def y_side(self, y_side: float):
        if type(y_side) is float or type(y_side) is int or y_side is None:
            self.__y_side = y_side
        else:
            raise TypeError(
                "y_side must be a float, int or None, but is {}".format(type(y_side)))

    @property
    def z_side(self) -> float:
        return self.__z_side

    @z_side.setter
    def z_side(self, z_side: float):
        if type(z_side) is float or type(z_side) is int or z_side is None:
            self.__z_side = z_side
        else:
            raise TypeError(
                "z_side must be a float, int or None, but is {}".format(type(z_side)))

    @property
    def h_side(self) -> float:
        return self.__h_side

    @h_side.setter
    def h_side(self, h_side: float):
        if type(h_side) is float or type(h_side) is int or h_side is None:
            self.__h_side = h_side
        else:
            raise TypeError(
                "h_side must be a float, int or None, but is {}".format(type(h_side)))

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
