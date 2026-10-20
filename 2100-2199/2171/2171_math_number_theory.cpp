#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

using Integer = std::int64_t;

struct Progression {
    Integer first;
    Integer step;
};

std::pair<Integer, Integer> extended_gcd(Integer a, Integer b) {
    Integer x = 1;
    Integer next_x = 0;
    while (b != 0) {
        Integer quotient = a / b;
        Integer remainder = a % b;
        a = b;
        b = remainder;
        Integer coefficient = x - quotient * next_x;
        x = next_x;
        next_x = coefficient;
    }
    return {a, x};
}

Integer count_union(const std::vector<Progression> &progressions, Integer limit, std::size_t begin,
                    Integer first, Integer step, Integer sign) {
    Integer answer = 0;
    for (std::size_t i = begin; i < progressions.size(); ++i) {
        Integer other_first = progressions[i].first;
        Integer other_step = progressions[i].step;
        Integer merged_first = first;
        Integer merged_step = step;
        if (step == 0) {
            if (first < other_first || (first - other_first) % other_step != 0) {
                continue;
            }
        } else {
            auto [divisor, inverse] = extended_gcd(step, other_step);
            Integer difference = other_first - first;
            if (difference % divisor != 0) {
                continue;
            }
            Integer modulus = other_step / divisor;
            Integer offset = (difference / divisor * inverse) % modulus;
            if (offset < 0) {
                offset += modulus;
            }
            merged_step = step * modulus;
            merged_first = first + step * offset;
            if (merged_first < other_first) {
                Integer gap = other_first - merged_first;
                merged_first += ((gap - 1) / merged_step + 1) * merged_step;
            }
            if (merged_first > limit) {
                continue;
            }
            // A zero step stores an intersection with just one in-range value.
            if (merged_step > limit - merged_first) {
                merged_step = 0;
            }
        }
        Integer count = merged_step == 0 ? 1 : (limit - merged_first) / merged_step + 1;
        answer += sign * count;
        answer += count_union(progressions, limit, i + 1, merged_first, merged_step, -sign);
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    Integer limit;
    std::size_t count;
    if (!(std::cin >> limit >> count)) {
        return 0;
    }
    std::vector<Progression> progressions(count);
    for (auto &progression : progressions) {
        std::cin >> progression.first >> progression.step;
    }
    std::cout << count_union(progressions, limit, 0, 1, 1, 1) << '\n';
}
