import tkinter as tk
from src.models.animation_model import CircleAnimationModel

class ControlsHandler:
    def __init__(self, root: tk.Tk, model: CircleAnimationModel):
        root.bind("<Up>", lambda e: setattr(model, 'angular_speed', min(0.2, model.angular_speed + 0.005)))
        root.bind("<Down>", lambda e: setattr(model, 'angular_speed', max(0.005, model.angular_speed - 0.005)))
        root.bind("<space>", lambda e: model.toggle_direction())
        root.bind("<p>", lambda e: model.toggle_pause())
        root.bind("<r>", lambda e: model.reset())
