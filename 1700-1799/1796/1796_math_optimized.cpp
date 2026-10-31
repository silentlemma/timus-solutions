#include <cstdio>

constexpr int NOTES[] = {10, 50, 100, 500, 1000, 5000};

// stdio avoids the iostream startup overhead and streams the output.
int main() {
    long long total = 0, smallest = 0;
    for (int note : NOTES) {
        long long count;
        if (std::scanf("%lld", &count) != 1)
            return 0;
        total += count * note;
        if (count > 0 && smallest == 0)
            smallest = note;
    }
    long long price;
    std::scanf("%lld", &price);
    // k tickets fit when k * price <= total, and taking away the smallest
    // note must leave too little: total - smallest < k * price
    long long low = (total - smallest) / price + 1, high = total / price;
    std::printf("%lld\n", high - low + 1);
    for (long long k = low; k <= high; k++) {
        std::printf("%lld%c", k, k < high ? ' ' : '\n');
    }
    return 0;
}
