#include <algorithm>
#include <cstdio>

const int SIDES = 2;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 0;
    // every minute fries at most k of the 2n sides, and one steak takes
    // two minutes on its own; rotating sides cyclically reaches both bounds
    printf("%d\n", std::max(SIDES, (SIDES * n + k - 1) / k));
    return 0;
}
