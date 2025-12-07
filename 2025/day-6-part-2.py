INPUT_FILE = "./day-6-input.txt"


class Problem:
    def __init__(self, initialValue: int):
        self.result = initialValue

    def calculate(self, num: int):
        return self.result

    @staticmethod
    def parse(text: str):
        return AddProblem() if text == "+" else MultiplyProblem()


class AddProblem(Problem):
    def __init__(self):
        super().__init__(0)

    def calculate(self, num: int):
        self.result += num
        return self.result


class MultiplyProblem(Problem):
    def __init__(self):
        super().__init__(1)

    def calculate(self, num: int):
        self.result *= num
        return self.result


class Worksheet:
    def __init__(self, sheet: list[str]):
        self.numbersSheet = sheet[:-1]
        self.rowCount = len(self.numbersSheet)
        self.colCount = len(self.numbersSheet[0]) if self.rowCount > 0 else 0
        self.problems = list(
            Problem.parse(operator) for operator in sheet[-1].split()
        )

    def calculate(self):
        problemIdx = 0

        for col in range(self.colCount):
            numText = "".join(
                self.numbersSheet[row][col] for row in range(self.rowCount)
            )

            if numText.isspace():
                problemIdx += 1
                continue

            self.problems[problemIdx].calculate(int(numText))

        return sum(problem.result for problem in self.problems)


def main():

    with open(INPUT_FILE, "r") as file:
        worksheet = Worksheet(file.readlines())
        grandTotal = worksheet.calculate()
        print("Worksheet grand total: " + str(grandTotal))


if __name__ == "__main__":
    main()
