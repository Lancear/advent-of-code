INPUT_FILE = "./day-7-input.txt"


class Beam:
    def __init__(self, col: int, nrOfPaths: int):
        self.col = col
        self.nrOfPaths = nrOfPaths

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Beam):
            return False

        return self.col == other.col


class Laser:
    def __init__(self, diagram: list[str]):
        self.beams = [Beam(diagram[0].index("S"), 1)]
        self.rows = diagram[1:]
        self.rowCount = len(self.rows)
        self.colCount = len(self.rows[0].strip()) if self.rowCount > 0 else 0

    def calculate_paths(self):
        for row in self.rows:
            self.process_row(row)

        return sum(beam.nrOfPaths for beam in self.beams)

    def process_row(self, row: str):
        newBeams: list[Beam] = []

        for beam in self.beams:
            self.update_beam(row, beam, newBeams)

        self.beams = newBeams

    def update_beam(self, row: str, beam: Beam, newBeams: list[Beam]):
        if row[beam.col] == "^":
            self.add_beam(newBeams, Beam(beam.col - 1, beam.nrOfPaths))
            self.add_beam(newBeams, Beam(beam.col + 1, beam.nrOfPaths))
        else:
            self.add_beam(newBeams, beam)

    def add_beam(self, beams: list[Beam], beam: Beam):
        if beam.col < 0 or beam.col >= self.colCount:
            return

        if beam not in beams:
            beams.append(beam)
        else:
            beamIdx = beams.index(beam)
            beams[beamIdx].nrOfPaths += beam.nrOfPaths


def main():
    with open(INPUT_FILE, "r") as file:
        laser = Laser(file.readlines())
        nrOfPaths = laser.calculate_paths()
        print("Number of paths: " + str(nrOfPaths))


if __name__ == "__main__":
    main()
