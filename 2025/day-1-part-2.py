import math
from enum import IntEnum

INPUT_FILE = "./day-1-input.txt"
DIAL_MAX = 100


class Direction(IntEnum):
    LEFT = -1
    RIGHT = 1


class Rotation:
    def __init__(self, distance: int, direction: Direction):
        self.distance = distance
        self.direction = direction

    def diff(self):
        return self.distance * self.direction

    @staticmethod
    def parse(text: str):
        distance = int(text[1:]) if text[1:].isdigit() else None
        direction = (
            (Direction.LEFT if text[0] == "L" else Direction.RIGHT)
            if text[0] in ["L", "R"]
            else None
        )

        if distance is None or direction is None:
            return InvalidRotation(
                "Invalid Rotation, Expected format <L|R><int> "
                "(e.g. L12, R46), received: " + text
            )

        return Rotation(distance, direction)


class InvalidRotation(Rotation):
    def __init__(self, error: str):
        super().__init__(0, Direction.LEFT)
        self.error = error


class Dial:
    value: int
    maximum: int

    def __init__(self, value: int, maximum: int):
        self.value = value
        self.maximum = maximum

    def rotate(self, rotation: Rotation):
        oldValue = self.value
        unnormalizedNewValue = oldValue + rotation.diff()
        self.value = unnormalizedNewValue % self.maximum

        fullRotations = math.floor(abs(unnormalizedNewValue) / 100)

        rotationsPastZero = (
            fullRotations + 1  # additional rotation to zero / negative
            if unnormalizedNewValue <= 0 and oldValue > 0
            else fullRotations
        )

        return rotationsPastZero


def main():
    dial = Dial(int(DIAL_MAX / 2), DIAL_MAX)
    rotationsPastZero = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            rotation = Rotation.parse(line.strip())

            if isinstance(rotation, InvalidRotation):
                print("Skipped " + rotation.error)

            rotationsPastZero += dial.rotate(rotation)

    print("Rotations past zero: " + str(rotationsPastZero))


if __name__ == "__main__":
    main()
