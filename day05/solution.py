def main():
    ranges: list[list[int, int]] = []
    available_ids: list[int] = []
    with open("input.txt") as f:
        while(line := f.readline().strip()) and line != "":
            ranges.append(list(map(int, line.split("-"))))
        while(line := f.readline().strip()):
            available_ids.append(int(line))

    print(part1(ranges, available_ids))
    print(part2(ranges))

def part1(ranges: list[list[int, int]], available_ids: list[int]):
    valid_ids = []
    for id in available_ids:
        for range in ranges:
            if range[0] <= id and range[1] >= id:
                valid_ids.append(id)
                break
    return len(valid_ids)
                    
def part2(ranges: list[list[int, int]]):
    total = 0
    ranges.sort()
    curr_range: list[int, int] = [0, -1]
    for range in ranges:
        if range[0] <= curr_range[1]:
            curr_range[1] = max(range[1], curr_range[1])
        else:
            total += curr_range[1] - curr_range[0] + 1
            curr_range = range

    total += curr_range[1] - curr_range[0] + 1
    return total
    
if __name__ == "__main__":
    main()
