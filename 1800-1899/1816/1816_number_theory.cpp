#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) return 0;
    std::vector<long long> primes;
    std::vector<int> exps;
    long long rest = n;
    for (long long p = 2; p * p <= rest; p++) {
        if (rest % p) continue;
        primes.push_back(p);
        exps.push_back(0);
        while (rest % p == 0) {
            rest /= p;
            exps.back()++;
        }
    }
    if (rest > 1) {
        primes.push_back(rest);
        exps.push_back(1);
    }
    // a divisor is its exponent vector, numbered in mixed radix: every
    // proper divisor of a divisor gets a smaller number
    int k = primes.size();
    std::vector<int> radix = {1};
    for (int e : exps) radix.push_back(radix.back() * (e + 1));
    int count = radix.back();
    std::vector<double> expected(count, 0.0);
    std::vector<std::pair<int, double>> parts, next;
    for (int index = 0; index < count; index++) {
        int total = 0;
        parts.assign(1, {0, 1.0});
        for (int i = 0; i < k; i++) {
            int top = index / radix[i] % (exps[i] + 1);
            total += top;
            // gcd(m, r) for a uniform r splits over the primes: the exponent
            // of p in it is b < top with chance (1 - 1/p) / p^b, or top with
            // chance 1/p^top
            double q = (double)primes[i];
            next.clear();
            for (auto [offset, chance] : parts) {
                double scale = 1;
                for (int b = 0; b <= top; b++) {
                    double factor = b < top ? (1 - 1 / q) / scale : 1 / scale;
                    next.push_back({offset + b * radix[i], chance * factor});
                    scale *= q;
                }
            }
            parts.swap(next);
        }
        if (total <= 1) continue;  // 1 or a prime: no gcd is taken
        double stay = parts.front().second + parts.back().second;
        double sum = 1;
        for (size_t j = 1; j + 1 < parts.size(); j++) {
            auto [offset, chance] = parts[j];
            sum += chance * (expected[offset] + expected[index - offset]);
        }
        expected[index] = sum / (1 - stay);
    }
    printf("%.10f\n", expected[count - 1]);
    return 0;
}
