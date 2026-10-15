#include <cstdio>
#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;
    // with first boxes 1..n and second boxes spaced n apart above them,
    // every sum a + b names its pair, so no two gifts can weigh the same
    for (int i = 1; i <= n; i++) printf("%d%c", i, i < n ? ' ' : '\n');
    for (int j = 0; j < m; j++) printf("%d%c", (j + 1) * n + 1, j + 1 < m ? ' ' : '\n');
}
