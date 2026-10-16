#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

const long long SCALE = 1000;
const long long SAFE = 256 * SCALE;
const int DEODORANT = 1, PERFUME = 2, BOTH = DEODORANT | PERFUME;
const long long DOWN_NUM = 3, DOWN_DEN = 4;
const long long UP_NUM = 11, UP_DEN = 10;
const int INF = 1 << 30;

struct Move {
    int kind, deodorized, perfumed, set;
};

std::vector<long long> total;
std::vector<Move> moves;

// keep the sets not inside another one: carrying more costs nothing,
// since fruit already outside can be brought back and carried again
void addMaximal(std::vector<int> sets, int kind, int i, int j) {
    std::stable_sort(sets.begin(), sets.end(), [](int a, int b) {
        return __builtin_popcount(a) > __builtin_popcount(b);
    });
    std::vector<int> kept;
    for (int a : sets) {
        bool inside = false;
        for (int b : kept) {
            if ((a & b) == a) inside = true;
        }
        if (!inside) {
            kept.push_back(a);
            moves.push_back({kind, i, j, a});
        }
    }
}

std::string names(int set, int n) {
    std::string s;
    int count = 0;
    for (int k = 0; k < n; k++) {
        if (set >> k & 1) {
            s += " " + std::to_string(k + 1);
            count++;
        }
    }
    return std::to_string(count) + s;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // aromas times 1000 keep 3/4, 11/10 and both together whole
    std::vector<long long> w(n);
    for (auto &x : w) {
        scanf("%lld", &x);
        x *= SCALE;
    }
    int full = (1 << n) - 1;
    total.assign(full + 1, 0);
    for (int m = 1; m <= full; m++) total[m] = total[m & (m - 1)] + w[__builtin_ctz(m)];
    auto collect = [&](int need, long long change) {
        std::vector<int> sets;
        for (int m = 1; m <= full; m++) {
            if ((m & need) == need && (total[m] + change) % SAFE == 0) sets.push_back(m);
        }
        return sets;
    };
    addMaximal(collect(0, 0), 0, -1, -1);
    // what each spray adds to the total of a set holding the fruit
    std::vector<long long> weaker(n), stronger(n);
    for (int i = 0; i < n; i++) {
        weaker[i] = w[i] * DOWN_NUM / DOWN_DEN - w[i];
        stronger[i] = w[i] * UP_NUM / UP_DEN - w[i];
    }
    for (int i = 0; i < n; i++) {
        addMaximal(collect(1 << i, weaker[i]), DEODORANT, i, -1);
        addMaximal(collect(1 << i, stronger[i]), PERFUME, -1, i);
        for (int j = 0; j < n; j++) {
            long long change = weaker[i] + stronger[j];
            if (i == j) change = w[i] * DOWN_NUM * UP_NUM / (DOWN_DEN * UP_DEN) - w[i];
            addMaximal(collect(1 << i | 1 << j, change), BOTH, i, j);
        }
    }
    // best[used][mask]: fewest exits that get the fruit of mask out
    std::vector<std::vector<int>> best(BOTH + 1, std::vector<int>(full + 1, INF));
    std::vector<std::vector<int>> choice(BOTH + 1, std::vector<int>(full + 1, -1));
    for (int used = 0; used <= BOTH; used++) best[used][0] = 0;
    for (int mask = 1; mask <= full; mask++) {
        for (int used = 0; used <= BOTH; used++) {
            for (size_t k = 0; k < moves.size(); k++) {
                const Move &mv = moves[k];
                if ((mv.kind & used) || !(mv.set & mask)) continue;
                int value = best[used | mv.kind][mask & ~mv.set] + 1;
                if (value < best[used][mask]) {
                    best[used][mask] = value;
                    choice[used][mask] = k;
                }
            }
        }
    }
    if (best[0][full] >= INF) {
        printf("IMPOSSIBLE\n");
        return 0;
    }
    std::vector<std::string> out;
    for (int mask = full, used = 0; mask;) {
        const Move &mv = moves[choice[used][mask]];
        int back = mv.set & ~mask;
        if (back) out.push_back("return " + names(back, n));
        if (mv.deodorized >= 0) out.push_back("dearomatize " + std::to_string(mv.deodorized + 1));
        if (mv.perfumed >= 0) out.push_back("aromatize " + std::to_string(mv.perfumed + 1));
        out.push_back("take " + names(mv.set, n));
        used |= mv.kind;
        mask &= ~mv.set;
    }
    printf("%d\n", (int)out.size());
    for (const auto &line : out) printf("%s\n", line.c_str());
}
