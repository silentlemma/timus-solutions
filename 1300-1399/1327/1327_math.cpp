#include <cstdio>

int main() {
    int a = 0, b = 0;
    if (scanf("%d %d", &a, &b) != 2)
        return 0;
    // the fuses burn on the odd days; (x + 1) / 2 odd days are in 1..x
    printf("%d\n", (b + 1) / 2 - a / 2);
    return 0;
}
