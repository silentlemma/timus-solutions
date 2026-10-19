#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

constexpr int KINDS = 8;   // cocktails as masks of three juices; 0 is unused
constexpr int INF = 1 << 30;
constexpr int WORD = 4;    // up to three letters and the terminating zero
const char* JUICES = "ABP";

int main() {
    int n;
    scanf("%d", &n);
    vector<int> glasses[KINDS];
    char s[WORD];
    for (int i = 1; i <= n; i++) {
        scanf("%s", s);
        int mask = 0;
        for (char* c = s; *c; c++) mask |= 1 << (strchr(JUICES, *c) - JUICES);
        glasses[mask].push_back(i);
    }
    // equal cocktails stand together; the cocktails present are ordered by a DP over
    // subsets, where best[used][last] counts the pourings, and a juice needs a new pouring
    // when a cocktail contains it and the previous one does not
    int present = 0;
    for (int k = 1; k < KINDS; k++)
        if (!glasses[k].empty()) present |= 1 << k;
    static int best[1 << KINDS][KINDS], from[1 << KINDS][KINDS];
    for (auto& row : best)
        for (int& x : row) x = INF;
    for (int k = 1; k < KINDS; k++)
        if (present >> k & 1) best[1 << k][k] = __builtin_popcount(k), from[1 << k][k] = 0;
    for (int used = 0; used < 1 << KINDS; used++)
        for (int last = 1; last < KINDS; last++) {
            if (best[used][last] == INF) continue;
            for (int k = 1; k < KINDS; k++) {
                if (!(present >> k & 1) || used >> k & 1) continue;
                int cost = best[used][last] + __builtin_popcount(k & ~last);
                int next = used | 1 << k;
                if (cost < best[next][k]) best[next][k] = cost, from[next][k] = last;
            }
        }
    int last = 1;
    for (int k = 1; k < KINDS; k++)
        if (best[present][k] < best[present][last]) last = k;
    printf("%d\n", best[present][last]);
    vector<int> order;
    for (int used = present; last != 0;) {
        order.push_back(last);
        int prev = from[used][last];
        used ^= 1 << last;
        last = prev;
    }
    bool first = true;
    for (int i = (int)order.size() - 1; i >= 0; i--)
        for (int g : glasses[order[i]]) printf(first ? "%d" : " %d", g), first = false;
    printf("\n");
}
