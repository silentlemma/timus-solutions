#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

const int WORD = 64;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    std::unordered_map<long long, int> cheapest;
    for (int i = 0; i < k; i++) {
        int x, y, c;
        if (scanf("%d %d %d", &x, &y, &c) != 2 + 1) return 0;
        long long key = (long long)(x - 1) * n + (y - 1);
        auto it = cheapest.find(key);
        if (it == cheapest.end() || c < it->second) cheapest[key] = c;
    }
    // the edges sorted by cost; the first m of them are those of cost up to
    // the m-th cost
    std::vector<std::tuple<int, int, int>> edges;
    for (auto [key, c] : cheapest) edges.push_back({c, (int)(key / n), (int)(key % n)});
    std::sort(edges.begin(), edges.end());
    int words = (n + WORD - 1) / WORD, total = edges.size();
    // reach[x]: the targets x pays for, as a bit set
    std::vector<std::vector<uint64_t>> reach(n, std::vector<uint64_t>(words, 0));
    std::vector<int> size(n, 0);
    std::vector<std::vector<std::pair<int, int>>> into(n);  // (edge index, operator)
    for (int i = 0; i < total; i++) {
        auto [c, x, y] = edges[i];
        into[y].push_back({i, x});
    }
    // the target with the fewest ways in comes first when picking a witness
    std::vector<int> rare(n);
    for (int y = 0; y < n; y++) rare[y] = y;
    std::sort(rare.begin(), rare.end(),
              [&](int a, int b) { return into[a].size() < into[b].size(); });
    std::vector<uint64_t> full(words, ~0ULL), missing(words);
    if (n % WORD) full[words - 1] = (1ULL << (n % WORD)) - 1;
    int half = (n + 1) / 2;

    auto feasible = [&](int m) {
        for (int a = 0; a < n; a++) {
            // one operator of a covering pair pays for at least half
            if (size[a] < half) continue;
            bool any = false;
            for (int w = 0; w < words; w++) {
                missing[w] = full[w] ^ reach[a][w];
                any = any || missing[w];
            }
            if (!any) return true;
            int t = 0;
            for (int y : rare) {
                if (missing[y / WORD] >> (y % WORD) & 1) {
                    t = y;
                    break;
                }
            }
            for (auto [i, b] : into[t]) {
                if (i >= m) continue;
                bool covers = true;
                for (int w = 0; w < words && covers; w++) {
                    covers = (reach[b][w] & missing[w]) == missing[w];
                }
                if (covers) return true;
            }
        }
        return false;
    };
    // take the edges between two prefixes in or out
    int now = 0;
    auto move = [&](int to) {
        for (; now < to; now++) {
            auto [c, x, y] = edges[now];
            reach[x][y / WORD] ^= 1ULL << (y % WORD);
            size[x]++;
        }
        for (; now > to; now--) {
            auto [c, x, y] = edges[now - 1];
            reach[x][y / WORD] ^= 1ULL << (y % WORD);
            size[x]--;
        }
    };
    move(total);
    if (total == 0 || !feasible(total)) {
        puts("No solution");
        return 0;
    }
    int lo = 1, hi = total;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        move(mid);
        if (feasible(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    printf("%d\n", std::get<0>(edges[lo - 1]));
    return 0;
}
