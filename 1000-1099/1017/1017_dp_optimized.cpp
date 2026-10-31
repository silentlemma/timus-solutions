#include <cstdio>

// n <= 500, so a fixed array avoids dynamic allocation
const int MAX_CUBES = 500;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    // ways[s]: sets of distinct step sizes, each used at most once, summing
    // to s; sizes are added one by one, going over s downwards
    long long ways[MAX_CUBES + 1] = {};
    ways[0] = 1;
    for (int size = 1; size <= n; size++)
        for (int s = n; s >= size; s--)
            ways[s] += ways[s - size];
    // a staircase needs at least two steps: drop the single step of n cubes
    printf("%lld\n", ways[n] - 1);
}
