#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> deadline(n), reward(n), orders(n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &deadline[i], &reward[i]);
        orders[i] = i;
    }
    sort(orders.begin(), orders.end(), [&](int a, int b) { return deadline[a] < deadline[b]; });
    // by deadline: keep the best orders that fit, dropping the cheapest when
    // there are more orders than days so far
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> kept;
    for (int i : orders) {
        kept.push({reward[i], i});
        if ((int)kept.size() > deadline[i])
            kept.pop();
    }
    vector<int> chosen;
    for (; !kept.empty(); kept.pop())
        chosen.push_back(kept.top().second);
    sort(chosen.begin(), chosen.end(), [&](int a, int b) { return deadline[a] < deadline[b]; });
    printf("%d\n", (int)chosen.size());
    for (size_t k = 0; k < chosen.size(); k++)
        printf(k + 1 < chosen.size() ? "%d " : "%d", chosen[k] + 1);
    printf("\n");
}
