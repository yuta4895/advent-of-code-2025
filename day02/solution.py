def main():
    with open("input.txt") as f:
        line = f.readline()
    ranges : list[tuple[int, int]] = parse(line)
    print(part1(ranges))
    print(part2(ranges))

def parse(line: str) -> list[tuple[int, int]]:
    parts = line.split(",")
    ranges = []
    for part in parts:
        a, b = part.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def part1(ranges: list[tuple[int, int]]):
    sum = 0
    for a, b in ranges:
        for x in range(a, b + 1):
            if(invalid(x)):
                sum += x
    return sum

def invalid(x: int) -> bool:
    if len(str(x))%2 != 0:
        return False
    for i in range(len(str(x))//2):
        if str(x)[i] != str(x)[i+len(str(x))//2]:
            return False
    return True

def part2(ranges: list[tuple[int, int]]):
    sum = 0
    for a, b in ranges:
        for x in range(a, b + 1):
            s = str(x)
            for chunk_size in range(1, len(s)):
                if has_chunk_repetition(s, chunk_size):
                    sum += x
                    break
    return sum

def has_chunk_repetition(s: str, chunk_size: int) -> bool:
    """Returns True if x is repeating number with specified chunk_size."""
    if(len(s)%chunk_size != 0):
        return False
    chunk_num = len(s) // chunk_size
    for chunk_index in range(chunk_num):
        for base_index in range(chunk_size):
            if s[base_index] != s[base_index+chunk_size*chunk_index]:
                return False
    return True

if __name__ == "__main__":
    main()