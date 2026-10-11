#include <cstdio>
#include <vector>

const int DIGITS = 10;

// ways[s]: strings of k digits with digit sum s
static std::vector<long long> sums(int k) {
    std::vector<long long> ways = {1};
    for (int i = 0; i < k; i++) {
        std::vector<long long> next(ways.size() + DIGITS - 1, 0);
        for (size_t s = 0; s < ways.size(); s++) {
            for (int d = 0; d < DIGITS; d++) {
                next[s + d] += ways[s];
            }
        }
        ways = next;
    }
    return ways;
}

// pairs of a k-digit and an m-digit string with equal digit sums
static long long matching(int k, int m) {
    std::vector<long long> a = sums(k), b = sums(m);
    long long total = 0;
    for (size_t s = 0; s < a.size() && s < b.size(); s++) {
        total += a[s] * b[s];
    }
    return total;
}

int main() {
    int n;
    scanf("%d", &n);
    // size[in the first half][odd] counts positions; lucky both ways means the
    // odd digits of the first half sum like the even ones of the second half,
    // and the even digits of the first half like the odd ones of the second
    int size[2][2] = {{0, 0}, {0, 0}};
    for (int p = 1; p <= n; p++) {
        size[p <= n / 2][p % 2]++;
    }
    long long first = matching(size[1][1], size[0][0]);
    long long second = matching(size[1][0], size[0][1]);
    printf("%lld\n", first * second);
}
