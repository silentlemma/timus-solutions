#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <vector>

using namespace std;
typedef unsigned long long Hash;

// Four exact searches with growing time slices and perturbed orders, tried in
// turns until one places all ships: B (rows one at a time), C (B over the
// rare lengths only), D (C with residues modulo K checked exactly), A (ships).
const int MAX_SHIPS = 100;
const int MAX_ROWS = 10;
const int MAX_LEN = 100;
const int MAX_SUM = 10001; // fewer than 100 ships of at most 100
const double TIME_LIMIT = 0.9;
const int CLOCK_EVERY = 256; // nodes between looks at the clock
const int WORD = 64;
const int WORDS = (MAX_SUM + WORD - 1) / WORD;

int n, m;
int ships[MAX_SHIPS], rowLen[MAX_ROWS];
int v[MAX_SHIPS], shipId[MAX_SHIPS]; // current ship order: lengths and input positions
int rowId[MAX_ROWS];                 // the input row of search row b
int placed[MAX_SHIPS];               // the search row of ship i
long long nodes;
double attemptEnd; // the time when the current attempt stops
bool aborted;
clock_t started;

const unsigned SEED = 2463534242u;
unsigned rngState = SEED;
const int XS_A = 13, XS_B = 17, XS_C = 5; // xorshift32 shifts

unsigned rnd() {
    rngState ^= rngState << XS_A;
    rngState ^= rngState >> XS_B;
    rngState ^= rngState << XS_C;
    return rngState;
}

Hash rnd64() {
    Hash high = rnd();
    return high << (WORD / 2) | rnd();
}

// splitmix64 finalizer
const Hash GOLDEN = 0x9E3779B97F4A7C15ULL;
const Hash MIX1 = 0xBF58476D1CE4E5B9ULL;
const Hash MIX2 = 0x94D049BB133111EBULL;
const int MIX_S1 = 30, MIX_S2 = 27, MIX_S3 = 31;

Hash mix(Hash x) {
    x += GOLDEN;
    x = (x ^ (x >> MIX_S1)) * MIX1;
    x = (x ^ (x >> MIX_S2)) * MIX2;
    return x ^ (x >> MIX_S3);
}

double elapsed() { return double(clock() - started) / CLOCKS_PER_SEC; }

bool tick() {
    ++nodes;
    if (nodes % CLOCK_EVERY == 0 && elapsed() > attemptEnd) {
        aborted = true;
        return false;
    }
    return true;
}

// Ships go one by one into rows. Every row's remaining length must be a sum
// of unplaced ships, and the rows' ship counts must be able to add up.
int remain[MAX_ROWS];
bitset<MAX_SUM> suffixSums[MAX_SHIPS + 1];
vector<bitset<MAX_SUM>> countSums; // [first[i] + c]: sums of exactly c ships of i..n-1
int first[MAX_SHIPS + 2];
const int COUNT_BITS = 128;

void prepareA() {
    suffixSums[n].reset();
    suffixSums[n][0] = 1;
    for (int i = n - 1; i >= 0; i--)
        suffixSums[i] = suffixSums[i + 1] | (suffixSums[i + 1] << v[i]);
    int total = 0;
    for (int i = n; i >= 0; i--) {
        first[i] = total;
        total += n - i + 1;
    }
    countSums.assign(total, bitset<MAX_SUM>());
    countSums[first[n]][0] = 1;
    for (int i = n - 1; i >= 0; i--)
        for (int c = 0; c <= n - i; c++) {
            bitset<MAX_SUM> &d = countSums[first[i] + c];
            if (c <= n - i - 1)
                d = countSums[first[i + 1] + c];
            if (c >= 1)
                d |= countSums[first[i + 1] + c - 1] << v[i];
        }
}

bool countsFit(int i) {
    int total = n - i;
    bitset<COUNT_BITS> acc;
    acc[0] = 1;
    for (int b = 0; b < m; b++) {
        bitset<COUNT_BITS> next;
        bool any = false;
        for (int c = 0; c <= total; c++)
            if (countSums[first[i] + c][remain[b]]) {
                next |= acc << c;
                any = true;
            }
        if (!any)
            return false;
        acc = next;
    }
    return acc[total];
}

