import array

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = [list(line) for line in lines]
    print(part1(lines))
    print(part2(lines))

def part1(lines: list[list[str]]) -> int:
    rolls, _ = count_accessible_rolls(lines)
    return rolls

def part2(lines: list[list[str]]) -> int:
    total_rolls = 0
    while(True):
        rolls, lines = count_accessible_rolls(lines)
        if rolls == 0:
            break
        total_rolls += rolls
    return total_rolls

def count_accessible_rolls(lines: list[list[str]]) -> int:
    new_lines = [line.copy() for line in lines]
    rolls = 0
    dx = [0, 1, -1]
    dy = [0, 1, -1]
    directions = [(y, x) for y in dy for x in dx if (y, x) != (0, 0)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != "@":
                continue
            cnt = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]) and lines[ni][nj] == "@":
                    cnt += 1
            if cnt < 4:
                new_lines[i][j] = '.'
                rolls += 1
    return rolls, new_lines

if __name__ == "__main__":
    main()