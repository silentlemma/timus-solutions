#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>

using Integer = std::uint64_t;
using Wide = __uint128_t;
constexpr Integer MOD = 1000000007;

Wide columns(Integer n, Integer m, Integer k) {
    Integer end = n * m - 1;
    Wide total = 0;
    for (Integer c = 0; c < n; ++c) {
        Integer lower = c * m, upper = lower + m;
        Integer first = lower / k + 1, last = std::min(upper, end) / k;
        if (last < first)
            continue;
        Integer count = last - first + 1, a, b;
        if (c % 2 == 0) {
            a = first * k - lower;
            b = last * k - lower;
        } else {
            a = upper - first * k;
            b = upper - last * k;
            if (b == 0)
                ++total; // A bottom transition has half-detour one, not zero.
        }
        total += static_cast<Wide>(count) * (a + b) / 2;
    }
    return total;
}

Wide residues(Integer n, Integer m, Integer k) {
    Integer period = 2 * m, g = std::gcd(k, period), length = period / g;
    Integer refills = (n * m - 1) / k, remainder = refills % length;
    Integer reverse = length - remainder - 1, work = std::min(remainder, reverse);
    Integer half = length / 2;
    Wide cycle = static_cast<Wide>(g) * half * (length - half) + 1;
    Integer at = 0, step = k % period, prefix = 0;
    for (Integer i = 0; i < work; ++i) {
        at += step;
        if (at >= period)
            at -= period;
        prefix += std::min(at, period - at);
    }
    // This proper period prefix never contains residue zero.
    Wide tail = reverse < remainder ? cycle - 1 - prefix : prefix;
    return static_cast<Wide>(refills / length) * cycle + tail;
}

Integer solve(Integer n, Integer m, Integer k) {
    Integer base = n * m - 1;
    if (k > base)
        return base % MOD;
    Integer length = 2 * m / std::gcd(k, 2 * m), remainder = (base / k) % length;
    Integer work = std::min(remainder, length - remainder - 1);
    Wide extra = n < work ? columns(n, m, k) : residues(n, m, k);
    return static_cast<Integer>((base + 2 * extra) % MOD);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int tests;
    std::cin >> tests;
    while (tests--) {
        Integer n, m, k;
        std::cin >> n >> m >> k;
        std::cout << solve(n, m, k) << '\n';
    }
}
