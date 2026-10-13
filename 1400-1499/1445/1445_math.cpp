#include <algorithm>
#include <cstdio>

int main() {
    int n, biggest = 0, total = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int size;
        scanf("%d", &size);
        biggest = std::max(biggest, size);
        total += size;
    }
    // the biggest company needs gifts from outside it: prepared or from the others
    int best = std::max(1, 2 * biggest - total);
    // in the worst order the biggest company comes first, and that many always suffice
    printf("%d %d\n", best, biggest);
}
