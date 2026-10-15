#include <algorithm>
#include <cstdio>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

typedef unsigned long long u64;
typedef unsigned __int128 u128;

const int LONGEST = 15;  // no minimal forbidden multiset is longer for bases up to 36
const int SHIFT = 6;  // bits per digit in a word code
const u64 DIGIT_MASK = (1 << SHIFT) - 1;
const int LOW_BITS = 64;  // a least word keeps its low 64 bits apart
const int LENGTH_AT = 28;  // the length sits above the 26 high bits of the word

const int STAR = 15;  // a pattern count meaning "any number of this digit"
const int FIELD = 4;  // bits per count in a packed vector
const int FIELDS = 16;  // counts per 64-bit word
const int WORDS = 3;
const u64 COUNT_MASK = (1 << FIELD) - 1;
const u64 MIX_1 = 0x9e3779b97f4a7c15ULL;
const u64 MIX_2 = 0xbf58476d1ce4e5b9ULL;
const u64 MIX_3 = 0x94d049bb133111ebULL;
const int MIX_SHIFT_1 = 30;
const int MIX_SHIFT_2 = 27;
const int MIX_SHIFT_3 = 31;
const int LOAD_DEN = 2;  // the hash table is kept at most half full
const int KEY_AT = 32;  // a table slot keeps the key above the index
const int ESTIMATE_DIV = 2;  // about base^4 / 2 least words exist

u64 mix(u64 x) {
    x += MIX_1;
    x = (x ^ (x >> MIX_SHIFT_1)) * MIX_2;
    x = (x ^ (x >> MIX_SHIFT_2)) * MIX_3;
    return x ^ (x >> MIX_SHIFT_3);
}

// the least word of a pair (sum of digits, sum of squares): its length and
// sorted digits, SHIFT bits each, as one number split in two, so that
// comparing the numbers compares length first and then the words
struct Least {
    u64 low;
    unsigned high;
    unsigned key;

    u128 value() const {
        return (u128)high << LOW_BITS | low;
    }
    void set(u128 v) {
        high = v >> LOW_BITS;
        low = (u64)v;
    }
};

u128 encode(int length, u128 word) {
    return (u128)length << (LOW_BITS + LENGTH_AT) | word;
}

// open addressing from a pair key to the index of its least word: a slot
// holds (key + 1) << 32 | index, and 0 marks an empty one
struct Table {
    std::vector<u64> slots;
    int bits = 1;
    size_t used = 0;

    explicit Table(size_t expected) {
        while (((size_t)1 << bits) < expected * LOAD_DEN) {
            bits++;
        }
        slots.assign((size_t)1 << bits, 0);
    }
    size_t slot(unsigned key) const {
        size_t mask = slots.size() - 1;
        size_t pos = (key * MIX_1) >> (LOW_BITS - bits);
        while (slots[pos] && (slots[pos] >> KEY_AT) != key + 1ULL) {
            pos = (pos + 1) & mask;
        }
        return pos;
    }
    int get(unsigned key) const {
        u64 s = slots[slot(key)];
        return s ? (int)(unsigned)s : -1;
    }
    void put(unsigned key, int value) {
        if ((used + 1) * LOAD_DEN > slots.size()) {
            std::vector<u64> old;
            old.swap(slots);
            bits++;
            slots.assign(old.size() * 2, 0);
            for (u64 s : old) {
                if (s) {
                    slots[slot((s >> KEY_AT) - 1)] = s;
                }
            }
        }
        slots[slot(key)] = (key + 1ULL) << KEY_AT | (unsigned)value;
        used++;
    }
};

// counts of the digits 1 .. m, FIELD bits each, with the set of nonzero
// counts and their total
struct Vec {
    u64 w[WORDS] = {0, 0, 0};
    u64 mask = 0;
    int sum = 0;

