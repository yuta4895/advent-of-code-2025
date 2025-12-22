def main():
    with open("input.txt") as f:
        coords: list[tuple[int, int]] = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
    print(part1(coords))

def part1(coords: list[tuple[int, int]]) -> int:
    max_area = 0
    for x, y in coords:
        for x2, y2 in coords:
            area = abs(x - x2 + 1) * abs(y - y2 + 1)
            max_area = max(max_area, area)
    return max_area

if __name__ == "__main__":
    main()