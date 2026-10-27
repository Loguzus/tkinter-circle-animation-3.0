import unittest
from src.models.animation_model import CircleAnimationModel

class TestCircleAnimationModel(unittest.TestCase):
    def test_initial_coordinates(self):
        model = CircleAnimationModel(center_x=300, center_y=300, radius=200)
        x, y = model.get_point_coords()
        self.assertAlmostEqual(x, 500.0)
        self.assertAlmostEqual(y, 300.0)

if __name__ == "__main__":
    unittest.main()
