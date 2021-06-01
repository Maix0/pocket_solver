import numpy
from enum import Enum


class Color(Enum):
    WHITE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    ORANGE = 4
    YELLOW = 5

    def code(self):
        if self == Color.WHITE:
            return "\x1b[1;37m"
        elif self == Color.RED:
            return "\x1b[1;31m"
        elif self == Color.GREEN:
            return "\x1b[1;32m"
        elif self == Color.BLUE:
            return "\x1b[1;34m"
        elif self == Color.ORANGE:
            return "\x1b[1;35m"
        elif self == Color.YELLOW:
            return "\x1b[1;93m"


class Direction(Enum):
    FRONT = F = "F"
    BACK = B = "B"
    RIGHT = R = "R"
    LEFT = L = "L"
    UPPER = U = "U"
    DOWN = D = "D"

    FRONT_INVERTED = F_I = "F'"
    BACK_INVERTED = B_I = "B'"
    RIGHT_INVERTED = R_I = "R'"
    LEFT_INVERTED = L_I = "L'"
    UPPER_INVERTED = U_I = "U'"
    DOWN_INVERTED = D_I = "D'"

    FRONT_DOUBLE = F_D = "F2"
    BACK_DOUBLE = B_D = "B2"
    RIGHT_DOUBLE = R_D = "R2"
    LEFT_DOUBLE = L_D = "L2"
    UPPER_DOUBLE = U_D = "U2"
    DOWN_DOUBLE = D_D = "D2"


