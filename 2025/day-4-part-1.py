INPUT_FILE = "./day-4-input.txt"


class Diagram:
    def __init__(self, rows: list[str]):
        self.rows = rows
        self.rowCount = len(self.rows)
        self.colCount = len(self.rows[0].strip()) if self.rowCount > 0 else 0

    def cells(self):
        for row in range(self.rowCount):
            for col in range(self.colCount):
                yield (row, col)

    def is_paper_roll(self, row: int, col: int):
        if row < 0 or col < 0:
            return False

        if row >= self.rowCount or col >= self.colCount:
            return False

        return self.rows[row][col] == "@"

    def is_paper_roll_accessible(self, row: int, col: int):
        if not self.is_paper_roll(row, col):
            return False

        surroundingRolls = 0

        for rowDelta in range(-1, 2):
            for colDelta in range(-1, 2):
                if rowDelta == 0 and colDelta == 0:
                    continue

                if self.is_paper_roll(row + rowDelta, col + colDelta):
                    surroundingRolls += 1

        return surroundingRolls < 4


def main():
    accessibleRolls = 0

    with open(INPUT_FILE, "r") as file:
        diagram = Diagram(file.readlines())

        for row, col in diagram.cells():
            if diagram.is_paper_roll_accessible(row, col):
                accessibleRolls += 1

    print("Accessible rolls: " + str(accessibleRolls))


if __name__ == "__main__":
    main()
