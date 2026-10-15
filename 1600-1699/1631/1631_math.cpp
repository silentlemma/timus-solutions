#include <cmath>
#include <cstdio>

int main() {
    long long m, n;
    if (scanf("%lld %lld", &m, &n) != 2)
        return 0;
    // m * n moves close the tour; m + n + 1 of them are diagonal
    long long diagonal = m + n + 1;
    printf("%.12f\n", m * n + diagonal * (std::sqrt(2.0) - 1));
}
