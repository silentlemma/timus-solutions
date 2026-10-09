#include <cstdio>
#include <vector>

// x^n mod m by repeated squaring
int power(int x, int n, int m) {
    int result = 1 % m;
    for (x %= m; n > 0; n >>= 1) {
        if (n & 1)
            result = result * x % m;
        x = x * x % m;
    }
    return result;
}

int main() {
    int n, m, y;
    if (scanf("%d %d", &n, &m) != 2 || scanf("%d", &y) != 1)
        return 0;
    // only M candidates; a Y of M or more is never a remainder
    std::vector<int> roots;
    for (int x = 0; x < m; x++)
        if (power(x, n, m) == y)
            roots.push_back(x);
    if (roots.empty())
        printf("-1\n");
    for (size_t i = 0; i < roots.size(); i++)
        printf(i + 1 < roots.size() ? "%d " : "%d\n", roots[i]);
}
