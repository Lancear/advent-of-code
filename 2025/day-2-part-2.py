import math

INPUT_FILE = "./day-2-input.txt"


def nrlen(num: int):
    return len(str(num))


def repeat(amount: int, text: str):
    repeated = ""

    for _ in range(amount):
        repeated += text

    return repeated


class IdRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

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

    def invalid_ids_for_pattern(self, pattern: int):
        patternAmount = max(2, math.ceil(nrlen(self.start) / nrlen(pattern)))
        invalidId = int(repeat(patternAmount, str(pattern)))

        while invalidId <= self.end:
            if invalidId >= self.start:
                yield invalidId

            patternAmount += 1
            invalidId = int(repeat(patternAmount, str(pattern)))

    def invalid_ids(self):
        for patternLength in range(1, int(nrlen(self.end) / 2) + 1):
            pattern = 10 ** (patternLength - 1)

            while nrlen(pattern) == patternLength:
                yield from self.invalid_ids_for_pattern(pattern)
                pattern += 1


class InvalidIdRange(IdRange):
    def __init__(self, error: str):
        super().__init__(0, 0)
        self.error = error


def main():
    invalidIds: set[int] = set()

    with open(INPUT_FILE, "r") as file:
        for rangeText in file.read().strip().split(","):
            idRange = IdRange.parse(rangeText)

            if isinstance(idRange, InvalidIdRange):
                print("Skipped " + idRange.error)

            for invalidId in idRange.invalid_ids():
                invalidIds.add(invalidId)

    print("Sum of invalid ids: " + str(sum(invalidIds)))


if __name__ == "__main__":
    main()