bool searchA(int i) {
    if (i == n)
        return true;
    if (!tick() || !countsFit(i))
        return false;
    int x = v[i];
    const bitset<MAX_SUM> &rest = suffixSums[i + 1];
    int forced = -1; // a row that cannot be completed without ship i
    for (int b = 0; b < m; b++)
        if (!rest[remain[b]]) {
            if (forced != -1)
                return false;
            forced = b;
        }
    int low = i > 0 && v[i - 1] == x ? placed[i - 1] : 0; // equal ships: rows in order
    int tried[MAX_ROWS], triedCount = 0;
    for (int b = forced != -1 ? forced : low; b < m; b++) {
        if (b < low)
            return false;
        int r = remain[b];
        if (r >= x && rest[r - x] && find(tried, tried + triedCount, r) == tried + triedCount) {
            tried[triedCount++] = r; // rows of equal remaining length are tried once
            remain[b] -= x;
            placed[i] = b;
            if (searchA(i + 1))
                return true;
            remain[b] += x;
            if (aborted)
                return false;
        }
        if (forced != -1)
            break;
    }
    return false;
}

bool runA() {
    prepareA();
    for (int b = 0; b < m; b++) {
        remain[b] = rowLen[rowId[b]];
        if (!suffixSums[0][remain[b]])
            return false;
    }
    return searchA(0);
}

// Failed states of the row searches, by a hash of the unused ships and the
// open rows; they do not depend on the order, so they survive restarts.
Hash zobrist[MAX_LEN + 1]; // a random key per ship length
const int MEMO_BITS = 20;
const int MEMO_SIZE = 1 << MEMO_BITS;
const int PROBES = 8;
Hash memo[MEMO_SIZE];

bool known(Hash k) {
    size_t p = k >> (WORD - MEMO_BITS);
    for (int t = 0; t < PROBES; t++) {
        Hash e = memo[(p + t) % MEMO_SIZE];
        if (e == k)
            return true;
        if (!e)
            return false;
    }
    return false;
}

void remember(Hash k) {
    size_t p = k >> (WORD - MEMO_BITS);
    for (int t = 0; t < PROBES; t++) {
        Hash &e = memo[(p + t) % MEMO_SIZE];
        if (!e || e == k) {
            e = k;
            return;
        }
    }
    memo[(p + k % PROBES) % MEMO_SIZE] = k;
}

// For strategy D: ships not divisible by mod fall into classes by residue.
// Rows b.. can only be completed if the class counts left split among them so
// that each row gets its length modulo mod: a DP over (row, counts), cached.
const int CHECK_BITS = 21;
const int CHECK_SIZE = 1 << CHECK_BITS;
const int CHECK_PROBES = 4;
const double MAX_CODES = 1e17; // the count vectors must fit in 64 bits
const long long QUERY_BUDGET = 100000;
const int MAX_OVER = 5;   // queries over budget before the check gives up
const int ROW_RADIX = 16; // more than the rows
const int SLOT_SHIFT = 8;
const Hash SALT = 0x1234567ULL;
Hash checked[CHECK_SIZE]; // (key with the low bit cleared) | feasible

struct Residues {
    int mod, classes;
    int residue[MAX_LEN], count[MAX_LEN]; // classes by count, the largest last
    Hash radix[MAX_LEN];
    int target[MAX_ROWS]; // row lengths modulo mod
    Hash orderSalt, full;
    long long ops, budget;
    bool broken;   // the current query is over budget: the answer is "feasible"
    int overCount; // queries over budget in this attempt

    Hash rotate(Hash x, int s) const { return s ? ((x << s) | (x >> (mod - s))) & full : x; }

    // Row b takes c of class j and of the classes after it (R: the counts
    // left, r: the residue so far, reach[j]: residues the classes j.. give).
    bool split(int b, const int *R, const Hash *reach, Hash code, int j, int r, Hash taken) {
        if (++ops > budget) {
            broken = true;
            return true;
        }
        int need = (target[b] - r + mod) % mod;
        if (!((reach[j] >> need) & 1))
            return false;
        if (j == classes)
            return feasible(b + 1, code - taken);
        if (j == classes - 1) { // the last class: its count is fixed modulo mod
            for (int c = 0; c <= R[j] && c < mod; c++) {
                if (c * residue[j] % mod != need)
                    continue;
                for (int cc = c; cc <= R[j]; cc += mod) {
                    if (++ops > budget) {
                        broken = true;
                        return true;
                    }
                    if (feasible(b + 1, code - taken - (Hash)cc * radix[j]) || broken)
                        return true;
                }
            }
            return false;
        }
        for (int c = 0; c <= R[j]; c++)
            if (split(b, R, reach, code, j + 1, (r + c * residue[j]) % mod,
                      taken + (Hash)c * radix[j]) ||
                broken)
                return true;
        return false;
    }

