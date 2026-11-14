#include <algorithm>
#include <array>
#include <cstdio>
#include <vector>

constexpr int MASK_COUNT = 8;
constexpr int INGREDIENTS = 3;
constexpr int INGREDIENT_C = 1 << (INGREDIENTS - 1);
constexpr int MAX_POURINGS = 3 * (MASK_COUNT - 1);

int main() {
    int count;
    if (std::scanf("%d", &count) != 1)
        return 0;

    std::vector<int> next(count + 1);
    std::array<int, MASK_COUNT> first{}, last{};
    for (int i = 1; i <= count; ++i) {
        char order[INGREDIENTS + 1];
        if (std::scanf("%3s", order) != 1)
            return 0;
        int mask = 0;
        for (const char *letter = order; *letter; ++letter)
            mask |= *letter == 'A' ? 1 : (*letter == 'B' ? 2 : INGREDIENT_C);
        if (last[mask])
            next[last[mask]] = i;
        else
            first[mask] = i;
        last[mask] = i;
    }

    std::array<int, MASK_COUNT - 1> order{}, best_order{};
    int types = 0;
    for (int mask = 1; mask < MASK_COUNT; ++mask) {
        if (first[mask])
            order[types++] = mask;
    }
    int best = MAX_POURINGS + 1;
    do {
        int previous = 0, cost = 0;
        for (int i = 0; i < types; ++i) {
            cost += __builtin_popcount(order[i] & ~previous);
            previous = order[i];
        }
        if (cost < best) {
            best = cost;
            best_order = order;
        }
    } while (std::next_permutation(order.begin(), order.begin() + types));

    std::printf("%d\n", best);
    int remaining = count;
    for (int i = 0; i < types; ++i) {
        for (int glass = first[best_order[i]]; glass; glass = next[glass])
            std::printf("%d%c", glass, --remaining ? ' ' : '\n');
    }
}