    int get(int i) const {
        return (w[i / FIELDS] >> (i % FIELDS * FIELD)) & COUNT_MASK;
    }
    void put(int i, int c) {
        int shift = i % FIELDS * FIELD;
        sum += c - get(i);
        w[i / FIELDS] = (w[i / FIELDS] & ~(COUNT_MASK << shift)) | (u64)c << shift;
        mask = c ? mask | 1ULL << i : mask & ~(1ULL << i);
    }
};

// whether every count of g is at most that of f
bool below(const Vec& g, const Vec& f) {
    for (u64 rest = g.mask; rest; rest &= rest - 1) {
        int i = __builtin_ctzll(rest);
        if (g.get(i) > f.get(i)) {
            return false;
        }
    }
    return true;
}

// vectors sorted by their sets of nonzero counts, to find quickly whether one
// of them lies below a given vector
struct Index {
    std::vector<Vec> items;
    std::vector<u64> supports;  // the distinct sets, increasing
    std::vector<unsigned> begin;  // items of supports[s] are begin[s] .. begin[s + 1] - 1

    explicit Index(std::vector<Vec> vectors) : items(std::move(vectors)) {
        std::sort(items.begin(), items.end(),
                  [](const Vec& a, const Vec& b) { return a.mask < b.mask; });
        for (size_t i = 0; i < items.size(); i++) {
            if (i == 0 || items[i].mask != items[i - 1].mask) {
                supports.push_back(items[i].mask);
                begin.push_back(i);
            }
        }
        begin.push_back(items.size());
    }
    bool in_group(size_t s, const Vec& f) const {
        for (unsigned j = begin[s]; j < begin[s + 1]; j++) {
            if (below(items[j], f)) {
                return true;
            }
        }
        return false;
    }
    // whether some item lies below f: by the subsets of its support or by a
    // scan of the supports, whichever is shorter
    bool covers(const Vec& f) const {
        if ((1ULL << __builtin_popcountll(f.mask)) < supports.size()) {
            for (u64 sub = f.mask;; sub = (sub - 1) & f.mask) {
                auto it = std::lower_bound(supports.begin(), supports.end(), sub);
                if (it != supports.end() && *it == sub && in_group(it - supports.begin(), f)) {
                    return true;
                }
                if (sub == 0) {
                    return false;
                }
            }
        }
        for (size_t s = 0; s < supports.size(); s++) {
            if (!(supports[s] & ~f.mask) && in_group(s, f)) {
                return true;
            }
        }
        return false;
    }
};

Vec without_last(Vec v, int last) {
    v.put(last, 0);
    return v;
}

bool same(const Vec& a, const Vec& b) {
    return a.w[0] == b.w[0] && a.w[1] == b.w[1] && a.w[2] == b.w[2];
}

// the minimal vectors: one that lies below another has a smaller total, so
// the vectors are taken by total, and those of one total are checked only
// against the smaller ones
std::vector<Vec> minimal(std::vector<Vec> vectors) {
    std::sort(vectors.begin(), vectors.end(), [](const Vec& a, const Vec& b) {
        if (a.sum != b.sum) {
            return a.sum < b.sum;
        }
        return a.w[0] != b.w[0] ? a.w[0] < b.w[0]
               : a.w[1] != b.w[1] ? a.w[1] < b.w[1] : a.w[2] < b.w[2];
    });
    std::vector<Vec> kept;
    Index smaller({});
    for (size_t i = 0; i < vectors.size();) {
        size_t j = i;
        bool grown = false;
        for (; j < vectors.size() && vectors[j].sum == vectors[i].sum; j++) {
            if ((j == i || !same(vectors[j], vectors[j - 1])) && !smaller.covers(vectors[j])) {
                kept.push_back(vectors[j]);
                grown = true;
            }
        }
        if (grown && j < vectors.size()) {
            smaller = Index(kept);
        }
        i = j;
    }
    return kept;
}

// consecutive nodes start, start + 1, ..., start + count - 1
struct Run {
    unsigned start;
    unsigned count;
};

