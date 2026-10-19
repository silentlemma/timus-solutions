#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<int> area(n), low(n), high(n);
    for (int& a : area) scanf("%d", &a);
    for (int i = 0; i < n; i++) scanf("%d %d", &low[i], &high[i]);
    vector<int> order(n), by_low(n);
    for (int i = 0; i < n; i++) order[i] = by_low[i] = i;
    sort(order.begin(), order.end(), [&](int a, int b) { return area[a] < area[b]; });
    sort(by_low.begin(), by_low.end(), [&](int a, int b) { return low[a] < low[b]; });
    vector<int> sizes(n);
    for (int i = 0; i < n; i++) sizes[i] = area[order[i]];
    // rooms from the smallest up, each to the waiting team whose largest
    // area is the smallest
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> waiting;
    vector<int> team(n);
    int at = 0;
    for (int place = 0; place < n; place++) {
        while (at < n && low[by_low[at]] <= sizes[place]) {
            waiting.push({high[by_low[at]], by_low[at]});
            at++;
        }
        if (waiting.empty() || waiting.top().first < sizes[place]) {
            puts("Let's search for another office.");
            return 0;
        }
        team[place] = waiting.top().second;
        waiting.pop();
    }
    // the team in room place takes rooms first[place] .. last[place] in
    // sorted order; another seating exists exactly when two teams could swap
    vector<int> first(n), last(n);
    for (int p = 0; p < n; p++) {
        int t = team[p];
        first[p] = lower_bound(sizes.begin(), sizes.end(), low[t]) - sizes.begin();
        last[p] = upper_bound(sizes.begin(), sizes.end(), high[t]) - sizes.begin() - 1;
    }
    for (int q = 1; q < n; q++) {
        for (int p = first[q]; p < q; p++) {
            if (last[p] >= q) {
                puts("Ask Shiftman for help.");
                return 0;
            }
        }
    }
    vector<int> room(n);
    for (int p = 0; p < n; p++) room[team[p]] = order[p] + 1;
    puts("Perfect!");
    for (int i = 0; i < n; i++) printf("%d%c", room[i], i + 1 < n ? ' ' : '\n');
    return 0;
}
