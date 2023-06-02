from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.halfedge import HalfEdge


class Face:

    def __init__(self, half_edge: 'HalfEdge' = None, id: str | int = None):
        self.half_edge = half_edge
        self.id = id

    def __repr__(self) -> str:
        repr = "Face(\n\n"
        repr += "\tid: {}\n".format(self.id)
        repr += "\thalf_edge: {}\n".format(self.half_edge.id)
        repr += "\n)\n"
        return repr

    @property
    def half_edge(self) -> 'HalfEdge':
        return self.__half_edge

    @half_edge.setter
    def half_edge(self, half_edge: 'HalfEdge'):
        if type(half_edge).__name__ == "HalfEdge" or half_edge is None:
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
