#include <cstdio>
#include <vector>

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 0;
    // value[i] and locks[i]: the sum of values and the number of locked
    // buffers among the first i buffers
    std::vector<long long> value(n + 1, 0);
    std::vector<int> locks(n + 1, 0);
    for (int i = 1; i <= n;) {
        int c = getchar();
        if (c == EOF)
            break;
        if (c == '*') {
            locks[i] = locks[i - 1] + 1;
            value[i] = value[i - 1];
        } else if (c >= '0' && c <= '9') {
            locks[i] = locks[i - 1];
            value[i] = value[i - 1] + (c - '0');
        } else {
            continue;
        }
        i++;
    }
    // the windows [l, l + k - 1] without locks; the first cheapest wins
    int best = 0;
    long long best_value = 0;
    for (int l = 1; l + k - 1 <= n; l++) {
        int r = l + k - 1;
        if (locks[r] != locks[l - 1])
            continue;
        long long v = value[r] - value[l - 1];
        if (best == 0 || v < best_value) {
            best = l;
            best_value = v;
        }
    }
    printf("%d\n", best);
}
