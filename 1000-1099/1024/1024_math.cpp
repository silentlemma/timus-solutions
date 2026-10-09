#include <cstdio>
#include <numeric>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    std::vector<int> p(n + 1);
    for (int i = 1; i <= n; i++)
        if (scanf("%d", &p[i]) != 1)
            return 1;
    // P^k is the identity exactly when k is a multiple of every cycle length:
    // the order is their least common multiple
    std::vector<bool> seen(n + 1, false);
    long long order = 1;
    for (int i = 1; i <= n; i++) {
        long long length = 0;
        for (int j = i; !seen[j]; j = p[j]) {
            seen[j] = true;
            length++;
        }
        if (length > 0)
            order = std::lcm(order, length);
    }
    printf("%lld\n", order);
}