class Cube:
    UPPER = 0
    FRONT = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4
    BACK = 5

    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 2

    def __init__(self):
        self.cube = numpy.array(
            [
                [Color.YELLOW] * 4,  # UPPER
                [Color.ORANGE] * 4,  # FRONT
                [Color.GREEN] * 4,  # LEFT
                [Color.BLUE] * 4,  # RIGHT
                [Color.WHITE] * 4,  # DOWN
                [Color.RED] * 4  # BACK
            ]
        )

    @staticmethod
    def from_dict(sides):
        cube = Cube()
        cube.cube[Cube.UPPER] = numpy.array(sides["upper"])
        cube.cube[Cube.FRONT] = numpy.array(sides["front"])
        cube.cube[Cube.LEFT] = numpy.array(sides["left"])
        cube.cube[Cube.RIGHT] = numpy.array(sides["right"])
        cube.cube[Cube.DOWN] = numpy.array(sides["down"])
        cube.cube[Cube.BACK] = numpy.array(sides["back"])
        return cube

    def rotate_face_clockwise(self, face):
        cube_face = numpy.copy(self.cube[face])
        self.cube[face, Cube.TOP_LEFT] = cube_face[Cube.BOTTOM_LEFT]
        self.cube[face, Cube.TOP_RIGHT] = cube_face[Cube.TOP_LEFT]
        self.cube[face, Cube.BOTTOM_RIGHT] = cube_face[Cube.TOP_RIGHT]
        self.cube[face, Cube.BOTTOM_LEFT] = cube_face[Cube.BOTTOM_RIGHT]

    def rotate_face_counter_clockwise(self, face):
        cube_face = numpy.copy(self.cube[face])
        self.cube[face, Cube.TOP_LEFT] = cube_face[Cube.TOP_RIGHT]
        self.cube[face, Cube.TOP_RIGHT] = cube_face[Cube.BOTTOM_RIGHT]
        self.cube[face, Cube.BOTTOM_RIGHT] = cube_face[Cube.BOTTOM_RIGHT]
        self.cube[face, Cube.BOTTOM_LEFT] = cube_face[Cube.TOP_LEFT]

    def rotate_face_double(self, face):
        cube_face = numpy.copy(self.cube[face])
        self.cube[face, Cube.TOP_LEFT] = cube_face[Cube.TOP_RIGHT]
        self.cube[face, Cube.TOP_RIGHT] = cube_face[Cube.BOTTOM_RIGHT]
        self.cube[face, Cube.BOTTOM_RIGHT] = cube_face[Cube.BOTTOM_RIGHT]
        self.cube[face, Cube.BOTTOM_LEFT] = cube_face[Cube.TOP_LEFT]

    def move(self, direction):
        cube_copy = numpy.copy(self.cube)
        if direction == Direction.FRONT:
            self.rotate_face_clockwise(Cube.FRONT)
            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.RIGHT, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.RIGHT, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.BACK:
            self.rotate_face_clockwise(Cube.BACK)
            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]

            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            pass
        elif direction == Direction.LEFT:
            self.rotate_face_clockwise(Cube.LEFT)

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]

            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]

            pass
        elif direction == Direction.RIGHT:
            self.rotate_face_clockwise(Cube.RIGHT)

            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]

            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]

            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]
            pass
        elif direction == Direction.UPPER:
            self.rotate_face_clockwise(Cube.UPPER)

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.RIGHT, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.RIGHT, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.DOWN:
            self.rotate_face_clockwise(Cube.DOWN)

            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]

            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]

            pass

        elif direction == Direction.FRONT_INVERTED:
            self.rotate_face_counter_clockwise(Cube.FRONT)

            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.RIGHT, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.RIGHT, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.BACK_INVERTED:
            self.rotate_face_counter_clockwise(Cube.BACK)

            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]

            pass
        elif direction == Direction.LEFT_INVERTED:
            self.rotate_face_counter_clockwise(Cube.LEFT)

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]

            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]

            pass
        elif direction == Direction.RIGHT_INVERTED:
            self.rotate_face_counter_clockwise(Cube.RIGHT)

            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]

            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]
            pass
        elif direction == Direction.UPPER_INVERTED:
            self.rotate_face_counter_clockwise(Cube.UPPER)

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.RIGHT, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.RIGHT, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.DOWN_INVERTED:
            self.rotate_face_counter_clockwise(Cube.DOWN)

            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]
            pass

        elif direction == Direction.FRONT_DOUBLE:
            self.rotate_face_double(Cube.FRONT)
            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.BACK_DOUBLE:
            self.rotate_face_double(Cube.BACK)
            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            pass
        elif direction == Direction.LEFT_DOUBLE:
            self.rotate_face_double(Cube.LEFT)

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]

            self.cube[Cube.UPPER, Cube.TOP_LEFT] = cube_copy[Cube.DOWN, Cube.TOP_LEFT]
            self.cube[Cube.UPPER, Cube.BOTTOM_LEFT] = cube_copy[Cube.DOWN, Cube.BOTTOM_LEFT]

            self.cube[Cube.DOWN, Cube.TOP_LEFT] = cube_copy[Cube.UPPER, Cube.TOP_LEFT]
            self.cube[Cube.DOWN, Cube.BOTTOM_LEFT] = cube_copy[Cube.UPPER, Cube.BOTTOM_LEFT]

            pass
        elif direction == Direction.RIGHT_DOUBLE:
            self.rotate_face_double(Cube.RIGHT)

            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]

            self.cube[Cube.UPPER, Cube.TOP_RIGHT] = cube_copy[Cube.DOWN, Cube.TOP_RIGHT]
            self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT] = cube_copy[Cube.DOWN, Cube.BOTTOM_RIGHT]

            self.cube[Cube.DOWN, Cube.TOP_RIGHT] = cube_copy[Cube.UPPER, Cube.TOP_RIGHT]
            self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT] = cube_copy[Cube.UPPER, Cube.BOTTOM_RIGHT]
            pass
        elif direction == Direction.UPPER_DOUBLE:
            self.rotate_face_double(Cube.UPPER)

            self.cube[Cube.FRONT, Cube.TOP_LEFT] = cube_copy[Cube.BACK, Cube.TOP_LEFT]
            self.cube[Cube.FRONT, Cube.TOP_RIGHT] = cube_copy[Cube.BACK, Cube.TOP_RIGHT]

            self.cube[Cube.RIGHT, Cube.TOP_LEFT] = cube_copy[Cube.LEFT, Cube.TOP_LEFT]
            self.cube[Cube.RIGHT, Cube.TOP_RIGHT] = cube_copy[Cube.LEFT, Cube.TOP_RIGHT]

            self.cube[Cube.BACK, Cube.TOP_LEFT] = cube_copy[Cube.FRONT, Cube.TOP_LEFT]
            self.cube[Cube.BACK, Cube.TOP_RIGHT] = cube_copy[Cube.FRONT, Cube.TOP_RIGHT]

            self.cube[Cube.LEFT, Cube.TOP_LEFT] = cube_copy[Cube.RIGHT, Cube.TOP_LEFT]
            self.cube[Cube.LEFT, Cube.TOP_RIGHT] = cube_copy[Cube.RIGHT, Cube.TOP_RIGHT]

            pass
        elif direction == Direction.DOWN_DOUBLE:
            self.rotate_face_double(Cube.DOWN)

            self.cube[Cube.FRONT, Cube.BOTTOM_LEFT] = cube_copy[Cube.BACK, Cube.BOTTOM_LEFT]
            self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.BACK, Cube.BOTTOM_RIGHT]

            self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT] = cube_copy[Cube.LEFT, Cube.BOTTOM_LEFT]
            self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.LEFT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.BACK, Cube.BOTTOM_LEFT] = cube_copy[Cube.FRONT, Cube.BOTTOM_LEFT]
            self.cube[Cube.BACK, Cube.BOTTOM_RIGHT] = cube_copy[Cube.FRONT, Cube.BOTTOM_RIGHT]

            self.cube[Cube.LEFT, Cube.BOTTOM_LEFT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_LEFT]
            self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT] = cube_copy[Cube.RIGHT, Cube.BOTTOM_RIGHT]
            pass

    def __eq__(self, other):
        return numpy.array_equal(self.cube, other.cube)

    def unfold(self):
        s = """        {1}         {2}
        {0}|{utl}###{0}#{utr}###{0}|
        {1}{0}|{utl}###{0}#{utr}###{0}|{2}
        {0}|{ubl}###{0}#{ubr}###{0}|
{1}        {0}|{ubl}###{0}#{ubr}###{0}|                {2}
{0}|{ltl}###{0}#{ltr}###{0}|{ftl}###{0}#{ftr}###{0}|{rtl}###{0}{rtr}####{0}|{btl}###{0}#{btr}###{0}|
{1}{0}|{ltl}###{0}#{ltr}###{0}|{ftl}###{0}#{ftr}###{0}|{rtl}###{0}{rtr}####{0}|{btl}###{0}#{btr}###{0}|{2}
{0}|{lbl}###{0}#{lbr}###{0}|{fbl}###{0}#{fbr}###{0}|{rbl}###{0}{rbr}####{0}|{bbl}###{0}#{bbr}###{0}|
{1}{0}|{lbl}###{0}#{lbr}###{0}|{fbl}###{0}#{fbr}###{0}|{rbl}###{0}{rbr}####{0}|{bbl}###{0}#{bbr}###{0}|{2}
        {0}|{dtl}###{0}#{dtr}###{0}|
        {1}{0}|{dtl}###{0}#{dtr}###{0}|{2}
        {0}|{dbl}###{0}#{dbr}###{0}|
        {1}{0}|{dbl}###{0}#{dbr}###{0}|{2}
        """.format("\x1b[97m", "\x1b[4m", "\x1b[0m",
                   ltl=self.cube[Cube.LEFT, Cube.TOP_LEFT].code(),
                   ltr=self.cube[Cube.LEFT, Cube.TOP_RIGHT].code(),
                   lbl=self.cube[Cube.LEFT, Cube.BOTTOM_LEFT].code(),
                   lbr=self.cube[Cube.LEFT, Cube.BOTTOM_RIGHT].code(),

                   ftl=self.cube[Cube.FRONT, Cube.TOP_LEFT].code(),
                   ftr=self.cube[Cube.FRONT, Cube.TOP_RIGHT].code(),
                   fbl=self.cube[Cube.FRONT, Cube.BOTTOM_LEFT].code(),
                   fbr=self.cube[Cube.FRONT, Cube.BOTTOM_RIGHT].code(),

                   rtl=self.cube[Cube.RIGHT, Cube.TOP_LEFT].code(),
                   rtr=self.cube[Cube.RIGHT, Cube.TOP_RIGHT].code(),
                   rbl=self.cube[Cube.RIGHT, Cube.BOTTOM_LEFT].code(),
                   rbr=self.cube[Cube.RIGHT, Cube.BOTTOM_RIGHT].code(),

                   btl=self.cube[Cube.BACK, Cube.TOP_LEFT].code(),
                   btr=self.cube[Cube.BACK, Cube.TOP_RIGHT].code(),
                   bbl=self.cube[Cube.BACK, Cube.BOTTOM_LEFT].code(),
                   bbr=self.cube[Cube.BACK, Cube.BOTTOM_RIGHT].code(),

                   utl=self.cube[Cube.UPPER, Cube.TOP_LEFT].code(),
                   utr=self.cube[Cube.UPPER, Cube.TOP_RIGHT].code(),
                   ubl=self.cube[Cube.UPPER, Cube.BOTTOM_LEFT].code(),
                   ubr=self.cube[Cube.UPPER, Cube.BOTTOM_RIGHT].code(),

                   dtl=self.cube[Cube.DOWN, Cube.TOP_LEFT].code(),
                   dtr=self.cube[Cube.DOWN, Cube.TOP_RIGHT].code(),
                   dbl=self.cube[Cube.DOWN, Cube.BOTTOM_LEFT].code(),
                   dbr=self.cube[Cube.DOWN, Cube.BOTTOM_RIGHT].code(),
                   )
        return s


def array_eq(a, b):
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3]


if __name__ == "__main__":
    cube_ = Cube()
