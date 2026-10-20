#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    std::vector<int> s(n);
    long long total = 0;
    int largest = 0;
    for (auto &x : s) {
        scanf("%d", &x);
        total += x;
        largest = std::max(largest, x);
    }
    // Every sponsor needs its own problems, and no problem holds more than k.
    int m = std::max<long long>(largest, (total + k - 1) / k);
    // Write the sponsors one after another and deal the copies round robin:
    // a sponsor's copies are consecutive and at most m, so they land in
    // different problems, and every problem gets at most ceil(total / m) <= k.
    std::vector<std::vector<int>> problems(m);
    long long position = 0;
    for (int i = 0; i < n; i++)
        for (int c = 0; c < s[i]; c++) problems[position++ % m].push_back(i + 1);
    printf("%d\n", m);
    for (auto &p : problems) {
        printf("%d", (int)p.size());
        for (int x : p) printf(" %d", x);
        printf("\n");
    }
    return 0;
}
