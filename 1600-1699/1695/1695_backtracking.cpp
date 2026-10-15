#include <bitset>
#include <cstdio>
#include <unordered_map>
#include <vector>

typedef unsigned long long u64;
const int WORD = 64;  // bits in a mask, and room for a row of the table

int n;
std::vector<u64> enemy;
std::vector<u64> path;  // independent sets of a path on s vertices
std::unordered_map<u64, u64> memo;

int bits(u64 x) { return std::bitset<WORD>(x).count(); }

int lowest(u64 x) { return bits((x & -x) - 1); }

u64 count(u64 mask) {
    if (mask == 0) {
        return 1;
    }
    auto it = memo.find(mask);
    if (it != memo.end()) {
        return it->second;
    }
    // split into connected parts, which multiply
    u64 low = mask & -mask, part = low, frontier = low;
    while (frontier) {
        u64 bit = frontier & -frontier;
        frontier ^= bit;
        u64 grow = enemy[lowest(bit)] & mask & ~part;
        part |= grow;
        frontier |= grow;
    }
    u64 result;
    if (part != mask) {
        result = count(part) * count(mask & ~part);
    } else {
        int size = bits(mask), pivot = -1, most = -1, least = size;
        for (u64 rest = mask; rest; rest &= rest - 1) {
            int v = lowest(rest), degree = bits(enemy[v] & mask);
            least = degree < least ? degree : least;
            if (degree > most) {
                pivot = v;
                most = degree;
            }
        }
        if (least == size - 1) {
            result = size + 1;  // all pairs are enemies: the empty set or one robot
        } else if (most <= 2) {
            // a path, or a cycle: independent sets of a path on s - 1 plus s - 3
            const int CYCLE_CUT = 3;
            result = least <= 1 ? path[size] : path[size - 1] + path[size - CYCLE_CUT];
        } else {
            // branch on a vertex of most enemies: leave it out, or take it
            // and drop all its enemies
            u64 bit = 1ULL << pivot;
            result = count(mask & ~bit) + count(mask & ~(enemy[pivot] | bit));
        }
    }
    memo[mask] = result;
    return result;
}

int main() {
    scanf("%d", &n);
    enemy.assign(n, 0);
    for (int i = 0; i < n; i++) {
        char row[WORD];
        scanf("%s", row);
        for (int j = 0; j < n; j++) {
            if (i != j && row[j] == '0') {
                enemy[i] |= 1ULL << j;
            }
        }
    }
    // a working group is a clique of friends, that is an independent set of
    // the graph of non-friends; every group plus the empty one is a day, so
    // the day of rusting is the number of independent sets, empty included
    path = {1, 2};
    for (int s = 2; s <= n; s++) {
        path.push_back(path[s - 1] + path[s - 2]);
    }
    printf("%llu\n", count((1ULL << n) - 1));
}
