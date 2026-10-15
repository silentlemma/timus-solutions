#include <cstdio>
#include <vector>

const int LIMIT = 100000;
const int BASE = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> digits(LIMIT, 0), chosen;
    for (int i = 1; i < LIMIT; i++) digits[i] = digits[i / BASE] + i % BASE;
    // take numbers from the top whenever their digits still fit; the small
    // ones at the end fill any remainder, so the sum always comes out
    for (int i = LIMIT - 1; i >= 1 && n > 0; i--) {
        if (digits[i] <= n) {
            chosen.push_back(i);
            n -= digits[i];
        }
    }
    printf("%d\n", (int)chosen.size());
    for (size_t i = 0; i < chosen.size(); i++) {
        printf("%d%c", chosen[i], i + 1 < chosen.size() ? ' ' : '\n');
    }
}
