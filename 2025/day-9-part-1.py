from math import sqrt

INPUT_FILE = "./day-9-example.txt"


class Point:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def distance(self, other: "Point"):
        return sqrt((self.row - other.row) ** 2 + (self.col - other.col) ** 2)

    @staticmethod
    def parse(text: str):
        colText, rowText = text.split(",")
        row = int(rowText) if rowText.isdigit() else None
        col = int(colText) if colText.isdigit() else None

        if row is None or col is None:
            return InvalidPoint(
                "Invalid Point, Expected format <int>,<int> "
                "(e.g. 12,83 or 1,3078), received: " + text
            )

        return Point(row, col)


class InvalidPoint(Point):
    def __init__(self, error: str):
        super().__init__(0, 0)
        self.error = error


def main():
    topLeftCorner, topRightCorner, bottomLeftCorner, bottomRightCorner = (
        Point(0, 0),
        Point(0, 0),
        Point(0, 0),
        Point(0, 0),
    )
    topLeft, topRight, bottomLeft, bottomRight = None, None, None, None

    with open(INPUT_FILE, "r") as file:
        for line in file:
            point = Point.parse(line.strip())

            if topLeft is None or point.distance(
                topLeftCorner
            ) < topLeft.distance(topLeftCorner):
                topLeft = point

            topRightCorner = Point(0, max(point.col, topRightCorner.col))

            if topRight is None or point.distance(
                topRightCorner
            ) < topRight.distance(topRightCorner):
                topRight = point

            bottomLeftCorner = Point(max(point.row, bottomLeftCorner.row), 0)

            if bottomLeft is None or point.distance(
                bottomLeftCorner
            ) < bottomLeft.distance(bottomLeftCorner):
                bottomLeft = point

            bottomRightCorner = Point(
                max(point.row, bottomRightCorner.row),
                max(point.col, bottomRightCorner.row),
            )

            if bottomRight is None or point.distance(
                bottomRightCorner
            ) < bottomRight.distance(bottomRightCorner):
                bottomRight = point

    print("Top left: " + str(topLeft.col) + "," + str(topLeft.row))
    print("Top right: " + str(topRight.col) + "," + str(topRight.row))
    print("Bottom left: " + str(bottomLeft.col) + "," + str(bottomLeft.row))
    print("Bottom right: " + str(bottomRight.col) + "," + str(bottomRight.row))


if __name__ == "__main__":
    main()
