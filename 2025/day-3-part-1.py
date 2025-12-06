INPUT_FILE = "./day-3-input.txt"


def max_jolts_of_bank(bank: str):
    maxFirstDigitIdx = 0
    maxSecondDigitIdx = 1

    for idx, ch in enumerate(bank):
        digit = int(ch)

        if digit > int(bank[maxFirstDigitIdx]) and idx + 1 < len(bank):
            maxFirstDigitIdx = idx
            maxSecondDigitIdx = idx + 1
        elif digit > int(bank[maxSecondDigitIdx]) and idx > 0:
            maxSecondDigitIdx = idx

    maxJolts = int(bank[maxFirstDigitIdx] + bank[maxSecondDigitIdx])
    return maxJolts


def main():
    totalJolts = 0

    with open(INPUT_FILE, "r") as file:
        for bank in file:
            totalJolts += max_jolts_of_bank(bank.strip())

    print("Total jolts: " + str(totalJolts))


if __name__ == "__main__":
    main()
