#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    int step = 0;
    // the marks are counted as they are read, without storing them
    for (int ch = getchar(); ch != EOF; ch = getchar()) {
        if (ch == '!') {
            ++step;
        }
    }
    // multiply n, n - step, ... while the factor stays positive
    // n <= 10, so the product is at most 10! = 3628800 and fits in an int
    int product = 1;
    for (int factor = n; factor > 0; factor -= step) {
        product *= factor;
    }
    printf("%d\n", product);
}
