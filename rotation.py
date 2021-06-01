import unittest
import main
from main import Color
import numpy


# front, back, left, right, upper, down
#

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #    self.assertEqual(True, False)
    def test_rotation_front(self):
        cube = main.Cube()
        cube.move(main.Direction.FRONT)

        cube_dict = main.Cube.from_dict({
            "front": [Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE],
            "back": [Color.RED, Color.RED, Color.RED, Color.RED],
            "left": [Color.GREEN, Color.WHITE, Color.GREEN, Color.WHITE],
            "upper": [Color.YELLOW, Color.YELLOW, Color.GREEN, Color.GREEN],
            "down": [Color.BLUE, Color.BLUE, Color.WHITE, Color.WHITE],
            "right": [Color.YELLOW, Color.BLUE, Color.YELLOW, Color.BLUE]
        })
        print(cube.unfold());
        self.assert_(cube == cube_dict)


if __name__ == '__main__':
    unittest.main()
