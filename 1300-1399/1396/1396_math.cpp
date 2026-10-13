#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> Pair;

const int BITS = 61;   // every n is below 2^60, and a lowered bit leaves at most 60 free ones
const int ENDINGS = 4; // per first bit: as is, last bit 1, last two 11, last two 01

// (a_m, a_m+1) -> (a_2m+bit, a_2m+bit+1)
Pair step(Pair v, int bit) {
    return bit == 0 ? Pair(v.first, v.first + v.second) : Pair(v.first + v.second, v.second);
}

int main() {
    // maps[r]: (p, q) with a = p a_m + q a_m+1 after each candidate suffix of
    // r free bits: alternating bits with the last one or two changed
    vector<vector<Pair>> maps(BITS);
    for (int r = 0; r < BITS; r++)
        for (int first = 0; first < 2; first++)
            for (int e = 0; e < ENDINGS; e++) {
                vector<int> bits(r);
                for (int k = 0; k < r; k++)
                    bits[k] = (first + k) % 2;
                if (e == 1 && r >= 1)
                    bits[r - 1] = 1;
                if (e >= 2 && r >= 2) {
                    bits[r - 2] = e == 2;
                    bits[r - 1] = 1;
                }
                Pair p(1, 0), q(0, 1);
                for (int b : bits) {
                    p = step(p, b);
                    q = step(q, b);
                }
                maps[r].push_back(Pair(p.first, q.first));
            }
    ll n;
    while (scanf("%lld", &n) == 1 && n != 0) {
        int length = 0;
        while (length < BITS && (n >> length) > 0)
            length++;
        ll best = 0;
        Pair v(0, 1); // (a_0, a_1) for the empty prefix
        for (int k = length - 1; k >= 0; k--) {
            int bit = n >> k & 1;
            if (bit) {
                // lower this bit to 0: the k bits below are free
                Pair low = step(v, 0);
                for (auto &pq : maps[k])
                    best = max(best, pq.first * low.first + pq.second * low.second);
            }
            v = step(v, bit);
        }
        printf("%lld\n", max(best, v.first));
    }
}
