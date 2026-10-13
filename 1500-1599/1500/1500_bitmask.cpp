#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int HALF = 10; // categories are split into a low and a high half of the mask

int k, n, m, lowSize;
vector<vector<int>> low, high; // neighbours of a crossing under half a set

// whether the roads of the categories in s lead from crossing 0 to 1
bool connects(int s) {
    int lo = s & ((1 << lowSize) - 1), hi = s >> lowSize;
    int reach = 1, todo = 1;
    while (todo) {
        int u = __builtin_ctz(todo);
        todo &= todo - 1;
        int fresh = (low[u][lo] | high[u][hi]) & ~reach;
        reach |= fresh;
        todo |= fresh;
        if (reach & 2)
            return true;
    }
    return false;
}

int main() {
    scanf("%d %d %d", &k, &n, &m);
    // byCategory[u][c]: the crossings next to u along roads of category c
    vector<vector<int>> byCategory(n, vector<int>(k, 0));
    for (int i = 0; i < m; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        byCategory[a][c] |= 1 << b;
        byCategory[b][c] |= 1 << a;
    }
    lowSize = min(k, HALF);
    int highSize = k - lowSize;
    low.assign(n, vector<int>(1 << lowSize, 0));
    high.assign(n, vector<int>(1 << highSize, 0));
    for (int u = 0; u < n; u++) {
        for (int s = 1; s < (1 << lowSize); s++)
            low[u][s] = low[u][s & (s - 1)] | byCategory[u][__builtin_ctz(s)];
        for (int s = 1; s < (1 << highSize); s++)
            high[u][s] = high[u][s & (s - 1)] | byCategory[u][lowSize + __builtin_ctz(s)];
    }
    // fewer permits first
    for (int size = 1; size <= k; size++)
        for (int s = 0; s < (1 << k); s++)
            if (__builtin_popcount(s) == size && connects(s)) {
                printf("%d\n", size);
                for (int c = 0, first = 1; c < k; c++)
                    if (s >> c & 1) {
                        printf(first ? "%d" : " %d", c);
                        first = 0;
                    }
                printf("\n");
                return 0;
            }
}
