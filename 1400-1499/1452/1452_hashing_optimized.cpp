#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>

constexpr int MAX_COUNT = 2000;
constexpr std::int64_t MAX_VALUE = 1000000000;
constexpr unsigned CAPACITY = 4096;

class Positions {
    struct Entry {
        int value = 0;
        int position = 0;
    };
    std::array<Entry, CAPACITY> entries{};
    static constexpr unsigned FILTER_BITS = 1U << 16, WORD_BITS = 64;
    std::array<std::uint64_t, FILTER_BITS / WORD_BITS> present{};

    static unsigned fingerprint(int value) {
        constexpr unsigned MULTIPLIER = 2654435761U;
        constexpr int MIX_SHIFT = 16;
        unsigned hash = static_cast<unsigned>(value);
        return ((hash ^ (hash >> MIX_SHIFT)) * MULTIPLIER) & (FILTER_BITS - 1);
    }

    unsigned slot(int value) const {
        constexpr unsigned HASH_MULTIPLIER = 2654435761U;
        constexpr int HASH_SHIFT = 20;
        unsigned hash = static_cast<unsigned>(value);
        constexpr int FINAL_SHIFT = 16;
        hash ^= hash >> FINAL_SHIFT;
        unsigned i = (hash * HASH_MULTIPLIER) >> HASH_SHIFT;
        while (entries[i].position && entries[i].value != value)
            i = (i + 1) & (CAPACITY - 1);
        return i;
    }

  public:
    bool insert(int value, int position) {
        auto &entry = entries[slot(value)];
        if (entry.position)
            return false;
        entry = {value, position};
        const unsigned bit = fingerprint(value);
        present[bit / WORD_BITS] |= std::uint64_t{1} << (bit % WORD_BITS);
        return true;
    }

    int find(std::int64_t value) const {
        if (value < 0 || value > MAX_VALUE)
            return 0;
        const unsigned bit = fingerprint(static_cast<int>(value));
        // A missing bit proves absence; a hit still requires the exact key lookup.
        if (!(present[bit / WORD_BITS] & (std::uint64_t{1} << (bit % WORD_BITS))))
            return 0;
        return entries[slot(static_cast<int>(value))].position;
    }
};

int main() {
    int count;
    if (std::scanf("%d", &count) != 1)
        return 0;
    Positions positions;
    std::array<int, MAX_COUNT> values;
    int size = 0;
    for (int i = 1; i <= count; ++i) {
        int value;
        if (std::scanf("%d", &value) != 1)
            return 0;
        if (positions.insert(value, i))
            values[size++] = value;
    }
    std::sort(values.begin(), values.begin() + size);

    int best = 1, first = values[0], step = 0;
    for (int i = 0; i + best < size; ++i) {
        const int start = values[i];
        for (int j = i + 1; j < size; ++j) {
            const int delta = values[j] - start;
            const auto required = start + std::int64_t{best} * delta;
            // To beat the current record, this member must be present.
            if (required > values[size - 1])
                break;
            if ((best > 1 && !positions.find(required)) || positions.find(start - delta))
                continue;
            int length = 2;
            for (std::int64_t next = std::int64_t{values[j]} + delta; positions.find(next);
                 next += delta)
                ++length;
            if (length > best) {
                best = length;
                first = start;
                step = delta;
            }
        }
    }
    std::printf("%d\n", best);
    for (int i = 0; i < best; ++i)
        std::printf("%d%c", positions.find(first + std::int64_t{i} * step),
                    i + 1 == best ? '\n' : ' ');
}
