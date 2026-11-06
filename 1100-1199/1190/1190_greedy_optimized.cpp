#include <cstdio>

constexpr int WHOLE = 10000;

int main() {
    int count;
    if (std::scanf("%d", &count) != 1) {
        return 0;
    }
    int low = 0;
    int high = 0;
    int ceiling = WHOLE;
    int unknown = 0;
    for (int i = 0; i < count; ++i) {
        int shown;
        std::scanf("%*s%d", &shown);
        if (!shown) {
            ++unknown;
            continue;
        }
        int share;
        std::scanf("%d", &share);
        // Each run of unknown shares lies between its two printed neighbours.
        low += (unknown + 1) * share;
        high += unknown * ceiling + share;
        ceiling = share;
        unknown = 0;
    }
    low += unknown;
    high += unknown * ceiling;
    std::puts(low <= WHOLE && WHOLE <= high ? "YES" : "NO");
}
