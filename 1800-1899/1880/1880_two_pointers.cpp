#include <cstdio>
#include <vector>

using namespace std;

const int PLAYERS = 3;

int main() {
    vector<vector<int>> own(PLAYERS);
    for (auto& list : own) {
        int n;
        if (scanf("%d", &n) != 1) return 0;
        list.resize(n);
        for (int& v : list) scanf("%d", &v);
    }
    // walk the three sorted lists together, always moving past the
    // smallest current number
    size_t at[PLAYERS] = {0};
    int common = 0;
    while (true) {
        bool done = false;
        for (int p = 0; p < PLAYERS; p++) done = done || at[p] == own[p].size();
        if (done) break;
        int low = own[0][at[0]], high = low;
        for (int p = 1; p < PLAYERS; p++) {
            int v = own[p][at[p]];
            low = v < low ? v : low;
            high = v > high ? v : high;
        }
        if (low == high) common++;
        for (int p = 0; p < PLAYERS; p++)
            if (own[p][at[p]] == low) at[p]++;
    }
    printf("%d\n", common);
    return 0;
}
