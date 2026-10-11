#include <cstdio>
#include <string>

int main() {
    long long k, m;
    scanf("%lld %lld", &k, &m);
    std::string digits = std::to_string(k);
    // numbers not longer than k that come no later than k: for each length,
    // those from 10^(l-1) up to the first l digits of k; any N >= k has them
    long long before = 0, low = 1;
    for (size_t l = 1; l <= digits.size(); l++) {
        before += std::stoll(digits.substr(0, l)) - low + 1;
        low *= 10;
    }
    if (m < before) {
        printf("0\n");
        return 0;
    }
    // each further number before k is longer than k: of length l it lies in
    // [10^(l-1), k * 10^(l-len(k))), and N is the (m - before)-th of them
    long long need = m - before, top = k * 10;
    if (need == 0) {
        printf("%lld\n", k);
        return 0;
    }
    for (; top > low; low *= 10, top *= 10) {
        if (top - low >= need) {
            printf("%lld\n", low + need - 1);
            return 0;
        }
        need -= top - low;
    }
    // k is a power of ten, and no longer number comes before it
    printf("0\n");
}
