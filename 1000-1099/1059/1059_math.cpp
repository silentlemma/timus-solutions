#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // Horner's scheme: ((a0 * X + a1) * X + a2) ... in reverse Polish notation
    printf("0\n");
    for (int i = 1; i <= n; i++)
        printf("X\n*\n%d\n+\n", i);
}
