INPUT_FILE = "./day-5-input.txt"


class IdRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, id: int):
        return id >= self.start and id <= self.end

    def overlaps(self, other: "IdRange"):
        return (
            self.contains(other.start)
            or self.contains(other.end)
            or other.contains(self.start)
            or other.contains(self.end)
        )

    def merge(self, other: "IdRange"):
        return (
            IdRange(min(self.start, other.start), max(self.end, other.end))
            if self.overlaps(other)
            else None
        )

    def __len__(self):
        return self.end - self.start + 1

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


class IdRanges:
    def __init__(self):
        self.ranges: list[IdRange] = []

    def append(self, idRange: IdRange):
        for exisitingRange in self.ranges:
            if exisitingRange.overlaps(idRange):
                self.remove(exisitingRange)
                self.append(exisitingRange.merge(idRange))
                return

        self.ranges.append(idRange)

    def remove(self, idRange: IdRange):
        self.ranges.remove(idRange)

    def __iter__(self):
        for idRange in self.ranges:
            yield idRange


def main():
    freshIdRanges = IdRanges()

    with open(INPUT_FILE, "r") as file:
        for line in file:
            if line.isspace():
                break

            idRange = IdRange.parse(line.strip())

            if isinstance(idRange, InvalidIdRange):
                print("Skipped " + idRange.error)
                continue

            freshIdRanges.append(idRange)

    nrOfFreshProductIds = sum(len(idRange) for idRange in freshIdRanges)
    print("Number of fresh product ids: " + str(nrOfFreshProductIds))


if __name__ == "__main__":
    main()