    bool feasible(int b, Hash code) {
        if (broken)
            return true;
        int R[MAX_LEN];
        Hash c = code;
        for (int j = 0; j < classes; j++) {
            R[j] = c % (count[j] + 1);
            c /= count[j] + 1;
        }
        if (b == m - 1) {
            int r = 0;
            for (int j = 0; j < classes; j++)
                r = (r + R[j] * residue[j]) % mod;
            return r == target[b];
        }
        Hash key = mix(orderSalt ^ mix(code * ROW_RADIX + b)) & ~1ULL;
        size_t p = key >> (WORD - CHECK_BITS);
        for (int t = 0; t < CHECK_PROBES; t++) {
            Hash e = checked[(p + t) % CHECK_SIZE];
            if ((e & ~1ULL) == key)
                return e & 1;
        }
        Hash reach[MAX_LEN + 1];
        reach[classes] = 1;
        for (int j = classes - 1; j >= 0; j--) {
            reach[j] = 0;
            for (int t = 0; t <= R[j] && t < mod; t++)
                reach[j] |= rotate(reach[j + 1], t * residue[j] % mod);
            ops += min(R[j], mod) + 1;
        }
        if (ops > budget) {
            broken = true;
            return true;
        }
        bool ok = split(b, R, reach, code, 0, 0, 0);
        if (broken)
            return true;
        size_t q = (p + (key >> SLOT_SHIFT) % CHECK_PROBES) % CHECK_SIZE;
        for (int t = 0; t < CHECK_PROBES; t++)
            if (!checked[(p + t) % CHECK_SIZE]) {
                q = (p + t) % CHECK_SIZE;
                break;
            }
        checked[q] = key | ok;
        return ok;
    }

    // the classes for modulus k; false if the count vectors do not fit in 64 bits
    bool init(int k) {
        int perResidue[MAX_LEN] = {0};
        for (int i = 0; i < n; i++)
            if (ships[i] % k)
                perResidue[ships[i] % k]++;
        mod = k;
        classes = 0;
        full = (1ULL << k) - 1;
        vector<pair<int, int>> list;
        for (int r = 1; r < k; r++)
            if (perResidue[r])
                list.push_back({perResidue[r], r});
        sort(list.begin(), list.end());
        double total = 1;
        Hash s = 1;
        for (auto [cnt, r] : list) {
            residue[classes] = r;
            count[classes] = cnt;
            radix[classes++] = s;
            total *= cnt + 1;
            if (total > MAX_CODES)
                return false;
            s *= cnt + 1;
        }
        return true;
    }

    Hash fullCode() const {
        Hash c = 0;
        for (int j = 0; j < classes; j++)
            c += (Hash)count[j] * radix[j];
        return c;
    }

    // a query from a search: limited effort, "feasible" when it runs out
    bool query(int b, Hash code) {
        if (overCount > MAX_OVER || elapsed() > attemptEnd)
            return true;
        ops = 0;
        broken = false;
        bool ok = feasible(b, code);
        overCount += broken;
        return ok;
    }

    // a new attempt with these row lengths, in search order
    void setRows(const int *len) {
        orderSalt = mix(SALT + mod);
        for (int b = 0; b < m; b++) {
            target[b] = len[b] % mod;
            orderSalt = mix(orderSalt ^ (Hash)len[b]);
        }
        overCount = 0;
        budget = QUERY_BUDGET;
    }
};

// a bitset of run-time width: a row search needs sums up to its longest row
struct Bits {
    Hash w[WORDS];
    bool get(int x) const { return (w[x / WORD] >> (x % WORD)) & 1; }
    void one(int words) {
        w[0] = 1;
        fill(w + 1, w + words, 0);
    }
    void copy(const Bits &s, int words) { copy_n(s.w, words, w); }
    void shiftOr(const Bits &s, int sh, int words) { // this = s | s << sh; s may be this
        int ws = sh / WORD, bs = sh % WORD;
        for (int i = words - 1; i >= 0; i--) {
            Hash x = s.w[i];
            int j = i - ws;
            if (j >= 0) {
                x |= s.w[j] << bs;
                if (bs && j > 0)
                    x |= s.w[j - 1] >> (WORD - bs);
            }
            w[i] = x;
        }
    }
};

