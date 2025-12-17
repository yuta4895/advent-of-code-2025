def main():
    with open("input.txt") as f:
        field: list[str] = [line.strip() for line in f.readlines()]
    print(part1(field))
    print(part2(field))

def part1(field: list[str]):
    split_count = 0
    beams = set()

    for line in field:
        # Add initial beams
        beams.add(line.index("S")) if "S" in line else None

        # Process existing beams
        for beam in set(beams):
            if line[beam] == '^':
                split_count += 1
                beams.remove(beam)
                beams.add(beam-1)
                beams.add(beam+1)

    return split_count

def part2(field: list[str]):
    for line in field:
        if "S" in line:
            return dfs(field.index(line), line.index("S"), field, [[-1]*len(field[0]) for _ in range(len(field))])

def dfs(i: int, j: int, field: list[str], memo: list[list[int]]) -> int:
    time_line_count = 0
    if memo[i][j] != -1:
        return memo[i][j]
    if i == len(field)-1:
        return 1
    if j < 0 or j >= len(field[0]):
        return 0
    
    if field[i+1][j] == '^':
        time_line_count += dfs(i+1, j+1, field, memo)
        time_line_count += dfs(i+1, j-1, field, memo)
    else:
        time_line_count += dfs(i+1, j, field, memo)
    memo[i][j] = time_line_count
    return memo[i][j]
    
if __name__ == "__main__":
    main()