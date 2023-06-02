from __future__ import annotations

from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from models.halfedge import HalfEdge


class Vertex:

    def __init__(self, x: float, y: float, z: float, h: float = 1.0, half_edge: 'HalfEdge' = None, id: str | int = None):
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.half_edge = half_edge
        self.id = id

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
