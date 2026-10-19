#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

std::pair<int, int> optimalTotals(int budget, int gift, int limit) {
    std::vector<int> current(budget + 1), opponent(budget + 1);
    for (int remaining = 1; remaining <= budget; ++remaining) {
        int best = remaining < limit ? gift : -1;
        int other = 0;
        for (int request = 1; request <= std::min(remaining, limit); ++request) {
            const int rest = remaining - request;
            const int ownTotal = request + opponent[rest];
            const int otherTotal = current[rest];
            if (ownTotal > best || (ownTotal == best && otherTotal < other)) {
                best = ownTotal;
                other = otherTotal;
            }
        }
        current[remaining] = best;
        opponent[remaining] = other;
    }
    return {current[budget], opponent[budget]};
}

int main() {
    int budget, gift, limit;
    std::cin >> budget >> gift >> limit;
    const auto answer = optimalTotals(budget, gift, limit);
    std::cout << answer.first << ' ' << answer.second << '\n';
    return 0;
}
