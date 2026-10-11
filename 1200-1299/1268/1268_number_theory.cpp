#include <cstdio>
#include <vector>

const int LIMIT = 1 << 16; // N < 65536

long long power(long long b, long long e, long long m) {
    long long r = 1;
    for (b %= m; e > 0; e >>= 1) {
        if (e & 1)
            r = r * b % m;
        b = b * b % m;
    }
    return r;
}

int main() {
    // smallest prime factor of every number below the limit
    std::vector<int> spf(LIMIT), known(LIMIT);
    for (int i = 0; i < LIMIT; i++)
        spf[i] = i;
    for (int i = 2; i * i < LIMIT; i++)
        if (spf[i] == i)
            for (int j = i * i; j < LIMIT; j += i)
                if (spf[j] == j)
                    spf[j] = i;
    int t;
    scanf("%d", &t);
    while (t--) {
        int p;
        scanf("%d", &p);
        if (!known[p]) {
            // g is a primitive root when no g^((p-1)/q) is 1 for a prime q | p-1
            std::vector<int> quotients;
            for (int rest = p - 1; rest > 1;) {
                int q = spf[rest];
                quotients.push_back((p - 1) / q);
                while (rest % q == 0)
                    rest /= q;
            }
            int g = p - 1;
            for (;; g--) {
                bool root = true;
                for (int e : quotients)
                    if (power(g, e, p) == 1) {
                        root = false;
                        break;
                    }
                if (root)
                    break;
            }
            known[p] = g;
        }
        printf("%d\n", known[p]);
    }
}
