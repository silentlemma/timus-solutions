#include <cstdio>

const int FOUR = 4; // one corner inside: 4 points, one triangle on each side
const int FIVE = 5; // two corners inside: 5 points, one triangle per apex
const int SIX = 6;  // three corners inside: 6 points, the three long diagonals

long long choose(long long n, int k) {
    long long c = 1;
    for (int i = 1; i <= k; i++)
        c = c * (n - k + i) / i; // stays below C(n, k) * n
    return c;
}

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    // a triangle is fixed by the set of chord ends it uses, and a set of
    // k points on the circle gives a fixed number of triangles
    printf("%lld\n", choose(n, SIX) + FIVE * choose(n, FIVE) + FOUR * choose(n, FOUR));
}