// patterns over the first n digits, a trie of (parent, count) nodes, where
// the patterns of one solved set are a few runs of consecutive nodes
struct Patterns {
    std::vector<unsigned> nodes;  // (parent << FIELD) | count; node 0 is empty
    std::vector<unsigned> stars;
    std::unordered_map<u64, int> memo;
    std::vector<Run> runs;
    std::vector<unsigned> first_run;  // the runs of result i are first_run[i] ..

    explicit Patterns(int digits) : nodes(1, 0), stars(1, 0) {
        for (int i = 0; i < digits; i++) {
            stars.push_back(extend(stars.back(), STAR));
        }
        first_run.push_back(0);
    }
    template <class F>
    void each(int result, F visit) const {
        for (unsigned r = first_run[result]; r < first_run[result + 1]; r++) {
            for (unsigned i = 0; i < runs[r].count; i++) {
                visit(runs[r].start + i);
            }
        }
    }
    unsigned extend(unsigned parent, int count) {
        nodes.push_back(parent << FIELD | count);
        return nodes.size() - 1;
    }
    Vec decode(unsigned node, int n) const {
        Vec p;
        for (int i = n - 1; i >= 0; i--) {
            u64 c = nodes[node] & COUNT_MASK;
            p.w[i / FIELDS] |= c << (i % FIELDS * FIELD);
            if (c) {
                p.mask |= 1ULL << i;
            }
            node = nodes[node] >> FIELD;
        }
        return p;
    }

    // the index of the result: patterns covering exactly the count vectors over
    // the first n digits above none of gens (minimal vectors); the last digit
    // takes each fixed count below the largest one in gens, then any count
    int solve(const std::vector<Vec>& gens, int n) {
        u64 key = mix(n) + gens.size();
        for (const Vec& g : gens) {
            key += mix(g.w[0]) ^ mix(g.w[1] + MIX_1) * MIX_3 ^ mix(g.w[2] + MIX_2);
        }
        auto found = memo.find(key);
        if (found != memo.end()) {
            return found->second;
        }
        std::vector<Run> result;
        if (gens.empty()) {
            result.push_back(Run{stars[n], 1});
        } else if (gens[0].mask != 0) {
            int last = n - 1;
            int top = 0;
            for (const Vec& g : gens) {
                top = std::max(top, g.get(last));
            }
            // levels[k]: the minimal gens that apply with k copies of the last
            // digit; as gens are minimal, a newcomer with k copies never lies
            // above an earlier one, and the last level serves any count
            std::vector<std::vector<Vec>> levels(top + 1);
            for (int k = 0; k <= top; k++) {
                std::vector<Vec> fresh;
                for (const Vec& g : gens) {
                    if (g.get(last) == k) {
                        fresh.push_back(without_last(g, last));
                    }
                }
                if (k > 0) {
                    Index newcomers(fresh);
                    for (const Vec& f : levels[k - 1]) {
                        if (!newcomers.covers(f)) {
                            levels[k].push_back(f);
                        }
                    }
                }
                levels[k].insert(levels[k].end(), fresh.begin(), fresh.end());
            }
            Index open(levels[top]);
            for (int k = 0; k < top; k++) {
                int sub = solve(levels[k], last);
                Run run{(unsigned)nodes.size(), 0};
                each(sub, [&](unsigned node) {
                    // a prefix allowed with any count is already covered below
                    if (open.covers(decode(node, last))) {
                        extend(node, k);
                        run.count++;
                    }
                });
                result.push_back(run);
            }
            int sub = solve(open.items, last);
            Run run{(unsigned)nodes.size(), 0};
            each(sub, [&](unsigned node) {
                extend(node, STAR);
                run.count++;
            });
            result.push_back(run);
        }
        runs.insert(runs.end(), result.begin(), result.end());
        first_run.push_back(runs.size());
        memo[key] = first_run.size() - 2;
        return first_run.size() - 2;
    }
};

