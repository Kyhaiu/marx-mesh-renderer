from models.scene import Scene
from view import gui as win


def main():
    root = win.tk.Tk()
    scene = Scene()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window = win.GUI(800, 475, root)

    window.make_scene(scene)

    root.mainloop()


if __name__ == '__main__':
    main()
