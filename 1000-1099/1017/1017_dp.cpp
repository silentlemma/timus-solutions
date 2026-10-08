#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    // ways[s]: sets of distinct step sizes, each used at most once, summing
    // to s; sizes are added one by one, going over s downwards
    std::vector<long long> ways(n + 1, 0);
    ways[0] = 1;
    for (int size = 1; size <= n; size++)
        for (int s = n; s >= size; s--)
            ways[s] += ways[s - size];
    // a staircase needs at least two steps: drop the single step of n cubes
    printf("%lld\n", ways[n] - 1);
}
