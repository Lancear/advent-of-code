INPUT_FILE = "./day-7-input.txt"


class Laser:
    def __init__(self, diagram: list[str]):
        self.beams = [diagram[0].index("S")]
        self.rows = diagram[1:]
        self.rowCount = len(self.rows)
        self.colCount = len(self.rows[0].strip()) if self.rowCount > 0 else 0
        self.nrOfSplits = 0

    def calculate_splits(self):
        for row in self.rows:
            self.process_row(row)

        return self.nrOfSplits

    def process_row(self, row: str):
        newBeams: list[int] = []

        for beam in self.beams:
            self.update_beam(row, beam, newBeams)

        self.beams = newBeams

    def update_beam(self, row: str, beam: int, newBeams: list[int]):
        if row[beam] == "^":
            self.nrOfSplits += 1
            self.add_beam(newBeams, beam - 1)
            self.add_beam(newBeams, beam + 1)
        else:
            self.add_beam(newBeams, beam)

    def add_beam(self, beams: list[int], beam: int):
        if beam < 0 or beam >= self.colCount:
            return

        if beam not in beams:
            beams.append(beam)


def main():
    with open(INPUT_FILE, "r") as file:
        laser = Laser(file.readlines())
        nrOfSplits = laser.calculate_splits()
        print("Number of splits: " + str(nrOfSplits))


if __name__ == "__main__":
    main()
