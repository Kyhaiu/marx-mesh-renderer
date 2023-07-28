from objects.char_0 import faces as faces_0, vertices as vertices_0
from objects.char_1 import faces as faces_1, vertices as vertices_1
from objects.char_2 import faces as faces_2, vertices as vertices_2
from objects.char_3 import faces as faces_3, vertices as vertices_3
from objects.char_4 import faces as faces_4, vertices as vertices_4
from objects.char_5 import faces as faces_5, vertices as vertices_5
from objects.char_6 import faces as faces_6, vertices as vertices_6
from objects.char_7 import faces as faces_7, vertices as vertices_7
from objects.char_8 import faces as faces_8, vertices as vertices_8
from objects.char_9 import faces as faces_9, vertices as vertices_9
from objects.char_A import faces as faces_A, vertices as vertices_A
from objects.char_B import faces as faces_B, vertices as vertices_B
from objects.char_C import faces as faces_C, vertices as vertices_C
from objects.char_D import faces as faces_D, vertices as vertices_D
from objects.char_E import faces as faces_E, vertices as vertices_E
from objects.char_F import faces as faces_F, vertices as vertices_F
from objects.char_G import faces as faces_G, vertices as vertices_G
from objects.char_H import faces as faces_H, vertices as vertices_H
from objects.char_I import faces as faces_I, vertices as vertices_I
from objects.char_J import faces as faces_J, vertices as vertices_J
from objects.char_K import faces as faces_K, vertices as vertices_K
from objects.char_L import faces as faces_L, vertices as vertices_L
from objects.char_M import faces as faces_M, vertices as vertices_M
from objects.char_N import faces as faces_N, vertices as vertices_N
from objects.char_O import faces as faces_O, vertices as vertices_O
from objects.char_P import faces as faces_P, vertices as vertices_P
from objects.char_Q import faces as faces_Q, vertices as vertices_Q
from objects.char_R import faces as faces_R, vertices as vertices_R
from objects.char_S import faces as faces_S, vertices as vertices_S
from objects.char_T import faces as faces_T, vertices as vertices_T
from objects.char_U import faces as faces_U, vertices as vertices_U
from objects.char_V import faces as faces_V, vertices as vertices_V
from objects.char_W import faces as faces_W, vertices as vertices_W
from objects.char_X import faces as faces_X, vertices as vertices_X
from objects.char_Y import faces as faces_Y, vertices as vertices_Y
from objects.char_Z import faces as faces_Z, vertices as vertices_Z
from objects.debug import make_debug, faces as faces_debug, vertices as vertices_debug

from models.object import Object
from models.vertex import Vertex


def the_space_bar(vertices: list[Vertex]):
    """
    add some space between letters

    :param vertices: the vertices of the letter

    :return: the vertices of the letter with space
    """

    # 1 u. in sru
    padding = 1
    spaced_letter = []
    for vertex in vertices:
        vertex.x += padding
        spaced_letter.append(vertex)

    return spaced_letter


@staticmethod
def get_letter(_letter: str, need_space: bool) -> Object:
    """
    Returns the letter object

    :param _letter: the letter to be returned
    :param need_space: if the letter needs space between it and the next letter

    :return: the letter object (spaced or not)
    """

    letter = _letter.lower()

    if letter == '.':
        return make_debug()
        # return Object(vertices_debug, faces_debug)

    if not letter.isalnum():
        raise ValueError("Letter must be a char between a-z0-9")

    if letter == 'a':
        return Object(vertices_A if not need_space else the_space_bar(vertices_A), faces_A)
    elif letter == 'b':
        return Object(vertices_B if not need_space else the_space_bar(vertices_B), faces_B)
    elif letter == 'c':
        return Object(vertices_C if not need_space else the_space_bar(vertices_C), faces_C)
    elif letter == 'd':
        return Object(vertices_D if not need_space else the_space_bar(vertices_D), faces_D)
    elif letter == 'e':
        return Object(vertices_E if not need_space else the_space_bar(vertices_E), faces_E)
    elif letter == 'f':
        return Object(vertices_F if not need_space else the_space_bar(vertices_F), faces_F)
    elif letter == 'g':
        return Object(vertices_G if not need_space else the_space_bar(vertices_G), faces_G)
    elif letter == 'h':
        return Object(vertices_H if not need_space else the_space_bar(vertices_H), faces_H)
    elif letter == 'i':
        return Object(vertices_I if not need_space else the_space_bar(vertices_I), faces_I)
    elif letter == 'j':
        return Object(vertices_J if not need_space else the_space_bar(vertices_J), faces_J)
    elif letter == 'k':
        return Object(vertices_K if not need_space else the_space_bar(vertices_K), faces_J)
    elif letter == 'l':
        return Object(vertices_L if not need_space else the_space_bar(vertices_L), faces_L)
    elif letter == 'm':
        return Object(vertices_M if not need_space else the_space_bar(vertices_M), faces_M)
    elif letter == 'n':
        return Object(vertices_N if not need_space else the_space_bar(vertices_N), faces_N)
    elif letter == 'o':
        return Object(vertices_O if not need_space else the_space_bar(vertices_O), faces_O)
    elif letter == 'p':
        return Object(vertices_P if not need_space else the_space_bar(vertices_P), faces_P)
    elif letter == 'q':
        return Object(vertices_Q if not need_space else the_space_bar(vertices_Q), faces_Q)
    elif letter == 'r':
        return Object(vertices_R if not need_space else the_space_bar(vertices_R), faces_R)
    elif letter == 's':
        return Object(vertices_S if not need_space else the_space_bar(vertices_S), faces_S)
    elif letter == 't':
        return Object(vertices_T if not need_space else the_space_bar(vertices_T), faces_T)
    elif letter == 'u':
        return Object(vertices_U if not need_space else the_space_bar(vertices_U), faces_U)
    elif letter == 'v':
        return Object(vertices_V if not need_space else the_space_bar(vertices_V), faces_V)
    elif letter == 'w':
        return Object(vertices_W if not need_space else the_space_bar(vertices_W), faces_W)
    elif letter == 'x':
        return Object(vertices_X if not need_space else the_space_bar(vertices_X), faces_X)
    elif letter == 'y':
        return Object(vertices_Y if not need_space else the_space_bar(vertices_Y), faces_Y)
    elif letter == 'z':
        return Object(vertices_Z if not need_space else the_space_bar(vertices_Z), faces_Z)
    elif letter == '0':
        return Object(vertices_0 if not need_space else the_space_bar(vertices_0), faces_0)
    elif letter == '1':
        return Object(vertices_1 if not need_space else the_space_bar(vertices_1), faces_1)
    elif letter == '2':
        return Object(vertices_2 if not need_space else the_space_bar(vertices_2), faces_2)
    elif letter == '3':
        return Object(vertices_3 if not need_space else the_space_bar(vertices_3), faces_3)
    elif letter == '4':
        return Object(vertices_4 if not need_space else the_space_bar(vertices_4), faces_4)
    elif letter == '5':
        return Object(vertices_5 if not need_space else the_space_bar(vertices_5), faces_5)
    elif letter == '6':
        return Object(vertices_6 if not need_space else the_space_bar(vertices_6), faces_6)
    elif letter == '7':
        return Object(vertices_7 if not need_space else the_space_bar(vertices_7), faces_7)
    elif letter == '8':
        return Object(vertices_8 if not need_space else the_space_bar(vertices_8), faces_8)
    elif letter == '9':
        return Object(vertices_9 if not need_space else the_space_bar(vertices_9), faces_9)
    else:
        raise ValueError("Letter must be a char between a-z0-9")
