#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

const int STEP = 10; // every tenth person is fined
const int INF = 1 << 30;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 0;
    vector<char> buf(n + 1);
    if (scanf("%s", buf.data()) != 1)
        return 0;
    string good(buf.data());
    // cost[i][j] holds the least fines once i conductors and j friends stand
    // in line, and the next person then stands at place i + j + 1
    vector<vector<int>> cost(n + 1, vector<int>(k + 1, INF));
    cost[0][0] = 0;
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= k; j++) {
            int here = cost[i][j];
            if (here == INF)
                continue;
            int fined = (i + j + 1) % STEP == 0;
            if (j < k)
                cost[i][j + 1] = min(cost[i][j + 1], here + fined); // a friend steps in
            if (i < n)
                cost[i + 1][j] = min(cost[i + 1][j], here + (fined && good[i] == '1'));
        }
    int j = min_element(cost[n].begin(), cost[n].end()) - cost[n].begin();
    int best = cost[n][j];
    // walk back: a friend was added wherever the cost came from the left
    vector<int> places;
    for (int i = n; i > 0 || j > 0;) {
        int fined = (i + j) % STEP == 0;
        if (i > 0 && cost[i - 1][j] + (fined && good[i - 1] == '1') == cost[i][j])
            i--;
        else {
            places.push_back(i + j);
            j--;
        }
    }
    reverse(places.begin(), places.end());
    printf("%d\n%d", best, (int)places.size());
    for (int p : places)
        printf(" %d", p);
    printf("\n");
}
