#include <cstdio>

int main() {
    int size, limit;
    scanf("%d %d", &size, &limit);
    int prefix = 0;
    // Since the total excess equals limit, a negative prefix makes its
    // suffix too heavy; a prefix above limit itself violates the bound.
    for (int i = 0; i < size; i++) {
        int value;
        scanf("%d", &value);
        prefix += value - 1;
        if (prefix < 0 || prefix > limit) {
            puts("NO");
            return 0;
        }
    }
    puts("YES");
}
