#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

int main() {
    const int SIZE = 3;
    int k;
    std::cin >> k;
    std::vector<std::set<std::string>> teams(k);
    for (auto &team : teams) {
        for (int j = 0; j < SIZE; j++) {
            std::string name;
            std::cin >> name;
            team.insert(name);
        }
    }
    // clash[i]: the teams sharing a member with team i, i itself included
    std::vector<int> clash(k, 0);
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            for (const auto &name : teams[i]) {
                if (teams[j].count(name)) {
                    clash[i] |= 1 << j;
                }
            }
        }
    }
    // the lowest team of a set is either skipped or taken with its clashes
    // out; both smaller sets come earlier in this order
    std::vector<int> best(1 << k, 0);
    for (int mask = 1; mask < (1 << k); mask++) {
        int i = __builtin_ctz(mask);
        best[mask] = std::max(best[mask & (mask - 1)], 1 + best[mask & ~clash[i]]);
    }
    std::cout << best[(1 << k) - 1] << "\n";
}