char digit_char(int d) {
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[d];
}

int main() {
    int base;
    scanf("%d", &base);
    int m = base - 1;
    // the least number of every pair (sum of digits, sum of squares) with at most
    // LONGEST digits: digits are appended in increasing order, and adding the
    // same digits to two words keeps their order, so the best per pair suffices
    unsigned width = LONGEST * m * m + 1;
    size_t estimate = (size_t)base * base * base * base / ESTIMATE_DIV + 1;
    std::vector<Least> least;
    least.reserve(estimate);
    least.push_back(Least{0, 0, 0});
    Table table(estimate);
    table.put(0, 0);
    for (int d = 1; d < base; d++) {
        unsigned step = d * width + d * d;
        size_t count = least.size();
        for (size_t i = 0; i < count; i++) {
            unsigned key = least[i].key;
            u128 value = least[i].value();
            int length = value >> (LOW_BITS + LENGTH_AT);
            u128 word = value ^ encode(length, 0);
            for (int grown = length + 1; grown <= LONGEST; grown++) {
                key += step;
                word = word << SHIFT | d;
                u128 candidate = encode(grown, word);
                int at = table.get(key);
                if (at < 0) {
                    table.put(key, least.size());
                    least.push_back(Least{0, 0, key});
                    least.back().set(candidate);
                } else if (candidate < least[at].value()) {
                    least[at].set(candidate);
                }
            }
        }
    }
    // a minimal forbidden multiset is not the least of its pair, while every
    // multiset with one digit fewer is; without its largest digit it is one
    // of the least words, so each least word is grown by one digit at its end
    std::vector<Vec> forbidden;
    int digits[LONGEST];
    for (const Least& r : least) {
        u128 value = r.value();
        int length = value >> (LOW_BITS + LENGTH_AT);
        if (length == 0 || length >= LONGEST) {
            continue;
        }
        u128 word = value ^ encode(length, 0);
        for (int i = 0; i < length; i++) {
            digits[i] = (word >> (SHIFT * (length - 1 - i))) & DIGIT_MASK;
        }
        for (int add = digits[length - 1]; add < base; add++) {
            unsigned key = r.key + add * width + add * add;
            if (least[table.get(key)].value() == encode(length + 1, word << SHIFT | add)) {
                continue;
            }
            bool is_minimal = true;
            for (int i = 0; i < length && is_minimal; i++) {
                int drop = digits[i];
                if (drop == add || (i > 0 && digits[i - 1] == drop)) {
                    continue;
                }
                u128 rest = 0;
                for (int j = 0; j < length; j++) {
                    if (j != i) {
                        rest = rest << SHIFT | digits[j];
                    }
                }
                rest = rest << SHIFT | add;
                const Least& shorter = least[table.get(key - drop * width - drop * drop)];
                is_minimal = shorter.value() == encode(length, rest);
            }
            if (is_minimal) {
                Vec f;
                for (int i = 0; i < length; i++) {
                    f.put(digits[i] - 1, f.get(digits[i] - 1) + 1);
                }
                f.put(add - 1, f.get(add - 1) + 1);
                forbidden.push_back(f);
            }
        }
    }
    std::vector<Least>().swap(least);
    std::vector<u64>().swap(table.slots);
    Patterns patterns(m);
    int top = patterns.solve(minimal(forbidden), m);
    std::vector<std::string> lines;
    patterns.each(top, [&](unsigned node) {
        Vec p = patterns.decode(node, m);
        std::string line;
        for (int i = 0; i < m; i++) {
            int c = p.get(i);
            if (c == STAR) {
                line += digit_char(i + 1);
                line += '*';
            } else {
                line += std::string(c, digit_char(i + 1));
            }
        }
        lines.push_back(line);
    });
    std::sort(lines.begin(), lines.end());
    std::string out;
    for (const std::string& line : lines) {
        out += line;
        out += '\n';
    }
    fputs(out.c_str(), stdout);
}
