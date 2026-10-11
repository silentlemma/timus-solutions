#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>

// the cells a ship may not use: rows top..bottom, columns left..right
struct Zone {
    long long top, bottom, left, right;
};

// Places for a ship lying along the rows of a rows x cols board.
static long long countLines(long long rows, long long cols, const std::vector<Zone> &zones,
                            long long k) {
    std::set<long long> cuts = {1, rows + 1};
    for (const Zone &z : zones) {
        for (long long e : {z.top, z.bottom + 1}) {
            if (e > 1 && e <= rows) {
                cuts.insert(e);
            }
        }
    }
    std::vector<long long> c(cuts.begin(), cuts.end());
    long long total = 0;
    // rows between two cuts meet the same zones, so they count the same
    for (size_t i = 0; i + 1 < c.size(); i++) {
        long long top = c[i];
        std::vector<std::pair<long long, long long>> spans;
        for (const Zone &z : zones) {
            if (z.top <= top && top <= z.bottom) {
                spans.push_back({z.left, z.right});
            }
        }
        std::sort(spans.begin(), spans.end());
        spans.push_back({cols + 1, cols + 1});
        long long free = 0, start = 1;
        for (auto [left, right] : spans) {
            if (left > start) {
                free += std::max(0LL, left - start - k + 1);
            }
            start = std::max(start, right + 1);
        }
        total += free * (c[i + 1] - top);
    }
    return total;
}

int main() {
    long long n, m, k;
    int ships;
    std::cin >> n >> m >> ships;
    std::vector<Zone> zones;
    for (int i = 0; i < ships; i++) {
        long long col, row, size;
        std::string way;
        std::cin >> col >> row >> size >> way;
        long long bottom = way == "V" ? row + size - 1 : row;
        long long right = way == "V" ? col : col + size - 1;
        // no other ship may touch this one, even at a corner
        zones.push_back({row - 1, bottom + 1, col - 1, right + 1});
    }
    std::cin >> k;
    long long total = countLines(n, m, zones, k);
    if (k > 1) {
        std::vector<Zone> flipped;
        for (const Zone &z : zones) {
            flipped.push_back({z.left, z.right, z.top, z.bottom});
        }
        total += countLines(m, n, flipped, k);
    }
    std::cout << total << "\n";
}
