from models.scene import Scene
from objects.char_0 import zero
from objects.pyramid import pyramid
from view import gui as win
import sys


def main():
    root = win.tk.Tk()
    window = win.GUI(500, 500, root)

    scene = Scene()

    scene.addObject(pyramid)

    window.make_scene(scene)

    root.mainloop()


if __name__ == '__main__':
    main()
