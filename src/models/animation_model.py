import math
from typing import Tuple

class CircleAnimationModel:
    def __init__(self, cx=300.0, cy=300.0, r=200.0, speed=0.03, direction=1):
        self.center_x, self.center_y, self.radius = cx, cy, r
        self.angular_speed, self.direction = speed, direction
        self.angle = 0.0
        self.is_paused = False

    def update(self):
        if not self.is_paused:
            self.angle += self.angular_speed * self.direction
            self.angle %= 2 * math.pi

    def get_point_coords(self) -> Tuple[float, float]:
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)
        return x, y

    def toggle_direction(self): self.direction *= -1
    def toggle_pause(self): self.is_paused = not self.is_paused
    def reset(self): self.angle = 0.0
