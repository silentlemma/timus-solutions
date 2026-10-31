#include <cstdio>

long long smaller(long long a, long long b) { return a < b ? a : b; }

void order(long long &a, long long &b) {
    if (a > b) {
        long long temporary = a;
        a = b;
        b = temporary;
    }
}

int main() {
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);
    order(a, b);
    order(b, c);
    order(a, b);
    long long gap = smaller(b - a, c - b);
    int asked = 1;
    while (gap > 0) {
        ++asked;
        // gap <= b - a < b: its only possible neighbors are the two smallest piles.
        // all other gaps are unchanged, so retain just those piles and the minimum.
        long long difference = gap > a ? gap - a : a - gap;
        long long next = smaller(gap, smaller(difference, b - gap));
        if (gap < a) {
            b = a;
            a = gap;
        } else {
            b = gap;
        }
        gap = next;
    }
    printf("%d\n", asked);
}
