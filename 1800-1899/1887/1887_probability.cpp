#include <cstdio>
#include <vector>

using namespace std;

const int PRIME = 11;
const int DIGITS = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<int> a(n), b(n), c(n);
    for (int& v : a) scanf("%d", &v);
    for (int& v : b) scanf("%d", &v);
    for (int& v : c) scanf("%d", &v);
    // chance[r]: probability that the product so far is r modulo 11
    vector<double> chance(PRIME, 0);
    chance[1] = 1;
    for (int i = 0; i < n; i++) {
        vector<double> next(PRIME, 0);
        for (int x = 0; x < DIGITS; x++) {
            int factor = (a[i] * x * x + b[i] * x + c[i]) % PRIME;
            for (int r = 0; r < PRIME; r++) next[r * factor % PRIME] += chance[r] / DIGITS;
        }
        chance = next;
    }
    vector<double> p(DIGITS, 0);
    for (int r = 0; r < PRIME; r++) p[r % DIGITS] += chance[r];
    for (double q : p) {
        // only positive terms are ever added, so an impossible digit stays 0
        if (q == 0) {
            puts("-1");
            return 0;
        }
    }
    // expected draws from the set of digits seen to all ten: a draw of a
    // missing digit moves on, others repeat; the chance to move on is summed
    // directly so that small probabilities keep their precision
    int full = (1 << DIGITS) - 1;
    vector<double> expect(full + 1, 0);
    for (int mask = full - 1; mask >= 0; mask--) {
        double move = 0, sum = 1;
        for (int d = 0; d < DIGITS; d++) {
            if (mask >> d & 1) continue;
            move += p[d];
            sum += p[d] * expect[mask | 1 << d];
        }
        expect[mask] = sum / move;
    }
    printf("%.10f\n", expect[0]);
    return 0;
}
