def main(path="input.txt"):
    with open(path) as f:
        lines = f.readlines()
    print(part1(lines))
    print(part2(lines))

def part1(lines):
    pos = 50
    ans = 0
    for line in lines:
        dir, delta = line[0], int(line[1:])
        pos += delta if dir == "R" else -delta
        pos %= 100
        ans += pos == 0
    return ans

def part2(lines):
    pos = 50
    ans = 0
    for line in lines:
        dir, delta = line[0], int(line[1:])
        if dir == "R":
            ans += (pos + delta) // 100
            pos = (pos + delta) % 100
        else:
            offset = pos % 100
            ans += abs(delta - offset) // 100 + (delta >= offset and offset != 0)
            pos = (pos - delta) % 100            
    return ans

if __name__ == "__main__":
    main()