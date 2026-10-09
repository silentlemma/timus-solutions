#include <algorithm>
#include <cstdio>
#include <vector>

const int TOP = 99999;

int main() {
    std::vector<int> a(TOP + 1, 0), best(TOP + 1, 0);
    a[1] = best[1] = 1;
    for (int i = 2; i <= TOP; i++) {
        a[i] = i % 2 == 0 ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
        best[i] = std::max(best[i - 1], a[i]);
    }
    int n;
    while (scanf("%d", &n) == 1 && n != 0)
        printf("%d\n", best[n]);
}