// Rows are filled one at a time; inside a row each ship is taken or skipped
// (equal ships skipped together). Ships kept..n-1, if any, are deferred: a
// row then only needs a remainder they can make, and `sub` places them last.
const int MAX_CHECKS = 13;
const Hash ROW_SALT = 0x51ED27ULL, REMAINDER_SALT = 0xC0FFEEULL, TAG_SALT = 0x7A6ULL;

struct RowSearch {
    int n, m, kept;
    int v[MAX_SHIPS], len[MAX_ROWS], where[MAX_SHIPS], remainder[MAX_ROWS];
    bool used[MAX_SHIPS];
    Hash tag, shipsHash, remainderHash; // tag: which lengths are deferred (0: none)
    int words;
    Bits sums[MAX_ROWS][MAX_SHIPS + 1]; // per row: sums of unused ships pos.. (+ deferred)
    Bits deferredSums;
    RowSearch *sub;
    int checks; // residue checks: valid since closed rows are complete modulo each
    Residues *check[MAX_CHECKS];
    int cls[MAX_CHECKS][MAX_SHIPS]; // the class of ship i in check t, -1 if divisible
    Hash code[MAX_CHECKS];          // mixed-radix codes of the unused class counts

    void take(int pos, int sign) {
        for (int t = 0; t < checks; t++)
            if (cls[t][pos] >= 0)
                code[t] += sign * check[t]->radix[cls[t][pos]];
    }

    bool placeDeferred() {
        RowSearch &s = *sub;
        s.n = s.kept = n - kept;
        s.m = m;
        s.checks = 0;
        copy(v + kept, v + n, s.v);
        copy(remainder, remainder + m, s.len);
        if (!s.run(0))
            return false;
        copy(s.where, s.where + s.n, where + kept);
        return true;
    }

    bool fill(int b, int pos, int r) {
        if (!tick())
            return false;
        while (pos < kept && used[pos])
            pos++;
        if (r == 0 || pos >= kept) { // row b is done; the rest comes from deferred ships
            if (r > 0 && (kept == n || !deferredSums.get(r)))
                return false;
            remainder[b] = r;
            remainderHash += kept < n ? mix(r) : 0;
            bool ok = open(b + 1);
            remainderHash -= kept < n ? mix(r) : 0;
            return ok;
        }
        int x = v[pos];
        if (x <= r && sums[b][pos + 1].get(r - x)) {
            used[pos] = true;
            where[pos] = b;
            shipsHash -= zobrist[x];
            take(pos, -1);
            if (fill(b, pos + 1, r - x))
                return true;
            used[pos] = false;
            shipsHash += zobrist[x];
            take(pos, 1);
            if (aborted)
                return false;
        }
        int q = pos + 1; // skip ship x and all its copies
        while (q < kept && v[q] == x)
            q++;
        return sums[b][q].get(r) && fill(b, q, r);
    }

    bool open(int b) {
        if (b == m)
            return placeDeferred();
        if (b == m - 1) { // the last row takes all the ships left
            int s = 0;
            for (int i = 0; i < kept; i++)
                if (!used[i])
                    s += v[i], where[i] = b;
            if (kept == n)
                return true;
            int r = len[b] - s;
            if (r < 0 || !deferredSums.get(r))
                return false;
            remainder[b] = r;
            return placeDeferred();
        }
        Hash rowsHash = tag;
        for (int c = b; c < m; c++)
            rowsHash += mix(len[c] + ROW_SALT);
        Hash key = (mix(shipsHash ^ mix(rowsHash)) + mix(remainderHash ^ REMAINDER_SALT)) | 1;
        if (known(key))
            return false;
        for (int t = 0; t < checks; t++)
            if (!check[t]->query(b, code[t])) {
                remember(key);
                return false;
            }
        Bits *s = sums[b];
        if (kept == n)
            s[kept].one(words);
        else
            s[kept].copy(deferredSums, words);
        for (int i = kept - 1; i >= 0; i--) {
            if (used[i])
                s[i].copy(s[i + 1], words);
            else
                s[i].shiftOr(s[i + 1], v[i], words);
        }
        for (int c = b; c < m; c++)
            if (!s[0].get(len[c])) {
                remember(key);
                return false;
            }
        bool ok = fill(b, 0, len[b]);
        if (!ok && !aborted)
            remember(key);
        return ok;
    }

