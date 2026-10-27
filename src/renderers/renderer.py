import tkinter as tk
from src.models.animation_model import CircleAnimationModel

class CircleRenderer:
    def __init__(self, canvas: tk.Canvas, model: CircleAnimationModel):
        self.canvas, self.model = canvas, model
        cx, cy, r = self.model.center_x, self.model.center_y, self.model.radius
        self.orbit = self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#334155", width=2)
        px, py = self.model.get_point_coords()
        self.point = self.canvas.create_oval(px - 8, py - 8, px + 8, py + 8, fill="#ef4444")
        self.info = self.canvas.create_text(300, 25, text="", font=("Arial", 10))

    def render(self):
        px, py = self.model.get_point_coords()
        self.canvas.coords(self.point, px - 8, py - 8, px + 8, py + 8)
        self.canvas.itemconfig(self.info, text=f"Скорость: {self.model.angular_speed:.3f}")
