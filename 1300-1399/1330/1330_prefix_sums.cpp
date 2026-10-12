#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n = 0, q = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // before[i] is the sum of the first i readings
    std::vector<long long> before(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long k = 0;
        if (scanf("%lld", &k) != 1)
            return 0;
        before[i] = before[i - 1] + k;
    }
    if (scanf("%d", &q) != 1)
        q = 0;
    std::string out;
    for (int t = 0; t < q; t++) {
        int i = 0, j = 0;
        if (scanf("%d %d", &i, &j) != 2)
            break;
        out += std::to_string(before[j] - before[i - 1]);
        out += '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
