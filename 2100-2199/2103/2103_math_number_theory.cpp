#include <initializer_list>
#include <iostream>
#include <vector>

using Integer = long long;

constexpr Integer kThree = 3;
constexpr Integer kFive = 5;
constexpr Integer kSix = 6;
constexpr Integer kSeven = 7;
constexpr Integer kEight = 8;
constexpr Integer kNine = 9;

struct Result {
    Integer cost;
    std::vector<Integer> route;
};

Result makeResult(Integer cost, std::initializer_list<Integer> points) {
    Result result{cost, {}};
    for (Integer point : points) {
        if (result.route.empty() || result.route.back() != point) {
            result.route.push_back(point);
        }
    }
    return result;
}

Result solve(Integer source, Integer target) {
    if (target <= source) {
        return makeResult(source - target, {source, target});
    }
    if (target % source == 0) {
        return makeResult(0, {source, target});
    }

    // A unit-cost route has one adjacent step between two chains of free jumps.
    for (Integer divisor = 1; divisor * divisor <= target; ++divisor) {
        if (target % divisor != 0) {
            continue;
        }
        for (Integer point : {divisor, target / divisor}) {
            for (Integer adjacent : {point - 1, point + 1}) {
                if (adjacent >= source && adjacent % source == 0) {
                    return makeResult(1, {source, adjacent, point, target});
                }
            }
        }
    }

    if (source <= kFive) {
        Integer lower = target / source * source;
        Integer nearest = target - lower <= lower + source - target ? lower : lower + source;
        return makeResult(2, {source, nearest, target});
    }

    Integer remaining = target;
    for (Integer factor : {2LL, kThree}) {
        while (remaining % factor == 0) {
            remaining /= factor;
        }
    }
    // This divisor is adjacent to a multiple of six.
    if (remaining > 1) {
        Integer adjacent = remaining % kSix == 1 ? remaining - 1 : remaining + 1;
        return makeResult(2, {source, kSix, adjacent, remaining, target});
    }
    if (target % kSix == 0) {
        return makeResult(2, {source, kSix, target});
    }
    if (target % kEight == 0) {
        return makeResult(2, {source, kEight, target});
    }
    if (source == kSeven) {
        return makeResult(2, {source, kNine, target});
    }
    return makeResult(2, {source, kFive, 10, kNine, target});
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Integer source;
    Integer target;
    if (!(std::cin >> source >> target)) {
        return 0;
    }
    Result result = solve(source, target);
    std::cout << result.cost << '\n' << result.route.size() << '\n';
    for (std::size_t index = 0; index < result.route.size(); ++index) {
        if (index != 0) {
            std::cout << ' ';
        }
        std::cout << result.route[index];
    }
    std::cout << '\n';
}
