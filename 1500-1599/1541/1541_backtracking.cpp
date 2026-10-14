#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>
using namespace std;

const int FASTEST = 100000; // no speed above this
const int MOST = 19;        // K < 20 leagues
const double SLACK = 1e-9;  // floating point margin for the pruning bound
const long long BIG = 1LL << 61;

double harmonic[FASTEST + 2];
vector<long long> path;

// the largest sum of count unit fractions with denominators from start
double most(long long start, int count) {
    long long end = min(start + count - 1, (long long)FASTEST);
    return start <= end ? harmonic[end] - harmonic[start - 1] : 0;
}

// writes p / q as left or fewer unit fractions above 1 / last
bool decompose(long long p, long long q, long long last, int left) {
    if (p == 0)
        return true;
    if (left == 0)
        return false;
    long long start = max(last + 1, (q + p - 1) / p); // 1 / d must fit into p / q
    // left fractions of 1 / d at most
    long long stop = q > BIG / left ? FASTEST : min((long long)FASTEST, left * q / p);
    if (start > stop || most(start, left) + SLACK < (double)p / q)
        return false;
    for (long long d = start; d <= stop; d++) {
        if ((double)p / q - 1.0 / d > most(d + 1, left - 1) + SLACK)
            continue;
        // keep every fraction within 64 bits
        if (q > BIG / d || p > BIG / d)
            continue;
        long long np = p * d - q, nq = q * d, g = gcd(np, nq);
        path.push_back(d);
        if (decompose(np / g, nq / g, d, left - 1))
            return true;
        path.pop_back();
    }
    return false;
}

int main() {
    long long m, n;
    if (scanf("%lld %lld", &m, &n) != 2)
        return 0;
    // M / N hours over legs of one league each: M / N = 1 / V1 + ... + 1 / VK
    // with distinct whole speeds, a sum of distinct unit fractions
    for (int d = 1; d <= FASTEST; d++)
        harmonic[d] = harmonic[d - 1] + 1.0 / d;
    // the fewest fractions first keeps the search small
    for (int k = 1; k <= MOST; k++)
        if (decompose(m, n, 0, k)) {
            printf("%d\n", (int)path.size());
            for (size_t i = path.size(); i-- > 0;)
                printf(i + 1 < path.size() ? " %lld" : "%lld", path[i]);
            printf("\n");
            return 0;
        }
    printf("-1\n");
}
