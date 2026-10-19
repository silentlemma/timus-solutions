#include <algorithm>
#include <cstdio>
#include <map>
#include <numeric>
#include <utility>
#include <vector>

const int SEATS = 4;  // compartment seats in a block
const int SIDES = 2;  // side seats in a block

using Group = std::vector<int>;

int main() {
    int n, m;
    if (scanf("%d", &n) != 1) return 0;
    int people = (SEATS + SIDES) * n;
    std::vector<char> wish(people + 1);
    scanf("%s", wish.data());
    scanf("%d", &m);
    std::vector<int> parent(people);
    std::iota(parent.begin(), parent.end(), 0);
    auto find = [&](int x) {
        while (parent[x] != x) x = parent[x] = parent[parent[x]];
        return x;
    };
    for (int k = 0; k < m; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        parent[find(a - 1)] = find(b - 1);
    }
    std::map<int, Group> groups;
    for (int p = 0; p < people; p++) groups[find(p)].push_back(p + 1);
    // a group of friends wants a compartment seats and b side seats; a block
    // holds one group with b = 2, or two groups with b = 1, and groups with
    // b = 0 fill the compartment seats left: kind[b][a]
    std::vector<std::vector<std::vector<Group>>> kind(
        SIDES + 1, std::vector<std::vector<Group>>(SEATS + 1));
    for (auto &[root, g] : groups) {
        int a = 0;
        for (int p : g) a += wish[p - 1] == '1';
        kind[g.size() - a][a].push_back(g);
    }
    auto &fillers = kind[0], &halves = kind[1], &wholes = kind[SIDES];
    auto size = [](const std::vector<Group> &x) { return (int)x.size(); };
    int s0 = size(halves[0]), s1 = size(halves[1]), s2 = size(halves[2]);
    int s3 = size(halves[SEATS - 1]), s4 = size(halves[SEATS]);
    int t0 = size(wholes[0]), t1 = size(wholes[1]), t2 = size(wholes[2]);
    int f2 = size(fillers[2]), f3 = size(fillers[SEATS - 1]), f4 = size(fillers[SEATS]);
    // can the fillers fill blocks with c4, c3, c2 free compartment seats (and
    // some with 1)? fours need a 4, threes take a 3 first and then a 4, twos
    // take what is left of the 2s, 3s and 4s
    auto fits = [&](int c4, int c3, int c2) {
        if (f4 > c4 || f3 > c3 + c4 - f4) return false;
        int late = std::max(0, f3 - c3);  // threes in blocks with 4 free seats
        return f2 <= c2 + (c3 - f3 + late) + 2 * (c4 - f4 - late);
    };
    // two halves with a1 and a2 leave 4 - a1 - a2 free seats; merging the
    // free seats of two blocks never hurts, so threes pair with ones when they
    // can, and two (0, 2) pairs would rather be (2, 2) and (0, 0)
    int x31 = std::min(s3, s1), x30 = s3 - x31, ones = s1 - x31, zeros = s0 - s4 - x30;
    std::map<std::pair<int, int>, int> plan;
    for (int x20 = 0; x20 <= 1 && plan.empty(); x20++) {
        for (int x21 = 0; x21 <= std::min(s2 - x20, ones) && plan.empty(); x21++) {
            // with x11 pairs (1, 1) the zeros left pair up as base + 2 x11
            int base = zeros - x20 - ones + x21;
            if ((s2 - x21 - x20) % 2 != 0 || base % 2 != 0) continue;
            // x11 must leave both kinds of pairs possible and give the fours and
            // the threes their blocks; the room for twos rises until the free
            // threes run short of threes and falls after that
            int low = std::max({0, -base / 2, f4 - t0 - base / 2});
            int high = std::min((ones - x21) / 2, t0 + t1 + ones - x21 + base / 2 - f3 - f4);
            int peak = std::min(std::max((t1 + ones - x21 - f3) / 2, low), high);
            for (int x11 = peak - 1; x11 <= peak + 1; x11++) {
                int x10 = ones - x21 - 2 * x11, x00 = base / 2 + x11;
                if (low <= x11 && x11 <= high && fits(t0 + x00, t1 + x10, t2 + x20 + x11)) {
                    plan = {{{SEATS, 0}, s4},
                            {{SEATS - 1, 1}, x31},
                            {{SEATS - 1, 0}, x30},
                            {{2, 2}, (s2 - x21 - x20) / 2},
                            {{2, 1}, x21},
                            {{2, 0}, x20},
                            {{1, 1}, x11},
                            {{1, 0}, x10},
                            {{0, 0}, x00}};
                    break;
                }
            }
        }
    }
    std::vector<std::pair<Group, int>> blocks;  // members, free compartment seats
    for (int a = 0; a <= SEATS; a++) {
        for (auto &g : wholes[a]) blocks.push_back({g, SEATS - a});
    }
    for (auto &[kinds, count] : plan) {
        auto [a, b] = kinds;
        for (int k = 0; k < count; k++) {
            Group g = halves[a].back();
            halves[a].pop_back();
            g.insert(g.end(), halves[b].back().begin(), halves[b].back().end());
            halves[b].pop_back();
            blocks.push_back({g, SEATS - a - b});
        }
    }
    // the fillers, largest first, as the check above assumes
    std::vector<std::vector<int>> free(SEATS + 1);
    for (size_t i = 0; i < blocks.size(); i++) free[blocks[i].second].push_back(i);
    for (int sz = SEATS; sz >= 1; sz--) {
        for (auto &g : fillers[sz]) {
            int seats = sz;
            while (free[seats].empty()) seats++;
            int i = free[seats].back();
            free[seats].pop_back();
            blocks[i].first.insert(blocks[i].first.end(), g.begin(), g.end());
            free[seats - sz].push_back(i);
        }
    }
    for (auto &[members, seats] : blocks) {
        for (size_t k = 0; k < members.size(); k++) printf(k ? " %d" : "%d", members[k]);
        printf("\n");
    }
    return 0;
}
