INPUT_FILE = "./day-3-input.txt"
BATTERIES_PER_BANK = 12


def max_jolts_of_bank(bank: str):
    maxJoltDigitIndices = list(range(BATTERIES_PER_BANK))

    for bankIdx, battery in enumerate(bank):
        jolt = int(battery)

        for digitPosition, maxJoltIdx in enumerate(maxJoltDigitIndices):
            if bankIdx <= maxJoltIdx:
                break

            digitsLeft = BATTERIES_PER_BANK - digitPosition
            enoughSpaceLeft = bankIdx + digitsLeft - 1 < len(bank)

            if jolt > int(bank[maxJoltIdx]) and enoughSpaceLeft:
                for i in range(digitsLeft):
                    maxJoltDigitIndices[digitPosition + i] = bankIdx + i

                break

    maxJolts = ""

    for i in maxJoltDigitIndices:
        maxJolts += bank[i]

    return int(maxJolts)


def main():
    totalJolts = 0

    with open(INPUT_FILE, "r") as file:
        for bank in file:
            totalJolts += max_jolts_of_bank(bank.strip())

    print("Total jolts: " + str(totalJolts))


if __name__ == "__main__":
    main()
