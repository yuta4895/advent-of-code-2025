def main():
    with open("input.txt") as f:
        lines: list[str] = f.readlines()
    print(part1(lines))
    print(part2(lines))

def part1(lines: list[str]) -> int:
    total_joltage = 0
    for line in lines:
        joltage = calc_joltage(line.strip(), 2)
        total_joltage += joltage
    return total_joltage

def part2(lines: list[str]) -> int:
    total_joltage = 0
    for line in lines:
        joltage = calc_joltage(line.strip(), 12)
        total_joltage += joltage
    return total_joltage
            
def calc_joltage(s: str, digit: int) -> int:
    joltage = [0] * digit
    for i, n in enumerate(s):
        num = int(n)
        updated = False
        for d in range(max(digit-(len(s)-i), 0), digit): # update from highest digit to lowest, hightest digit is 
            if updated:
                joltage[d] = 0
            elif num > joltage[d]:
                joltage[d] = num
                updated = True

    result = 0
    for d in range(digit):
        result = result * 10 + joltage[d]
    return result
    

if __name__ == "__main__":
    main()