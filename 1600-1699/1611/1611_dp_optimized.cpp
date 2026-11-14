#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <limits>

constexpr int step = 10;
constexpr int max_conductors = 10000;
constexpr int max_friends = 50;
constexpr int line_capacity = max_conductors + 1;
static_assert(max_friends < std::numeric_limits<std::uint64_t>::digits);

int main() {
    int n, limit;
    std::array<char, line_capacity> good{};
    if (std::scanf("%d %d", &n, &limit) != 2 || std::scanf("%10000s", good.data()) != 1)
        return 0;

    // Costs for one row, plus one predecessor bit per state for reconstruction.
    std::array<std::uint16_t, max_friends + 1> cost{};
    std::array<std::uint64_t, line_capacity> from_friend;
    for (int j = 0; j <= limit; ++j)
        cost[j] = j / step;
    for (int i = 1; i <= n; ++i) {
        const bool good_conductor = good[i - 1] == '1';
        cost[0] += i % step == 0 && good_conductor;
        std::uint64_t row = 0;
        for (int j = 1; j <= limit; ++j) {
            const bool fined = (i + j) % step == 0;
            const int by_conductor = cost[j] + (fined && good_conductor);
            const int by_friend = cost[j - 1] + fined;
            if (by_friend < by_conductor) {
                cost[j] = by_friend;
                row |= std::uint64_t{1} << j;
            } else {
                cost[j] = by_conductor;
            }
        }
        from_friend[i] = row;
    }

    const auto minimum = std::min_element(cost.begin(), cost.begin() + limit + 1);
    int j = static_cast<int>(minimum - cost.begin());
    const int friends = j;
    std::array<int, max_friends> places;
    for (int i = n; i > 0 || j > 0;) {
        if (i == 0 || (from_friend[i] & (std::uint64_t{1} << j))) {
            places[j - 1] = i + j;
            --j;
        } else {
            --i;
        }
    }
    std::printf("%d\n%d", *minimum, friends);
    for (int i = 0; i < friends; ++i)
        std::printf(" %d", places[i]);
    std::puts("");
}
