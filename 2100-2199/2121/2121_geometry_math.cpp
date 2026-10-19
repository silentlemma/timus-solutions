#include <cstdio>

constexpr unsigned long long SIDE_FACTOR = 4;  // the area is 4a - 1/3

int main() {
    unsigned long long a;
    scanf("%llu", &a);
    // 4a - 1/3 = (4a - 1) + 2/3, and 2/3 rounds to 0.6666666667
    printf("%llu.6666666667\n", SIDE_FACTOR * a - 1);
    return 0;
}
