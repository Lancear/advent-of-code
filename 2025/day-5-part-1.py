INPUT_FILE = "./day-5-input.txt"


class IdRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, id: int):
        return id >= self.start and id <= self.end

    @staticmethod
    def parse(text: str):
        startText, endText = text.split("-")
        start = int(startText) if startText.isdigit() else None
        end = int(endText) if endText.isdigit() else None

        if start is None or end is None:
            return InvalidIdRange(
                "Invalid Id Range, Expected format <int>-<int> "
                "(e.g. 12-83, 1-3078), received: " + text
            )

        return IdRange(start, end)


class InvalidIdRange(IdRange):
    def __init__(self, error: str):
        super().__init__(0, 0)
        self.error = error


def main():
    freshIdRanges: list[IdRange] = []
    nrOfFreshProducts = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            if line.isspace():
                break

            idRange = IdRange.parse(line.strip())

            if isinstance(idRange, InvalidIdRange):
                print("Skipped " + idRange.error)
                continue

            freshIdRanges.append(idRange)

        for line in file:
            productId = int(line.strip())

            if any(
                freshIdRange.contains(productId)
                for freshIdRange in freshIdRanges
            ):
                nrOfFreshProducts += 1

    print("Number of fresh products: " + str(nrOfFreshProducts))


if __name__ == "__main__":
    main()
