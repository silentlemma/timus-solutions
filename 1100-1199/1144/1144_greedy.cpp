#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <queue>
#include <string>
#include <utility>
#include <vector>

// the local search stops after this many improvements
const int ROUNDS = 20000;
// an exact split of two generals may use at most this many bits of tables
const long long SPLIT_BITS = 4000000;
const int WORD = 64;
// the first line holds N, M and K
const int FIELDS = 3;

typedef std::pair<int, int> Box; // value and number of a box

std::vector<long long> sums;
std::vector<std::vector<Box>> boxes; // sorted, per general

void put(std::vector<Box> &list, Box b) {
    list.insert(std::lower_bound(list.begin(), list.end(), b), b);
}

// the move or swap of boxes from hi to lo that leaves the smallest gap
// between the two, if it is smaller than now
bool exchange(int hi, int lo) {
    long long d = sums[hi] - sums[lo], best = d;
    int bestA = -1, bestB = -1;
    std::vector<Box> &a = boxes[hi], &b = boxes[lo];
    auto consider = [&](long long t, int ia, int ib) {
        if (t > 0 && t < d && std::llabs(d - 2 * t) < best) {
            best = std::llabs(d - 2 * t);
            bestA = ia;
            bestB = ib;
        }
    };
    if (d <= 1)
        return false;
    int half = (int)(d / 2);
    if (a.size() > 1) {
        int k = std::lower_bound(a.begin(), a.end(), Box{half, -1}) - a.begin();
        for (int ia = k - 1; ia <= k; ia++)
            if (ia >= 0 && ia < (int)a.size())
                consider(a[ia].first, ia, -1);
    }
    for (int ia = 0; ia < (int)a.size(); ia++) {
        if (ia > 0 && a[ia].first == a[ia - 1].first)
            continue;
        int k = std::lower_bound(b.begin(), b.end(), Box{a[ia].first - half, -1}) - b.begin();
        for (int ib = k - 1; ib <= k; ib++)
            if (ib >= 0 && ib < (int)b.size())
                consider(a[ia].first - b[ib].first, ia, ib);
    }
    if (bestA < 0)
        return false;
    Box x = a[bestA];
    a.erase(a.begin() + bestA);
    sums[hi] -= x.first;
    sums[lo] += x.first;
    if (bestB >= 0) {
        Box y = b[bestB];
        b.erase(b.begin() + bestB);
        put(a, y);
        sums[hi] += y.first;
        sums[lo] -= y.first;
    }
    put(b, x);
    return true;
}

// the most even split of the boxes of hi and lo found by subset sums, if
// it narrows their gap and leaves each general a box
bool split(int hi, int lo) {
    std::vector<Box> items = boxes[hi];
    items.insert(items.end(), boxes[lo].begin(), boxes[lo].end());
    long long total = sums[hi] + sums[lo];
    int count = items.size(), words = (int)(total / WORD) + 1;
    if ((long long)(count + 1) * words * WORD > SPLIT_BITS)
        return false;
    // reach[k] holds the sums of subsets of the first k boxes
    std::vector<std::vector<uint64_t>> reach(count + 1, std::vector<uint64_t>(words, 0));
    reach[0][0] = 1;
    for (int k = 0; k < count; k++) {
        int v = items[k].first, shift = v / WORD, bits = v % WORD;
        std::vector<uint64_t> &from = reach[k], &to = reach[k + 1];
        for (int w = 0; w < words; w++) {
            uint64_t moved = 0;
            if (w - shift >= 0) {
                moved = from[w - shift] << bits;
                if (bits && w - shift - 1 >= 0)
                    moved |= from[w - shift - 1] >> (WORD - bits);
            }
            to[w] = from[w] | moved;
        }
    }
    auto has = [&](int k, long long t) { return reach[k][t / WORD] >> (t % WORD) & 1; };
    long long t = total / 2;
    while (t > 0 && !has(count, t))
        t--;
    if (t == 0 || total - 2 * t >= sums[hi] - sums[lo])
        return false;
    std::vector<Box> small, big;
    long long rest = t;
    for (int k = count - 1; k >= 0; k--)
        if (!has(k, rest)) {
            small.push_back(items[k]);
            rest -= items[k].first;
        } else
            big.push_back(items[k]);
    if (small.empty() || big.empty())
        return false;
    std::sort(small.begin(), small.end());
    std::sort(big.begin(), big.end());
    boxes[hi] = big;
    boxes[lo] = small;
    sums[hi] = total - t;
    sums[lo] = t;
    return true;
}

int main() {
    int n, m;
    long long limit;
    if (scanf("%d %d %lld", &n, &m, &limit) != FIELDS)
        return 0;
    std::vector<int> value(n);
    for (auto &v : value)
        if (scanf("%d", &v) != 1)
            return 0;
    // largest boxes first, each to the general with the least gold so far
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int x, int y) { return value[x] > value[y]; });
    sums.assign(m, 0);
    boxes.assign(m, {});
    std::priority_queue<std::pair<long long, int>, std::vector<std::pair<long long, int>>,
                        std::greater<>>
        poorest;
    for (int g = 0; g < m; g++)
        poorest.push({0, g});
    for (int i : order) {
        auto [s, g] = poorest.top();
        poorest.pop();
        boxes[g].push_back({value[i], i});
        sums[g] = s + value[i];
        poorest.push({sums[g], g});
    }
    for (auto &list : boxes)
        std::sort(list.begin(), list.end());
    // then even out the richest and the poorest general against the others
    std::vector<int> up(m), down(m);
    for (int round = 0; round < ROUNDS; round++) {
        int hi = std::max_element(sums.begin(), sums.end()) - sums.begin();
        int lo = std::min_element(sums.begin(), sums.end()) - sums.begin();
        if (sums[hi] - sums[lo] <= limit)
            break;
        if (exchange(hi, lo))
            continue;
        std::iota(up.begin(), up.end(), 0);
        std::stable_sort(up.begin(), up.end(), [&](int x, int y) { return sums[x] < sums[y]; });
        std::iota(down.begin(), down.end(), 0);
        std::stable_sort(down.begin(), down.end(), [&](int x, int y) { return sums[x] > sums[y]; });
        bool moved = false;
        for (int g : up)
            if (!moved && g != hi)
                moved = exchange(hi, g);
        for (int g : down)
            if (!moved && g != lo)
                moved = exchange(g, lo);
        moved = moved || split(hi, lo);
        for (int g : up)
            if (!moved && g != hi)
                moved = split(hi, g);
        for (int g : down)
            if (!moved && g != lo)
                moved = split(g, lo);
        if (!moved)
            break;
    }
    long long most = *std::max_element(sums.begin(), sums.end());
    long long least = *std::min_element(sums.begin(), sums.end());
    std::string out = std::to_string(most - least) + "\n";
    for (int g = 0; g < m; g++) {
        std::vector<int> ids;
        for (auto &b : boxes[g])
            ids.push_back(b.second + 1);
        std::sort(ids.begin(), ids.end());
        for (size_t k = 0; k < ids.size(); k++)
            out += (k ? " " : "") + std::to_string(ids[k]);
        out += "\n";
    }
    fputs(out.c_str(), stdout);
}
