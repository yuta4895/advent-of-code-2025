def main():
    with open("input.txt") as f:
        lines: list[list[str]] = [line.strip().split() for line in f.readlines()]
    print(part1(lines))

def part1(lines: list[list[str]]):
    sum = 0
    for i in range(len(lines[0])):
        op: str = lines[len(lines)-1][i]
        result: int = 0 if op == "+" else 1
        nums: list[int] = [(int)(lines[j][i]) for j in range(len(lines)-1)]
        for num in nums:
            if op == "+":
                result += num
            elif op == "*":
                result *= num
        sum += result
    return sum

if __name__ == "__main__":
    main()
