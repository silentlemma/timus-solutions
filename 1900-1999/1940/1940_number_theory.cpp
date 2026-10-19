#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

constexpr int MAX_MINUTES = 300;
constexpr int MAX_DIVISOR = MAX_MINUTES + 1;
constexpr int WHEEL_PRIMES = 6;
constexpr int USED_BITS = 6;

struct Wheel {
    int period;
    std::vector<int> prefix;
};

class Counter {
    std::vector<int> primes;
    std::vector<int> primeCounts;
    std::vector<Wheel> wheels;
    std::unordered_map<std::int64_t, int> memo;
    int base = 0;

    int phi(int value, int remaining) {
        if (remaining == base) {
            const auto &wheel = wheels[base];
            return value / wheel.period * wheel.prefix.back() + wheel.prefix[value % wheel.period];
        }
        if (value == 0)
            return 0;
        const int last = primes[remaining - 1];
        if (value < last)
            return 1;
        if (value < last * last)
            return 1 + primeCounts[value] - remaining;
        const auto key = (static_cast<std::int64_t>(value) << USED_BITS) | remaining;
        const auto found = memo.find(key);
        if (found != memo.end())
            return found->second;
        const int result = phi(value, remaining - 1) - phi(value / last, remaining - 1);
        memo.emplace(key, result);
        return result;
    }

  public:
    Counter() {
        const int limit = MAX_DIVISOR * MAX_DIVISOR;
        std::vector<bool> prime(limit + 1, true);
        prime[0] = prime[1] = false;
        for (int divisor = 2; divisor * divisor <= limit; ++divisor) {
            if (prime[divisor]) {
                for (int number = divisor * divisor; number <= limit; number += divisor) {
                    prime[number] = false;
                }
            }
        }
        primeCounts.resize(limit + 1);
        for (int number = 1; number <= limit; ++number) {
            primeCounts[number] = primeCounts[number - 1] + prime[number];
            if (number <= MAX_DIVISOR && prime[number])
                primes.push_back(number);
        }
        wheels.push_back({1, {0, 1}});
        int period = 1;
        for (int used = 1; used <= WHEEL_PRIMES; ++used) {
            period *= primes[used - 1];
            std::vector<bool> survives(period + 1, true);
            survives[0] = false;
            for (int index = 0; index < used; ++index) {
                for (int number = primes[index]; number <= period; number += primes[index]) {
                    survives[number] = false;
                }
            }
            std::vector<int> prefix(period + 1);
            for (int number = 1; number <= period; ++number) {
                prefix[number] = prefix[number - 1] + survives[number];
            }
            wheels.push_back({period, std::move(prefix)});
        }
    }

    int countYears(int start, int duration, int minutes) {
        const int limit = minutes + 1;
        const int used = primeCounts[limit];
        base = std::min(used, WHEEL_PRIMES);
        memo.clear();
        const int finish = start + duration;
        int result = phi(finish, used) - phi(start, used);
        result += primeCounts[std::min(finish, limit)] - primeCounts[std::min(start, limit)];
        return result;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int start, duration, minutes;
    std::cin >> start >> duration >> minutes;
    Counter counter;
    std::cout << counter.countYears(start, duration, minutes) << '\n';
    return 0;
}
