#include <cstdio>

int main() {
    long long n, p;
    while (scanf("%lld%lld", &n, &p) == 2 && (n || p)) {
        long long result = n >= p ? 0 : 1, i = 2;
        // At most (2e9-1)*10000*9999 < 2e17, within signed64.
        for (; i + 1 <= n && result; i += 2)
            result = result * i * (i + 1) % p;
        if (i <= n && result)
            result = result * i % p;
        printf("%lld\n", result);
    }
}
