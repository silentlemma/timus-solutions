#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    if (n == 2) {
        printf("2\n1 1\n");
        return 0;
    }
    printf("%d\n", 2 * (n - 2));
    // Two opposite sweeps catch the two possible initial position parities.
    // Generate the same construction directly, without a vector or iostream.
    for (int p = 2; p < n; p++)
        printf("%d ", p);
    for (int p = n - 1; p >= 2; p--)
        printf("%d%c", p, p == 2 ? '\n' : ' ');
}
