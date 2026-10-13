#include <cstdio>
#include <queue>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n, m, k, price;
    scanf("%d %d %d %d", &n, &m, &k, &price);
    vector<vector<int>> starts(n + 1);
    vector<int> finish(k + 1), ends(n + 1, 0);
    for (int i = 1; i <= k; i++) {
        int s;
        scanf("%d %d", &s, &finish[i]);
        starts[s].push_back(i);
    }
    vector<bool> taken(k + 1, false);
    priority_queue<pair<int, int>> onBoard; // riders by the farthest stop first
    int riding = 0;
    for (int stop = 1; stop <= n; stop++) {
        riding -= ends[stop];
        for (int i : starts[stop]) {
            taken[i] = true;
            onBoard.push({finish[i], i});
            ends[finish[i]]++;
            riding++;
        }
        // too many: drop whoever would ride the longest
        while (riding > m) {
            int i = onBoard.top().second;
            onBoard.pop();
            taken[i] = false;
            ends[finish[i]]--;
            riding--;
        }
    }
    string list;
    int count = 0;
    for (int i = 1; i <= k; i++)
        if (taken[i]) {
            list += (count++ ? " " : "") + to_string(i);
        }
    printf("%lld\n%s\n", (long long)count * price, list.c_str());
}
