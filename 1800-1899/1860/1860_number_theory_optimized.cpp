#include <cstdint>
#include <cstdio>
#include <vector>

constexpr uint32_t MOD = 1000000007;
constexpr int BYTE_BITS = 8;

int main() {
    int n;
    if (std::scanf("%d", &n) != 1)
        return 0;
    std::vector<uint32_t> fib(n + 1);
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        uint32_t value = fib[i - 1] + fib[i - 2];
        fib[i] = value >= MOD ? value - MOD : value;
    }
    std::vector<uint8_t> composite((n / 2 + BYTE_BITS) / BYTE_BITS);
    uint64_t answer = 1;
    for (int p = 2; p <= n; p += p == 2 ? 1 : 2) {
        int odd = p / 2;
        if (p != 2 && (composite[odd / BYTE_BITS] >> (odd % BYTE_BITS) & 1))
            continue;
        if (p != 2 && p <= n / p) {
            for (int multiple = p * p; multiple <= n; multiple += 2 * p) {
                int index = multiple / 2;
                composite[index / BYTE_BITS] |= uint8_t(1U << (index % BYTE_BITS));
            }
        }
        uint64_t exponent = 0;
        for (int power = p; power <= n;) {
            for (int k = power; k <= n; k += power)
                exponent += fib[n - k + 1];
            if (power > n / p)
                break;
            power *= p;
        }
        answer = answer * (exponent % MOD + 1) % MOD;
    }
    std::printf("%llu\n", (unsigned long long)answer);
}
