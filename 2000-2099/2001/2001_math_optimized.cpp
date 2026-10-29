#include <cstdio>

constexpr int REQUIRED_READINGS = 4;

int main() {
    int a1, b1, b2, a3;
    // the combined weights a2 and b3 are skipped with %*d
    if (scanf("%d %d %*d %d %d %*d", &a1, &b1, &b2, &a3) != REQUIRED_READINGS)
        return 0;
    printf("%d %d\n", a1 - a3, b1 - b2);
    return 0;
}
