#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

constexpr int GROUPS = 4;  // both courses, only the first, only the second, neither

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> column(m, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &column[j][i]);
    int best = n + 1, bestA = 0, bestB = 0;
    // every pair of courses is tried: the four groups of a pair are counted
    // in one pass over the programs
    for (int a = 0; a < m; a++)
        for (int b = a + 1; b < m; b++) {
            int count[GROUPS] = {};
            for (int i = 0; i < n; i++) count[2 * column[a][i] + column[b][i]]++;
            int worst = *max_element(count, count + GROUPS);
            if (worst < best) best = worst, bestA = a + 1, bestB = b + 1;
        }
    printf("%d\n%d %d\n", best, bestA, bestB);
}
