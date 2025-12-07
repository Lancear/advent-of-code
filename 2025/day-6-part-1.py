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
        self.problems = list(
            Problem.parse(operator) for operator in sheet[-1].split()
        )

    def calculate(self):
        for row in self.numbersSheet:
            for idx, num in enumerate(row.split()):
                self.problems[idx].calculate(int(num))

        return sum(problem.result for problem in self.problems)


def main():

    with open(INPUT_FILE, "r") as file:
        worksheet = Worksheet(file.readlines())
        grandTotal = worksheet.calculate()
        print("Worksheet grand total: " + str(grandTotal))


if __name__ == "__main__":
    main()
