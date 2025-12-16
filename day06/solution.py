def main():
    with open("input.txt") as f:
        lines: list[str] = f.readlines()
    print(part1(lines))
    print(part2(lines))

def part1(lines: list[str]):
    data: list[list[str]] = [line.strip().split() for line in lines]
    sum = 0
    for i in range(len(data[0])):
        op: str = data[len(data)-1][i]
        result: int = 0 if op == "+" else 1
        nums: list[int] = [(int)(data[j][i]) for j in range(len(data)-1)]
        for num in nums:
            if op == "+":
                result += num
            elif op == "*":
                result *= num
        sum += result
    return sum

def part2(lines: list[str]):
    num_lines, op_line = lines[:-1], lines[-1]
    total = 0
    index = 0
    for op in op_line.strip().split():
        result = 0 if op == "+" else 1

        while(True):
            num = 0
            for i in range(len(num_lines)):
                if num != 0 and (num_lines[i][index] == ' '):
                    # ignore trailing spaces
                    break
                num *= 10
                if num_lines[i][index] >= '0' and num_lines[i][index] <= '9':
                    num += int(num_lines[i][index])
            
            if num == 0:
                index += 1
                break

            if op == "+":
                result += num
            elif op == "*":
                result *= num

            index += 1
        total += result
    return total
    
if __name__ == "__main__":
    main()
