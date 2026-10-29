#include <cstdio>

// sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
void print_sine(int n) {
    for (int k = 1; k <= n; ++k) {
        std::printf("sin(%d", k);
        if (k < n)
            std::putchar(k % 2 ? '-' : '+');
    }
    for (int k = 0; k < n; ++k)
        std::putchar(')');
}

// the expression is printed piece by piece instead of being built in a string
int main() {
    int n;
    std::scanf("%d", &n);
    for (int k = 1; k < n; ++k)
        std::putchar('(');
    for (int i = 1; i <= n; ++i) {
        print_sine(i);
        std::printf("+%d", n - i + 1);
        if (i < n)
            std::putchar(')');
    }
    std::putchar('\n');
}
