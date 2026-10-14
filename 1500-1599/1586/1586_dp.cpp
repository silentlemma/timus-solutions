#include <cstdio>
#include <vector>
using namespace std;

const long long MOD = 1000000009;
const int LOW = 100, HIGH = 1000; // the three-digit numbers
const int PAIRS = 100;            // the last two digits
const int BASE = 10;
const int WINDOW = 3; // neighbouring digits that form a prime

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> primes;
    for (int p = LOW; p < HIGH; p++) {
        bool prime = true;
        for (int d = 2; d * d <= p; d++)
            if (p % d == 0)
                prime = false;
        if (prime)
            primes.push_back(p);
    }
    // ways[t]: numbers of the length so far that end in the two digits t and
    // whose every three neighbouring digits form a three-digit prime
    vector<long long> ways(PAIRS, 0);
    for (int p : primes)
        ways[p % PAIRS]++;
    for (int step = WINDOW; step < n; step++) {
        vector<long long> next(PAIRS, 0);
        // a prime abc extends a number ending in ab to one ending in bc
        for (int p : primes)
            next[p % PAIRS] = (next[p % PAIRS] + ways[p / BASE]) % MOD;
        ways = next;
    }
    long long total = 0;
    for (long long w : ways)
        total = (total + w) % MOD;
    printf("%lld\n", total);
}
