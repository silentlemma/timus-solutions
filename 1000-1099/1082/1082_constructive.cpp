#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // on sorted numbers every partition peels off just the first one
    for (int i = 1; i <= n; i++)
        printf("%d%c", i, i < n ? ' ' : '\n');
}
