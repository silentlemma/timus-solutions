#include <cstdio>
#include <set>
#include <utility>
#include <vector>
using namespace std;

int main() {
    int n, k, m;
    if (scanf("%d %d", &n, &k) != 2 || scanf("%d", &m) != 1)
        return 0;
    // rooms in turn: every room gets someone, and the split is as even as
    // possible, which leaves the most pairs from different rooms
    vector<int> room(n);
    for (int i = 0; i < n; i++)
        room[i] = i % k;
    // neighbours in this order always have different rooms
    vector<pair<int, int>> days;
    for (int i = 0; i + 1 < n; i += 2)
        days.push_back({i, i + 1});
    if (n % 2)
        days.push_back({0, n - 1});
    if (n % 2 && room[n - 1] == room[0])
        days.back() = {1, n - 1};
    set<pair<int, int>> used(days.begin(), days.end());
    for (int i = 0; i < n && (int)days.size() < m; i++)
        for (int j = i + 1; j < n && (int)days.size() < m; j++)
            if (room[i] != room[j] && !used.count({i, j}))
                days.push_back({i, j});
    for (int i = 0; i < n; i++)
        printf("%d\n", room[i] + 1);
    for (int d = 0; d < m; d++)
        printf("%d %d\n", days[d].first + 1, days[d].second + 1);
}
