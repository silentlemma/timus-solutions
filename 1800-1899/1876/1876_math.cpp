#include <algorithm>
#include <cstdio>

const int LEGS = 40;

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) return 0;
    // either every right slipper turns up while the left legs are dressed,
    // or 39 rights do, and then every spare left slipper is thrown away
    // before the last right leg is dressed
    printf("%d\n", std::max(2 * b + LEGS, 2 * a + LEGS - 1));
    return 0;
}
