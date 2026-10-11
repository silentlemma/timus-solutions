#include <algorithm>
#include <cstdio>

int main() {
    int s, n;
    scanf("%d %d", &s, &n);
    // the sum of A_i - 1 over every segment must stay at most N, so only the
    // largest such sum matters: Kadane's scan keeps the best one ending here
    int best = 0, here = 0;
    for (int i = 0; i < s; i++) {
        int a;
        scanf("%d", &a);
        here = std::max(here, 0) + a - 1;
        best = std::max(best, here);
    }
    puts(best <= n ? "YES" : "NO");
}
