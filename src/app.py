import tkinter as tk
from src.models.animation_model import CircleAnimationModel
from src.renderers.renderer import CircleRenderer
from src.widgets.controls import ControlsHandler

class AnimationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Работа 3.0 — Движение точки по окружности")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.model = CircleAnimationModel()
        self.renderer = CircleRenderer(self.canvas, self.model)
        self.controls = ControlsHandler(self.root, self.model)

    def animate(self):
        self.model.update()
        self.renderer.render()
        self.root.after(16, self.animate)

    def run(self):
        self.animate()
        self.root.mainloop()
