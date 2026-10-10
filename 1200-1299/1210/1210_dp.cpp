#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const int INF = 1 << 30;

// The next number of the input, skipping the "*" lines between blocks.
static int next() {
    std::string token;
    do {
        std::cin >> token;
    } while (token == "*");
    return std::stoi(token);
}

int main() {
    int levels = next();
    // the cheapest cost of reaching each planet of the current level
    std::vector<int> cost(1, 0);
    for (int level = 0; level < levels; level++) {
        int k = next();
        std::vector<int> nxt(k, INF);
        for (int planet = 0; planet < k; planet++) {
            for (int src = next(); src != 0; src = next()) {
                int price = next();
                if (cost[src - 1] < INF) {
                    nxt[planet] = std::min(nxt[planet], cost[src - 1] + price);
                }
            }
        }
        cost = nxt;
    }
    std::cout << *std::min_element(cost.begin(), cost.end()) << "\n";
}
