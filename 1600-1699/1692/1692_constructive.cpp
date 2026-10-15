#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    // every two flags need a common color, and a color on at most two flags
    // serves one pair only, so k(k - 1) / 2 <= n; one color per pair is enough
    int k = 1;
    while ((k + 1) * k / 2 <= n) {
        k++;
    }
    std::vector<std::vector<int>> flags(k);
    int color = 0;
    for (int a = 0; a < k; a++) {
        for (int b = a + 1; b < k; b++) {
            color++;
            flags[a].push_back(color);
            flags[b].push_back(color);
        }
    }
    printf("%d\n", k);
    for (const auto& flag : flags) {
        printf("%d", (int)flag.size());
        for (int c : flag) {
            printf(" %d", c);
        }
        printf("\n");
    }
}
