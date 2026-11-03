#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <utility>
#include <vector>

const std::uint64_t PRIMES[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
const int MOST = 64, MAX_TESTS = 100;
using Entry = std::pair<std::uint64_t, std::uint32_t>;
std::vector<Entry> records;
std::uint64_t limit;

void grow(int index, int cap, std::uint64_t value, std::uint32_t divisors) {
    auto position = std::lower_bound(records.begin(), records.end(), Entry(value, 0));
    if (position == records.begin() || (position - 1)->second < divisors) {
        auto end = position;
        // Remove exactly the records dominated by this value and divisor count.
        while (end != records.end() && end->second <= divisors)
            ++end;
        position = records.erase(position, end);
        records.insert(position, Entry(value, divisors));
    }
    if (index == static_cast<int>(sizeof(PRIMES) / sizeof(PRIMES[0])))
        return;
    for (int exponent = 1; exponent <= cap; exponent++) {
        if (value > limit / PRIMES[index])
            break;
        value *= PRIMES[index];
        grow(index + 1, exponent, value, divisors * (exponent + 1));
    }
}

int main() {
    int tests;
    if (scanf("%d", &tests) != 1)
        return 0;
    unsigned long long queries[MAX_TESTS];
    limit = 0;
    for (int i = 0; i < tests; i++) {
        scanf("%llu", &queries[i]);
        limit = std::max(limit, static_cast<std::uint64_t>(queries[i]));
    }
    grow(0, MOST, 1, 1);
    for (int i = 0; i < tests; i++) {
        auto entry =
            std::upper_bound(records.begin(), records.end(), Entry(queries[i], UINT32_MAX)) - 1;
        printf("%llu %u\n", static_cast<unsigned long long>(entry->first), entry->second);
    }
}