    bool run(Hash t) {
        tag = t;
        words = *max_element(len, len + m) / WORD + 1;
        shipsHash = remainderHash = 0;
        for (int i = 0; i < checks; i++)
            code[i] = check[i]->fullCode();
        fill_n(used, n, false);
        for (int i = 0; i < kept; i++)
            shipsHash += zobrist[v[i]];
        if (kept < n) {
            deferredSums.one(words);
            for (int i = kept; i < n; i++)
                deferredSums.shiftOr(deferredSums, v[i], words);
        }
        return open(0);
    }
};

RowSearch mainSearch, subSearch;
Residues residuePool[MAX_CHECKS];

bool runRows(int kept, Residues **checks, int checkCount) {
    RowSearch &s = mainSearch;
    s.n = n;
    s.m = m;
    s.kept = kept;
    s.sub = &subSearch;
    s.checks = checkCount;
    copy(v, v + n, s.v);
    for (int b = 0; b < m; b++)
        s.len[b] = rowLen[rowId[b]];
    for (int t = 0; t < checkCount; t++) {
        Residues *r = s.check[t] = checks[t];
        int classOf[MAX_LEN];
        classOf[0] = -1;
        for (int j = 0; j < r->classes; j++)
            classOf[r->residue[j]] = j;
        for (int i = 0; i < n; i++)
            s.cls[t][i] = classOf[v[i] % r->mod];
        r->setRows(s.len);
    }
    Hash tag = 0;
    if (kept < n) {
        bool rare[MAX_LEN + 1] = {false};
        for (int i = 0; i < kept; i++)
            rare[v[i]] = true;
        tag = TAG_SALT;
        for (int x = 1; x <= MAX_LEN; x++)
            if (rare[x])
                tag = mix(tag ^ (Hash)x);
    }
    if (!s.run(tag))
        return false;
    copy(s.where, s.where + n, placed);
    return true;
}

const int MOD_MIN = 2, MOD_MAX = 50; // moduli for D
const int SHARE = 4;                 // a modulus must divide a quarter of the ships
const int SMALL_MOD_MAX = 6;         // B also checks moduli up to this
const int TOP_MODS = 4;
const int SCORE_SCALE = 100;
const int SLOTS = 5; // B, B with rows ascending, C, D, A
const int STRATEGY_B = 0;
const int STRATEGY_C = 1;
const int STRATEGY_D = 2;
const int STRATEGY_A = 3;
const int RARE_LEVELS = 3;  // C: "rare" means at most 1..3 copies
const int KEY_SCALE = 1000; // ship order keys
const int MAX_NOISE = 30;
const long long RARE_FIRST = 1000000000LL, FREQUENT_FIRST = 1000000;
const double FIRST_SLICE = 0.003, SLICE_GROWTH = 1.6;
const int MAX_GROWTH = 20;

