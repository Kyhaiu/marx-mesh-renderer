from core.camera import Camera
from models.scene import Scene
from models.vertex import Vertex
from objects.pyramid import pyramid
from view import gui as win
import sys

from objects.char_0 import zero
from objects.char_1 import one
from objects.char_2 import two
from objects.char_3 import three
from objects.char_4 import four
from objects.char_5 import five
from objects.char_6 import six
from objects.char_7 import seven
from objects.char_8 import eight
from objects.char_9 import nine
from objects.char_A import A
from objects.char_B import B
from objects.char_C import C
from objects.char_D import D
from objects.char_E import E
from objects.char_F import F
from objects.char_G import G
from objects.char_H import H
from objects.char_I import I
from objects.char_J import J
from objects.char_K import K
from objects.char_L import L
# from objects.char_M import M
# from objects.char_N import N
# from objects.char_O import O
# from objects.char_P import P
# from objects.char_Q import Q
# from objects.char_R import R
# from objects.char_S import S
# from objects.char_T import T
# from objects.char_U import U
# from objects.char_V import V
# from objects.char_W import W
# from objects.char_X import X
# from objects.char_Y import Y
# from objects.char_Z import Z


def main():
    root = win.tk.Tk()
    scene = Scene()
    window = win.GUI(450, 450, root)

    # scene.addObject(pyramid)
    scene.addObject(L)

    window.make_scene(scene)

    root.mainloop()


if __name__ == '__main__':
    main()
