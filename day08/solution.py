import heapq

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def issame(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

    def unite(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]

        return True

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

def main():
    with open("input.txt") as f:
        coords: list[tuple[int, int, int]] = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
    print(part1(coords))
    print(part2(coords))

def part1(coords: list[tuple[int, int, int]]):
    distances: list[tuple[int, int, int]] = []
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            dist = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2 + (coords[i][2] - coords[j][2])**2
            distances.append((dist, i, j))
    heapq.heapify(distances)

    uf = UnionFind(len(coords))

    for _ in range(1000):
        dist, u, v = heapq.heappop(distances)
        if not uf.issame(u, v):
            uf.unite(u, v)
    
    components_size = [uf.size[i] for i in range(len(coords)) if uf.find(i) == i]
    components_size.sort(reverse=True)
    return components_size[0] * components_size[1] * components_size[2]

def part2(coords: list[tuple[int, int, int]]):
    distances: list[tuple[int, int, int]] = []
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            dist = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2 + (coords[i][2] - coords[j][2])**2
            distances.append((dist, i, j))
    heapq.heapify(distances)

    uf = UnionFind(len(coords))

    while True:
        dist, u, v = heapq.heappop(distances)
        if not uf.issame(u, v):
            uf.unite(u, v)
        if uf.size[uf.find(u)] == len(coords) or uf.size[uf.find(v)] == len(coords):
            return coords[u][0] * coords[v][0]
    
if __name__ == "__main__":
    main()