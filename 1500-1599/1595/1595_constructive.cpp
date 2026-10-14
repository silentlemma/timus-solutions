#include <cstdio>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    unordered_set<long long> used;
    used.reserve(n);
    string out;
    long long total = 0, length = 0; // the sum and the number of terms so far
    for (long long m = 1; m <= n; m++) {
        // put a large x at position k and then m at k + 1: x must make the
        // sum divisible by k, and x + m divisible by k + 1
        long long k = length + 1;
        long long a = ((-total) % k + k) % k;
        long long b = ((-total - m) % (k + 1) + (k + 1)) % (k + 1);
        // x = a + k t, and k = -1 modulo k + 1, so t = a - b modulo k + 1
        long long step = k * (k + 1);
        long long x = a + k * (((a - b) % (k + 1) + (k + 1)) % (k + 1));
        if (x <= n)
            x += (n - x) / step * step + step;
        while (used.count(x))
            x += step;
        used.insert(x);
        out += to_string(x) + " " + to_string(m) + (m < n ? " " : "\n");
        total += x + m;
        length += 2;
    }
    fputs(out.c_str(), stdout);
}
