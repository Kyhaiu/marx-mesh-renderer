from typing import Any
import tkinter as tk

from models.halfedge import HalfEdge
from models.vertex import Vertex


class GUI:
    def __init__(self, width: int, height: int, root: tk.Tk):
        self.width = width
        self.height = height
        self.root = root

        self.root.title("The L Plotter")

        self.frontal_canvas: tk.Frame = self._create_canvas(
            "Frontal view", 0, 0)
        self.top_canvas: tk.Frame = self._create_canvas("Top view", 0, 1)
        self.side_candas: tk.Frame = self._create_canvas("Side view", 1, 0)
        self.isometric_canvas: tk.Frame = self._create_canvas(
            "Isometric view", 1, 1)

    def _create_canvas(self, label_text: str, row: int, column: int) -> tk.Frame:
        """
        This is a private method to create a canvas with the given label text.

        :param label_text: The text to display on the canvas
        :param row: The row to place the canvas in
        :param column: The column to place the canvas in

        :return: The frame containing the canvas
        """
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=self.width*0.75,
                           height=self.height*0.75, bg='black')
        canvas.pack()
        label = tk.Label(frame, text=label_text)
        label.pack()
        frame.grid(row=row, column=column)

        return frame

    def getCanvasReference(self, canvas_name: str) -> tk.Canvas:
        """
        This method returns the reference to the canvas with the given name.

        :param canvas_name: The name of the canvas to return

        :return: The reference to the canvas
        """
        if canvas_name == "frontal":
            return self.frontal_canvas.winfo_children()[0]
        elif canvas_name == "top":
            return self.top_canvas.winfo_children()[0]
        elif canvas_name == "side":
            return self.side_canvas.winfo_children()[0]
        elif canvas_name == "isometric":
            return self.isometric_canvas.winfo_children()[0]
        else:
            raise ValueError("Invalid canvas name: {}".format(canvas_name))

    def plot_stuffs_on_canvas(self, canvas_name: str, half_edge: 'HalfEdge', vertices: list[Vertex] = None, size_dot: int = 4, color: str = 'white') -> None:
        """
        This method plots the given half-edge structure on the given canvas.

        :param canvas_name: The name of the canvas to plot on
        :param half_edge: The half-edge structure to plot
        :param vertices: The vertices to plot
        :param size_dot: The size of the dot to plot
        :param color: The color of the dot to plot

        :return: None
        """
        canvas = self.getCanvasReference(canvas_name)

        if vertices is not None:
            for vertex in vertices:
                canvas.create_oval(vertex.x-size_dot, vertex.y-size_dot,
                                   vertex.x+size_dot, vertex.y+size_dot, fill=color)
