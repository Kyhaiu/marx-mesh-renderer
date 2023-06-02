from objects.test import VERT_A, VERT_B, VERT_C, VERT_D, VERT_E
from view import gui as win


def main():
    root = win.tk.Tk()
    window = win.GUI(500, 500, root)

    vertices = [VERT_A, VERT_B, VERT_C, VERT_D, VERT_E]
    window.plot_stuffs_on_canvas("frontal", None, vertices)

    root.mainloop()


if __name__ == '__main__':
    main()
