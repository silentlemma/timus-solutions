#include <algorithm>
#include <cstdio>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

std::vector<std::string> animals, rows;
std::vector<int> owner;

int build(int lo, int hi) {
    if (owner[lo] == owner[hi - 1]) {
        rows.push_back(animals[owner[lo]]);
    } else {
        int mid = (lo + hi) / 2;
        int left = build(lo, mid);
        int right = build(mid, hi);
        rows.push_back(std::to_string(left) + " " + std::to_string(right));
    }
    return rows.size();
}

int main() {
    std::string name;
    std::cin >> name;
    size_t start = 0;
    while (true) {
        size_t dash = name.find('-', start);
        animals.push_back(name.substr(start, dash - start));
        if (dash == std::string::npos) break;
        start = dash + 1;
    }
    std::vector<int> num(animals.size()), den(animals.size());
    int leaves = 1;
    for (size_t i = 0; i < animals.size(); i++) {
        char slash;
        std::cin >> num[i] >> slash >> den[i];
        int g = std::gcd(num[i], den[i]);
        num[i] /= g;
        den[i] /= g;
        // a crossing halves every share, so only shares with a power of
        // two below can come out
        if (den[i] & (den[i] - 1)) {
            printf("No solution\n");
            return 0;
        }
        leaves = std::max(leaves, den[i]);
    }
    // give each animal its share of the equal leaves, in order, and cross
    // halves of the leaves; a half that is one animal is just that animal
    for (size_t i = 0; i < animals.size(); i++) {
        owner.insert(owner.end(), num[i] * (leaves / den[i]), i);
    }
    build(0, leaves);
    printf("%d\n", (int)rows.size());
    for (const auto &row : rows) printf("%s\n", row.c_str());
}
