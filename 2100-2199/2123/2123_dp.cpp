#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>

using State = std::uint64_t;

std::size_t merge(const std::vector<State> &states, std::int64_t weight, std::int64_t remaining,
                  unsigned mass_bits, std::vector<State> *output, std::int64_t &answer) {
    const auto infinity = std::numeric_limits<std::int64_t>::max();
    const State mask = (State{1} << mass_bits) - 1;
    const auto lower = [&](std::int64_t value) {
        return std::lower_bound(states.begin(), states.end(), value,
                                [mask](State state, std::int64_t key) {
                                    return static_cast<std::int64_t>(state & mask) < key;
                                }) -
               states.begin();
    };
    const auto upper = [&](std::int64_t value) {
        return std::upper_bound(states.begin(), states.end(), value,
                                [mask](std::int64_t key, State state) {
                                    return key < static_cast<std::int64_t>(state & mask);
                                }) -
               states.begin();
    };
    std::ptrdiff_t stay = 0;
    const auto stay_end = upper(remaining);
    auto reflected = upper(weight) - 1;
    const auto reflected_end = lower(weight - remaining);
    auto shifted = upper(weight);
    const auto shifted_end = upper(weight + remaining);
    std::size_t size = 0;

    // Each transition produces an ordered stream; reflection reverses its order.
    while (stay < stay_end || reflected >= reflected_end || shifted < shifted_end) {
        const auto stay_mass =
            stay < stay_end ? static_cast<std::int64_t>(states[stay] & mask) : infinity;
        const auto reflected_mass =
            reflected >= reflected_end
                ? weight - static_cast<std::int64_t>(states[reflected] & mask)
                : infinity;
        const auto shifted_mass = shifted < shifted_end
                                      ? static_cast<std::int64_t>(states[shifted] & mask) - weight
                                      : infinity;
        const auto mass = std::min(stay_mass, std::min(reflected_mass, shifted_mass));
        std::int64_t ways = 0;
        if (stay_mass == mass) {
            ways += states[stay++] >> mass_bits;
        }
        if (reflected_mass == mass) {
            ways += states[reflected--] >> mass_bits;
        }
        if (shifted_mass == mass) {
            ways += states[shifted++] >> mass_bits;
        }
        if (mass == 0) {
            if (output != nullptr) {
                answer += ways;
            }
        } else {
            ++size;
            if (output != nullptr) {
                output->push_back((static_cast<State>(ways) << (mass_bits - 1)) |
                                  static_cast<State>(mass));
            }
        }
    }
    return size;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::int64_t target;
    std::cin >> n >> target;
    std::vector<std::int64_t> weights(n);
    std::int64_t remaining = 0;
    for (auto &weight : weights) {
        std::cin >> weight;
        remaining += weight;
    }
    if (target > 2 * remaining) {
        std::cout << 0 << '\n';
        return 0;
    }
    target = target >= remaining ? target - remaining : remaining - target;
    if (target == 0) {
        std::cout << 1 << '\n';
        return 0;
    }

    // Each processed type halves the mass bound and at most doubles a multiplicity.
    unsigned mass_bits = std::numeric_limits<State>::digits - 2;
    std::vector<State> states{(State{1} << mass_bits) | static_cast<State>(target)};
    std::int64_t answer = 0;
    for (auto it = weights.rbegin(); it != weights.rend() && !states.empty(); ++it) {
        const auto weight = *it;
        remaining -= weight;
        // Count distinct masses first to allocate exactly one compact frontier.
        const auto size = merge(states, weight, remaining, mass_bits, nullptr, answer);
        std::vector<State> next;
        next.reserve(size);
        merge(states, weight, remaining, mass_bits, &next, answer);
        states.swap(next);
        --mass_bits;
    }
    std::cout << answer << '\n';
}
