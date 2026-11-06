#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <functional>
#include <vector>

constexpr int WORD_BITS = 64;

class Reach {
    int words;
    std::vector<std::uint64_t> bits;

  public:
    Reach(int count, int limit) : words(limit / WORD_BITS + 1), bits((count + 1) * words) {
        bits[count * words] = 1;
    }

    void add_item(int index, int length) {
        auto *current = bits.data() + index * words;
        const auto *suffix = current + words;
        const int offset = length / WORD_BITS;
        const int shift = length % WORD_BITS;
        for (int i = 0; i < words; ++i) {
            current[i] = suffix[i];
            if (i >= offset) {
                current[i] |= suffix[i - offset] << shift;
                if (shift != 0 && i > offset)
                    current[i] |= suffix[i - offset - 1] >> (WORD_BITS - shift);
            }
        }
    }

    bool has(int index, int sum) const {
        return (bits[index * words + sum / WORD_BITS] >> (sum % WORD_BITS)) & 1;
    }
};

const int SEARCH_LIMIT = 256, ATTEMPTS = 128, RNG_MOD = 65536;
constexpr int RNG_MULTIPLIER = 97;
constexpr int MAX_SHIP_LENGTH = 100;

int n, m, calls;
bool limited;
std::vector<int> ships, rows, order, owner;

bool fill(int pos);

bool pick(int pos, const std::vector<int> &free, const Reach &reach, int k, int need) {
    if (limited && ++calls > SEARCH_LIMIT)
        return false;
    if (need == 0)
        return fill(pos + 1);
    if (!reach.has(k, need))
        return false;
    int last = -1;
    for (int j = k; j < (int)free.size(); j++) {
        int length = ships[free[j]];
        // equal ships are interchangeable: try each length once per place
        if (length == last || length > need || !reach.has(j + 1, need - length))
            continue;
        last = length;
        owner[free[j]] = order[pos];
        if (pick(pos, free, reach, j + 1, need - length))
            return true;
        owner[free[j]] = -1;
        if (limited && calls > SEARCH_LIMIT)
            return false;
    }
    return false;
}

bool fill(int pos) {
    std::vector<int> free;
    for (int i = 0; i < n; i++)
        if (owner[i] < 0)
            free.push_back(i);
    if (pos == m - 1) {
        // the last row takes every ship that is left
        int sum = 0;
        for (int i : free)
            sum += ships[i];
        if (sum != rows[order[pos]])
            return false;
        for (int i : free)
            owner[i] = order[pos];
        return true;
    }
    int total = 0;
    for (int q = pos; q < m; ++q)
        total += rows[order[q]];
    int limit = rows[order[pos]];
    for (int q = pos + 1; q < m; ++q) {
        const int target = rows[order[q]];
        limit = std::max(limit, std::min(target, total - target));
    }
    // To check a later row we can test the lighter of its target and its complement.
    Reach reach(static_cast<int>(free.size()), limit);
    for (int k = static_cast<int>(free.size()) - 1; k >= 0; --k)
        reach.add_item(k, ships[free[k]]);
    for (int q = pos; q < m; ++q) {
        const int target = rows[order[q]];
        if (!reach.has(0, std::min(target, total - target)))
            return false;
    }
    return pick(pos, free, reach, 0, rows[order[pos]]);
}

int main() {
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    ships.resize(n);
    rows.resize(m);
    for (auto &s : ships)
        scanf("%d", &s);
    for (auto &r : rows)
        scanf("%d", &r);
    std::sort(ships.begin(), ships.end(), std::greater<int>());
    // try the shortest rows first as a heuristic
    for (int r = 0; r < m; r++)
        order.push_back(r);
    std::sort(order.begin(), order.end(),
              [](int a, int b) { return rows[a] != rows[b] ? rows[a] < rows[b] : a < b; });
    owner.assign(n, -1);
    int state = 1;
    // restart costly searches in a reproducible order; the final search is complete
    for (int attempt = 0; attempt <= ATTEMPTS; attempt++) {
        calls = 0;
        limited = attempt < ATTEMPTS;
        if (fill(0))
            break;
        for (int i = m - 1; i > 0; i--) {
            state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
            std::swap(order[i], order[state % (i + 1)]);
        }
        std::vector<int> rank(MAX_SHIP_LENGTH + 1);
        for (int i = 0; i <= MAX_SHIP_LENGTH; i++)
            rank[i] = i;
        for (int i = MAX_SHIP_LENGTH; i > 1; i--) {
            state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
            std::swap(rank[i], rank[1 + state % i]);
        }
        std::sort(ships.begin(), ships.end(), [&](int a, int b) { return rank[a] < rank[b]; });
    }
    for (int r = 0; r < m; r++) {
        std::vector<int> row;
        for (int i = 0; i < n; i++)
            if (owner[i] == r)
                row.push_back(ships[i]);
        printf("%d\n", (int)row.size());
        for (size_t i = 0; i < row.size(); i++)
            printf(i + 1 < row.size() ? "%d " : "%d\n", row[i]);
    }
}
