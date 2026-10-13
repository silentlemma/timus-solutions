#include <cstdio>
#include <vector>

const int DIGITS = 9; // numbers below 10^9 have at most nine digits
const int BASE = 10;

int main() {
    int target = 0;
    if (scanf("%d", &target) != 1)
        return 0;
    // ways[s]: digit strings of the current length with digit sum s
    std::vector<long long> ways(1, 1);
    for (int len = 0; len < DIGITS; len++) {
        std::vector<long long> next(ways.size() + BASE - 1, 0);
        for (size_t s = 0; s < ways.size(); s++)
            for (int d = 0; d < BASE; d++)
                next[s + d] += ways[s];
        ways = next;
    }
    // 10^9 itself has digit sum 1; zero is not counted since S >= 1
    printf("%lld\n", ways[target] + (target == 1 ? 1 : 0));
    return 0;
}