int main() {
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    for (int i = 0; i < n; i++)
        scanf("%d", &ships[i]);
    for (int j = 0; j < m; j++)
        scanf("%d", &rowLen[j]);
    started = clock();
    int copies[MAX_LEN + 1] = {0};
    for (int i = 0; i < n; i++)
        copies[ships[i]]++;
    for (int x = 0; x <= MAX_LEN; x++)
        zobrist[x] = rnd64();
    bool sane = true;
    for (int j = 0; j < m; j++)
        sane &= rowLen[j] > 0 && rowLen[j] < MAX_SUM;

    // moduli for D from two rankings: many multiples of a large k, and the
    // fewest non-multiples (say all ships even but one odd ship per row)
    vector<pair<long long, int>> byScore, byFew;
    for (int k = MOD_MIN; k <= MOD_MAX; k++) {
        int d = count_if(ships, ships + n, [k](int x) { return x % k == 0; });
        if (d < n && d >= max(MOD_MIN, n / SHARE)) {
            byScore.push_back({-(long long)d * k, k});
            byFew.push_back({(long long)(n - d) * SCORE_SCALE - k, k});
        }
    }
    sort(byScore.begin(), byScore.end());
    sort(byFew.begin(), byFew.end());
    vector<int> dMods;
    for (int c = 0; c < TOP_MODS; c++)
        for (auto *list : {&byScore, &byFew})
            if (c < (int)list->size() &&
                find(dMods.begin(), dMods.end(), (*list)[c].second) == dMods.end())
                dMods.push_back((*list)[c].second);
    // residue checks: D's moduli, plus small ones that B checks with them
    Residues *dChecks[2 * TOP_MODS], *bChecks[MAX_CHECKS];
    int bCount = 0;
    vector<int> mods = dMods;
    for (int k = MOD_MIN; k <= SMALL_MOD_MAX; k++)
        if (find(mods.begin(), mods.end(), k) == mods.end())
            mods.push_back(k);
    for (size_t c = 0; c < mods.size(); c++) {
        Residues &r = residuePool[bCount];
        bool ok = r.init(mods[c]) && r.classes > 0;
        if (c < dMods.size())
            dChecks[c] = ok ? &r : nullptr;
        if (ok)
            bChecks[bCount++] = &r;
    }

    vector<long long> key(n);
    vector<int> order(n);
    bool solved = false;
    for (int attempt = 0; sane && !solved; attempt++) {
        int slot = attempt % SLOTS, round = attempt / SLOTS;
        int strategy = slot <= 1 ? 0 : slot - 1; // 0 B, 1 C, 2 D, 3 A
        bool rowsUp = slot == 1;
        int rareLevel = 1 + round % RARE_LEVELS;
        int ci = dMods.empty() ? -1 : round % (int)dMods.size();
        int K = ci < 0 ? 0 : dMods[ci];
        bool rare[MAX_LEN + 1];
        for (int x = 1; x <= MAX_LEN; x++)
            rare[x] = strategy == STRATEGY_C ? copies[x] <= rareLevel
                                             : strategy == STRATEGY_D && K && x % K != 0;
        if (strategy == STRATEGY_D && !K)
            strategy = STRATEGY_B;
        int kept = count_if(ships, ships + n, [&](int x) { return rare[x]; });
        if ((strategy == STRATEGY_C || strategy == STRATEGY_D) && (kept == 0 || kept == n))
            strategy = STRATEGY_B;

        // ship order: B longest first, C and D rare lengths first, A by copies,
        // later rounds add noise, equal lengths stay together
        long long lengthKey[MAX_LEN + 1];
        for (int x = 1; x <= MAX_LEN; x++) {
            lengthKey[x] = (long long)x * KEY_SCALE;
            if (round)
                lengthKey[x] += rnd() % (KEY_SCALE * (unsigned)min(MAX_NOISE, round + 1));
            if ((strategy == STRATEGY_C || strategy == STRATEGY_D) && rare[x])
                lengthKey[x] += RARE_FIRST;
            if (strategy == STRATEGY_A)
                lengthKey[x] -= (long long)copies[x] * FREQUENT_FIRST;
        }
        for (int i = 0; i < n; i++) {
            order[i] = i;
            key[i] = lengthKey[ships[i]];
        }
        sort(order.begin(), order.end(), [&](int p, int q) {
            return key[p] != key[q] ? key[p] > key[q] : ships[p] > ships[q];
        });
        for (int i = 0; i < n; i++) {
            shipId[i] = order[i];
            v[i] = ships[order[i]];
        }
        // rows: longest first in round 0, then random; shortest first for the
        // second B slot and for D in even rounds (the last row absorbs the rest)
        for (int j = 0; j < m; j++)
            rowId[j] = j;
        if (rowsUp || (strategy == STRATEGY_D && round % 2 == 0))
            sort(rowId, rowId + m, [](int p, int q) { return rowLen[p] < rowLen[q]; });
        else if (round == 0)
            sort(rowId, rowId + m, [](int p, int q) { return rowLen[p] > rowLen[q]; });
        else
            for (int j = m - 1; j > 0; j--)
                swap(rowId[j], rowId[rnd() % (j + 1)]);

        nodes = 0;
        aborted = false;
        attemptEnd =
            min(TIME_LIMIT, elapsed() + FIRST_SLICE * pow(SLICE_GROWTH, min(round, MAX_GROWTH)));
        if (strategy == STRATEGY_B)
            solved = runRows(n, bChecks, (round + slot) % 2 == 0 ? bCount : 0);
        else if (strategy == STRATEGY_C)
            solved = runRows(kept, nullptr, 0);
        else if (strategy == STRATEGY_D)
            solved = runRows(kept, &dChecks[ci], dChecks[ci] ? 1 : 0);
        else
            solved = runA();
        if (!solved && elapsed() > TIME_LIMIT)
            break;
    }

    vector<vector<int>> rows(m);
    for (int i = 0; i < n; i++)
        rows[rowId[placed[i]]].push_back(ships[shipId[i]]);
    for (int j = 0; j < m; j++) {
        printf("%d\n", (int)rows[j].size());
        for (size_t k = 0; k < rows[j].size(); k++)
            printf(k ? " %d" : "%d", rows[j][k]);
        printf("\n");
    }
}
