"""Пример 1 из методички по работе с tkinter."""

from tkinter import *

def run_example_1() -> None:
    """Запускает демонстрационный пример 1 из методички."""
    root = Tk()
    root.title("Пример 1 — tkinter")
    
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()

    ball = c.create_oval(0, 100, 40, 140, fill='green')

    def motion() -> None:
        c.move(ball, 1, 0)
        if c.coords(ball)[2] < 300:
            root.after(10, motion)

    motion()
    root.mainloop()

if __name__ == "__main__":
    run_example_1()
