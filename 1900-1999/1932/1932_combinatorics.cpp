#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int DIGIT_COUNT = 4;
constexpr int HEX_BASE = 16;
constexpr int DIGIT_BITS = 4;
constexpr int DIGIT_MASK = HEX_BASE - 1;
constexpr int PAIR_DOMAIN = HEX_BASE * HEX_BASE;
constexpr int TRIPLE_DOMAIN = PAIR_DOMAIN * HEX_BASE;
constexpr int PAIR_GROUPS = DIGIT_COUNT * (DIGIT_COUNT - 1) / 2;

std::array<std::int64_t, DIGIT_COUNT> distanceHistogram(const std::vector<int> &numbers) {
    std::vector<std::vector<int>> singles(DIGIT_COUNT, std::vector<int>(HEX_BASE));
    std::vector<std::vector<int>> pairs(PAIR_GROUPS, std::vector<int>(PAIR_DOMAIN));
    std::vector<std::vector<int>> triples(DIGIT_COUNT, std::vector<int>(TRIPLE_DOMAIN));
    std::int64_t singlePairs = 0, doublePairs = 0, triplePairs = 0;
    for (int number : numbers) {
        const int first = number >> (DIGIT_BITS * (DIGIT_COUNT - 1));
        const int second = (number >> (2 * DIGIT_BITS)) & DIGIT_MASK;
        const int third = (number >> DIGIT_BITS) & DIGIT_MASK;
        const int fourth = number & DIGIT_MASK;
        const std::array<int, DIGIT_COUNT> singleKeys{first, second, third, fourth};
        for (int index = 0; index < DIGIT_COUNT; ++index) {
            singlePairs += singles[index][singleKeys[index]]++;
        }
        const std::array<int, PAIR_GROUPS> pairKeys{
            number >> (2 * DIGIT_BITS), first * HEX_BASE + third,
            first * HEX_BASE + fourth,  (number >> DIGIT_BITS) & (PAIR_DOMAIN - 1),
            second * HEX_BASE + fourth, number & (PAIR_DOMAIN - 1)};
        for (int index = 0; index < PAIR_GROUPS; ++index) {
            doublePairs += pairs[index][pairKeys[index]]++;
        }
        const std::array<int, DIGIT_COUNT> tripleKeys{
            number >> DIGIT_BITS, (number >> (2 * DIGIT_BITS)) * HEX_BASE + fourth,
            first * PAIR_DOMAIN + (number & (PAIR_DOMAIN - 1)), number & (TRIPLE_DOMAIN - 1)};
        for (int index = 0; index < DIGIT_COUNT; ++index) {
            triplePairs += triples[index][tripleKeys[index]]++;
        }
    }
    const auto count = static_cast<std::int64_t>(numbers.size());
    const auto distanceOne = triplePairs;
    const auto distanceTwo = doublePairs - (DIGIT_COUNT - 1) * distanceOne;
    const auto distanceThree = singlePairs - 2 * distanceTwo - (DIGIT_COUNT - 1) * distanceOne;
    const auto distanceFour = count * (count - 1) / 2 - distanceOne - distanceTwo - distanceThree;
    return {distanceOne, distanceTwo, distanceThree, distanceFour};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count >> std::hex;
    std::vector<int> numbers(count);
    for (int &number : numbers) {
        std::cin >> number;
    }
    const auto answer = distanceHistogram(numbers);
    for (int index = 0; index < DIGIT_COUNT; ++index) {
        if (index > 0) {
            std::cout << ' ';
        }
        std::cout << answer[index];
    }
    std::cout << '\n';
    return 0;
}
