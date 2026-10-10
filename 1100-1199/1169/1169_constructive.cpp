#include <bitset>
#include <cstdio>
#include <vector>

const int SMALLEST_CYCLE = 3;
const int MAX_PAIRS = 100 * 99 / 2;

int pairs(int s) { return s * (s - 1) / 2; }

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // a pair is not critical exactly when both computers lie in the same
    // 2-edge-connected part; such a part has one computer or at least three,
    // so the sizes must split n with pairs(size) adding up to pairs(n) - k
    int target = pairs(n) - k;
    std::vector<int> sizes = {1};
    for (int s = SMALLEST_CYCLE; s <= n; s++) {
        sizes.push_back(s);
    }
    // reach[m] has bit t set when m computers can be split with t inner pairs
    std::vector<std::bitset<MAX_PAIRS + 1>> reach(n + 1);
    reach[0][0] = 1;
    for (int m = 1; m <= n; m++) {
        for (int s : sizes) {
            if (s <= m) {
                reach[m] |= reach[m - s] << pairs(s);
            }
        }
    }
    if (target < 0 || !reach[n][target]) {
        printf("-1\n");
        return 0;
    }
    std::vector<int> parts;
    for (int m = n, t = target; m > 0;) {
        for (int s : sizes) {
            if (s <= m && pairs(s) <= t && reach[m - s][t - pairs(s)]) {
                parts.push_back(s);
                m -= s;
                t -= pairs(s);
                break;
            }
        }
    }
    // each part is a cycle (or a single computer), and bridges join the first
    // computers of consecutive parts
    int first = 1, prev = 0;
    for (int s : parts) {
        if (s > 1) {
            for (int j = 0; j < s; j++) {
                printf("%d %d\n", first + j, first + (j + 1) % s);
            }
        }
        if (prev) {
            printf("%d %d\n", prev, first);
        }
        prev = first;
        first += s;
    }
}
