INPUT_FILE = "./day-2-input.txt"


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

    def start_digits(self) -> int:
        text = str(self.start)

        if len(text) % 2 == 1:
            return 10 ** int(len(text) / 2)

        middle = int(len(text) / 2)
        firstHalf = int(text[:middle])
        secondHalf = int(text[middle:])
        return firstHalf + (1 if firstHalf < secondHalf else 0)

    def invalid_id_for_digits(self, digits: int):
        return int(str(digits) + str(digits))

    def invalid_ids(self):
        invalidIds: list[int] = []
        digits = self.start_digits()
        invalidId = self.invalid_id_for_digits(digits)

        while invalidId <= self.end:
            invalidIds.append(invalidId)
            digits += 1
            invalidId = self.invalid_id_for_digits(digits)

        return invalidIds


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

            invalidIds = invalidIds.union(idRange.invalid_ids())

    print("Sum of invalid ids: " + str(sum(invalidIds)))


if __name__ == "__main__":
    main()
