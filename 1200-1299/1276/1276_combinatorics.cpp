#include <cstdio>
#include <cstring>

const int MAXC = 64; // binomials needed only up to 41
const int WORD = 3;  // two couplings and the closing zero
long long binom[MAXC][MAXC];

// ways to put identical items into runs in order, runs may stay empty
long long spread(int items, int runs) {
    if (runs == 0)
        return items == 0;
    return binom[items + runs - 1][runs - 1];
}

int main() {
    for (int i = 0; i < MAXC; i++) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; j++)
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
    }
    int n, k;
    char loco[WORD], car[WORD];
    scanf("%d %d %2s", &n, &k, loco);
    int have[2][2] = {}; // have[x][y]: carriages with couplings x, y (0 = A)
    for (int i = 0; i < n; i++) {
        scanf("%2s", car);
        have[car[0] == 'B'][car[1] == 'B']++;
    }
    // the train starts with the coupling that fits the locomotive's right
    // end and finishes with the one that fits its left end
    int start = loco[1] == 'B', end = loco[0] == 'B';
    long long total = 0;
    for (int sw = 0; sw <= k; sw++) {
        // AB and BA carriages must alternate, beginning with the one that
        // leaves the starting coupling
        if ((sw + 1) / 2 > have[start][!start] || sw / 2 > have[!start][start])
            continue;
        if ((sw % 2 == 0 ? start : !start) != end)
            continue;
        // the runs between switches hold the AA and BB carriages
        int runs[2];
        runs[start] = sw / 2 + 1, runs[!start] = (sw + 1) / 2;
        for (int aa = 0; aa <= k - sw; aa++) {
            int bb = k - sw - aa;
            if (aa <= have[0][0] && bb <= have[1][1])
                total += spread(aa, runs[0]) * spread(bb, runs[1]);
        }
    }
    if (total)
        printf("YES\n%lld\n", total);
    else
        printf("NO\n");
}
