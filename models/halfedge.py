from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.face import Face
    from models.vertex import Vertex


class HalfEdge:
    def __init__(self, origin: Vertex = None, twin: 'HalfEdge' = None, prev: 'HalfEdge' = None, next: 'HalfEdge' = None, face: Face = None, id: str | int = None):
        self.origin = origin
        self.twin = twin
        self.prev = prev
        self.next = next
        self.face = face
        self.id = id

    def __repr__(self) -> str:
        repr = "HalfEdge("
        repr += "id={}, ".format(self.id)
        repr += "origin={}, ".format(self.origin.id)
        repr += "twin={}, ".format(self.twin.id)
        repr += "prev={}, ".format(self.prev.id)
        repr += "next={}, ".format(self.next.id)
        repr += "face={}".format(self.face.id)
        repr += ")"
        return repr

    @property
    def origin(self) -> Vertex:
        return self.__origin

    @origin.setter
    def origin(self, origin: Vertex):
        if type(origin).__name__ == "Vertex" or origin is None:
            self.__origin = origin
        else:
            raise TypeError(
                "origin must be a Vertex or None, but is {}".format(type(origin)))

    @property
    def twin(self) -> 'HalfEdge':
        return self.__twin

    @twin.setter
    def twin(self, twin: 'HalfEdge'):
        if type(twin).__name__ == "HalfEdge" or twin is None:
            self.__twin = twin
        else:
            raise TypeError(
                "twin must be a HalfEdge or None, but is {}".format(type(twin)))

    @property
    def prev(self) -> 'HalfEdge':
        return self.__prev

    @prev.setter
    def prev(self, prev: 'HalfEdge'):
        if type(prev).__name__ == "HalfEdge" or prev is None:
            self.__prev = prev
        else:
            raise TypeError(
                "prev must be a HalfEdge or None, but is {}".format(type(prev)))

    @property
    def next(self) -> 'HalfEdge':
        return self.__next

    @next.setter
    def next(self, next: 'HalfEdge'):
        if type(next).__name__ == "HalfEdge" or next is None:
            self.__next = next
        else:
            raise TypeError(
                "next must be a HalfEdge or None, but is {}".format(type(next)))

    @property
    def face(self) -> Face:
        return self.__face

    @face.setter
    def face(self, face: Face):
        if type(face).__name__ == "Face" or face is None:
            self.__face = face
        else:
            raise TypeError(
                "face must be a Face or None, but is {}".format(type(face)))

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
