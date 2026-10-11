#include <cstdio>
#include <utility>

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    // each turn of the loop swaps x and y, and there are x + y turns; the
    // sum survives, so an odd sum of positive numbers means one swap
    if (x > 0 && y > 0 && (x + y) % 2 == 1) {
        std::swap(x, y);
    }
    printf("%d %d\n", x, y);
}
