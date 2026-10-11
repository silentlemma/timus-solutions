#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> stones(n), order(n);
    for (int i = 0; i < n; i++)
        scanf("%d", &stones[i]);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) { return stones[a] < stones[b]; });
    // a swap moves a stone K + 1 places, so K + 1 must divide every stone's
    // distance to its place, in one order or the other; all weights differ
    int best = 0;
    for (int down = 0; down < 2; down++) {
        int g = 0;
        for (int place = 0; place < n; place++) {
            int target = down ? n - 1 - place : place;
            g = std::gcd(g, std::abs(target - order[place]));
        }
        best = std::max(best, g ? g - 1 : n - 1);
    }
    printf("%d\n", best);
}
