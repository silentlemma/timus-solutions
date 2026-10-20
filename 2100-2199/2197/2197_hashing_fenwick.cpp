#include <algorithm>
#include <cstdint>
#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

constexpr int64_t MOD = 1000000007;
constexpr int64_t OTHER_MOD = 1000000009;
constexpr int64_t MIN_BASE = 257;
constexpr int WORD_BITS = 64;
constexpr size_t CACHE_LIMIT = 1024;

struct Hash {
    int64_t a = 0, b = 0;
    Hash operator+(Hash h) const { return {(a + h.a) % MOD, (b + h.b) % OTHER_MOD}; }
    Hash operator-(Hash h) const {
        return {(a - h.a + MOD) % MOD, (b - h.b + OTHER_MOD) % OTHER_MOD};
    }
    Hash operator*(Hash h) const { return {a * h.a % MOD, b * h.b % OTHER_MOD}; }
    bool operator==(Hash h) const { return a == h.a && b == h.b; }
};

struct Positions {
    vector<uint64_t> low, middle;
    uint64_t top = 0;
    explicit Positions(int n) : low(n / WORD_BITS + 1), middle(low.size() / WORD_BITS + 1) {
        insert(0);
    }
    static int highest(uint64_t x) { return WORD_BITS - 1 - __builtin_clzll(x); }
    static uint64_t below(int bit) { return bit ? (uint64_t(-1) >> (WORD_BITS - bit)) : 0; }
    void insert(int position) {
        int block = position / WORD_BITS, group = block / WORD_BITS;
        low[block] |= uint64_t(1) << (position % WORD_BITS);
        middle[group] |= uint64_t(1) << (block % WORD_BITS);
        top |= uint64_t(1) << group;
    }
    void erase(int position) {
        int block = position / WORD_BITS, group = block / WORD_BITS;
        low[block] &= ~(uint64_t(1) << (position % WORD_BITS));
        if (!low[block]) {
            middle[group] &= ~(uint64_t(1) << (block % WORD_BITS));
            if (!middle[group])
                top &= ~(uint64_t(1) << group);
        }
    }
    int predecessor(int position) const {
        int block = position / WORD_BITS;
        uint64_t bits = low[block] & (uint64_t(-1) >> (WORD_BITS - 1 - position % WORD_BITS));
        if (!bits) {
            int group = block / WORD_BITS;
            uint64_t groups = middle[group] & below(block % WORD_BITS);
            if (!groups) {
                group = highest(top & below(group));
                groups = middle[group];
            }
            block = group * WORD_BITS + highest(groups);
            bits = low[block];
        }
        return block * WORD_BITS + highest(bits);
    }
};

struct Solver {
    int n;
    vector<Hash> hashes, power, values, fenwick;
    vector<int> following, sources, primes;
    Positions positions;
    Hash whole;
    unordered_map<int, Hash> multipliers;
    unordered_map<int64_t, int64_t> cache;

    Solver(int length, const string &text)
        : n(length), hashes(text.size() + 1), power(n + 1), values(n + 1), fenwick(n + 1),
          following(n + 1, n), sources(n + 1), positions(n) {
        mt19937_64 random(random_device{}());
        uniform_int_distribution<int64_t> first_base(MIN_BASE, MOD - 2);
        uniform_int_distribution<int64_t> second_base(MIN_BASE, OTHER_MOD - 2);
        Hash base;
        do {
            base = {first_base(random), second_base(random)};
            power[0] = {1, 1};
            for (int i = 0; i < n; ++i)
                power[i + 1] = power[i] * base;
        } while (power[n].a == 1 || power[n].b == 1);
        for (size_t i = 0; i < text.size(); ++i)
            hashes[i + 1] = hashes[i] * base + Hash{text[i], text[i]};
        whole = values[0] = hashes[n];
        for (int i = 1; i <= n; i *= 2)
            fenwick[i] = whole;
        int remaining = n;
        for (int divisor = 2; divisor * divisor <= remaining; ++divisor) {
            if (remaining % divisor == 0) {
                primes.push_back(divisor);
                while (remaining % divisor == 0)
                    remaining /= divisor;
            }
        }
        if (remaining > 1)
            primes.push_back(remaining);
    }

    // Static slices are weighted by their positions in the current string.
    Hash fingerprint(int source, int left, int right) const {
        int length = right - left;
        return (hashes[source + length] - hashes[source] * power[length]) * power[n - right];
    }

    void set_value(int position, Hash value) {
        Hash old = values[position];
        for (int i = position + 1; i <= n; i += i & -i) {
            // Raw sums avoid modular arithmetic in every Fenwick step.
            fenwick[i].a += value.a - old.a;
            fenwick[i].b += value.b - old.b;
        }
        values[position] = value;
    }

    void replace(int begin, int end, int source) {
        int start = positions.predecessor(begin);
        Hash removed;
        for (int position = start; position < end; position = following[position]) {
            int left = max(position, begin), right = min(following[position], end);
            removed =
                removed + (left == position && right == following[position]
                               ? values[position]
                               : fingerprint(sources[position] + left - position, left, right));
        }
        Hash replacement = fingerprint(source, begin, end);
        Hash delta = replacement - removed;
        if (delta == Hash{} && end <= following[start])
            return;
        whole = whole + delta;
        for (int position = start; position < end;) {
            int stop = following[position], old_source = sources[position];
            if (position < begin) {
                set_value(position, fingerprint(old_source, position, begin));
                following[position] = begin;
            } else if (position != begin) {
                set_value(position, {});
                positions.erase(position);
            }
            if (end < stop) {
                sources[end] = old_source + end - position;
                following[end] = stop;
                set_value(end, fingerprint(sources[end], end, stop));
                positions.insert(end);
            }
            position = stop;
        }
        sources[begin] = source;
        following[begin] = end;
        set_value(begin, replacement);
        positions.insert(begin);
    }

    Hash prefix(int length) const {
        int position = positions.predecessor(length - 1);
        Hash value;
        for (int i = position; i; i -= i & -i) {
            value.a += fenwick[i].a;
            value.b += fenwick[i].b;
        }
        value.a %= MOD;
        value.b %= OTHER_MOD;
        return value + (following[position] == length
                            ? values[position]
                            : fingerprint(sources[position], position, length));
    }

    int64_t answer() {
        int64_t key = whole.a * OTHER_MOD + whole.b;
        auto known = cache.find(key);
        if (known != cache.end())
            return known->second;
        int period = n;
        Hash repeated = power[n] - Hash{1, 1};
        // Remove prime factors while the shorter prefix still generates the string.
        for (int prime : primes) {
            while (period % prime == 0) {
                int candidate = period / prime;
                if (!multipliers.count(candidate))
                    multipliers[candidate] = (power[candidate] - Hash{1, 1}) * power[n - candidate];
                if (!(whole * multipliers[candidate] == prefix(candidate) * repeated))
                    break;
                period = candidate;
            }
        }
        int64_t result = int64_t(n) * period;
        if (cache.size() == CACHE_LIMIT)
            cache.clear();
        cache[key] = result;
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    string text, part;
    cin >> text;
    vector<int> starts(m + 1), lengths(m + 1);
    lengths[0] = n;
    for (int i = 1; i <= m; ++i) {
        cin >> part;
        starts[i] = int(text.size());
        lengths[i] = int(part.size());
        text += part;
    }
    Solver solver(n, text);
    cout << solver.answer() << '\n';
    for (int i = 0; i < q; ++i) {
        int begin, index;
        cin >> begin >> index;
        --begin;
        solver.replace(begin, begin + lengths[index], starts[index]);
        cout << solver.answer() << '\n';
    }
}
