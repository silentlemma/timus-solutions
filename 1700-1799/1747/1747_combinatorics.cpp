#include <cstdio>
#include <iostream>

int main() {
    long long n, p;
    std::cin >> n >> p;
    // the route is the capital, then the other n - 1 = m cities twice each
    // with no city twice in a row, then the capital; such words over m
    // pairs obey a(m) = m (2m - 1) a(m - 1) + m (m - 1) a(m - 2)
    long long before = 1 % p, current = 0;
    for (long long m = 2; m < n; m++) {
        long long next = (m * (2 * m - 1) % p * current + m * (m - 1) % p * before) % p;
        before = current;
        current = next;
    }
    printf("%lld\n", current % p);
}
