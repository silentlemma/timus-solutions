#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

typedef unsigned long long u64;
typedef std::vector<int> Shape;  // rank counts in decreasing order, no zeros
const std::string RANKS = "23456789TJQKA";
const int RANK_COUNT = 13;
const int NIBBLE = 4;  // a shape is packed four bits per count (counts stay below 16)

int n, m, k, combosCount;
std::vector<Shape> combos;
std::map<u64, int> bestCache;
std::vector<double> fact;

u64 pack(const Shape& shape) {
    u64 key = 0;
    for (int x : shape) {
        key = key << NIBBLE | x;
    }
    return key;
}

// the most valuable combination a hand with these sorted counts holds, or
// -1: (v1, ..., vL) fits when the i-th largest count is at least the i-th v
int best(const Shape& hand) {
    u64 key = pack(hand) << NIBBLE | hand.size();
    auto it = bestCache.find(key);
    if (it != bestCache.end()) {
        return it->second;
    }
    int found = -1;
    for (int c = combosCount - 1; c >= 0 && found < 0; c--) {
        const Shape& need = combos[c];
        bool fits = need.size() <= hand.size();
        for (size_t i = 0; fits && i < need.size(); i++) {
            fits = hand[i] >= need[i];
        }
        if (fits) {
            found = c;
        }
    }
    return bestCache[key] = found;
}

// the partitions of total into at most parts positive parts, decreasing
std::vector<Shape> partitions(int total, int parts) {
    std::vector<Shape> out;
    Shape cur;
    std::function<void(int, int)> build = [&](int rest, int top) {
        if (rest == 0) {
            out.push_back(cur);
            return;
        }
        if ((int)cur.size() == parts) {
            return;
        }
        for (int x = std::min(rest, top); x > 0; x--) {
            cur.push_back(x);
            build(rest - x, x);
            cur.pop_back();
        }
    };
    build(total, total);
    return out;
}

std::map<Shape, std::vector<double>> rivalCache;

// the chance, for each combination, that a rival's best one is cheaper,
// shifted by one place. Ranks with equal common counts are interchangeable,
// so each group takes a partition of its share of the rival's cards
const std::vector<double>& rival(const Shape& common) {
    auto it = rivalCache.find(common);
    if (it != rivalCache.end()) {
        return it->second;
    }
    std::map<int, int> groups;
    for (int v : common) {
        groups[v]++;
    }
    std::map<std::pair<Shape, int>, double> states = {{{Shape(), 0}, 1.0}};
    for (auto [v, g] : groups) {
        std::map<std::pair<Shape, int>, double> next;
        for (const auto& [state, w] : states) {
            const auto& [shape, used] = state;
            for (int s = 0; s + used <= m; s++) {
                for (const Shape& p : partitions(s, g)) {
                    double ways = fact[g] / fact[g - p.size()];
                    std::map<int, int> mult;
                    for (int x : p) {
                        mult[x]++;
                        ways /= fact[x];
                    }
                    for (auto [x, c] : mult) {
                        ways /= fact[c];
                    }
                    Shape merged = shape;
                    for (int x : p) {
                        merged.push_back(v + x);
                    }
                    if (v > 0) {
                        merged.insert(merged.end(), g - p.size(), v);
                    }
                    std::sort(merged.rbegin(), merged.rend());
                    next[{merged, used + s}] += w * ways;
                }
            }
        }
        states.swap(next);
    }
    double scale = fact[m] / std::pow((double)RANK_COUNT, m);
    std::vector<double> dist(combosCount + 1, 0.0), below(combosCount + 1, 0.0);
    for (const auto& [state, w] : states) {
        if (state.second == m) {
            dist[best(state.first) + 1] += w * scale;
        }
    }
    for (int c = 0; c < combosCount; c++) {
        below[c + 1] = below[c] + dist[c];
    }
    return rivalCache[common] = below;
}

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::istringstream(line) >> n >> m >> k;
    std::string ownText, shownText;
    std::getline(std::cin, ownText);
    std::getline(std::cin, shownText);
    std::vector<int> own(RANK_COUNT, 0), shown(RANK_COUNT, 0);
    int shownCount = 0;
    for (char c : ownText) {
        if (RANKS.find(c) != std::string::npos) {
            own[RANKS.find(c)]++;
        }
    }
    for (char c : shownText) {
        if (RANKS.find(c) != std::string::npos) {
            shown[RANKS.find(c)]++;
            shownCount++;
        }
    }
    std::cin >> combosCount;
    for (int c = 0; c < combosCount; c++) {
        int size;
        std::cin >> size;
        Shape need(size);
        for (int& v : need) {
            std::cin >> v;
        }
        std::sort(need.rbegin(), need.rend());
        combos.push_back(need);
    }
    fact.assign(m + k + RANK_COUNT + 1, 1.0);
    for (size_t i = 1; i < fact.size(); i++) {
        fact[i] = fact[i - 1] * i;
    }
    // the hidden common cards: every way to spread them over the ranks
    int hidden = k - shownCount;
    double answer = 0, scale = fact[hidden] / std::pow((double)RANK_COUNT, hidden);
    std::vector<int> common(RANK_COUNT);
    std::function<void(int, int, double)> spread = [&](int r, int left, double weight) {
        if (r == RANK_COUNT - 1) {
            common[r] = shown[r] + left;
            weight /= fact[left];
            Shape mine;
            for (int i = 0; i < RANK_COUNT; i++) {
                if (common[i] + own[i] > 0) {
                    mine.push_back(common[i] + own[i]);
                }
            }
            std::sort(mine.rbegin(), mine.rend());
            int top = best(mine);
            if (top >= 0) {
                Shape sorted = common;
                std::sort(sorted.rbegin(), sorted.rend());
                double beat = rival(sorted)[top + 1];
                answer += weight * scale * std::pow(beat, n - 1);
            }
            return;
        }
        for (int x = 0; x <= left; x++) {
            common[r] = shown[r] + x;
            spread(r + 1, left - x, weight / fact[x]);
        }
    };
    spread(0, hidden, 1.0);
    printf("%.10f\n", answer);
}
