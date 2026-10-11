#include <cstdio>
#include <vector>

const double PERCENT = 100.0;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<int> votes(n + 1);
    for (int i = 0, c; i < m; i++) {
        scanf("%d", &c);
        votes[c]++;
    }
    for (int i = 1; i <= n; i++)
        printf("%.2f%%\n", PERCENT * votes[i] / m);
}
