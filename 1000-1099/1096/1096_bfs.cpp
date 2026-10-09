#include <cstdio>
#include <map>
#include <queue>
#include <tuple>
#include <vector>

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    std::vector<int> route(k), back(k);
    std::map<int, std::vector<int>> by_route;
    for (int j = 0; j < k; j++) {
        scanf("%d %d", &route[j], &back[j]);
        by_route[route[j]].push_back(j);
    }
    int t, s1, s2;
    scanf("%d %d %d", &t, &s1, &s2);
    // a state is the plate in hand: the first one, or the plate of bus j; a
    // driver swaps when the plate in hand shows the route of his bus
    std::vector<int> came(k, -1);
    std::queue<std::tuple<int, int, int>> queue;
    queue.push({s1, s2, -1});
    while (!queue.empty()) {
        auto [x, y, j] = queue.front();
        queue.pop();
        for (int r : {x, y}) {
            auto it = by_route.find(r);
            if (it == by_route.end())
                continue;
            std::vector<int> buses = it->second;
            by_route.erase(it);
            for (int i : buses) {
                came[i] = j;
                if (route[i] == t || back[i] == t) {
                    std::vector<int> path;
                    for (; i >= 0; i = came[i])
                        path.push_back(i + 1);
                    printf("%d\n", (int)path.size());
                    for (size_t p = path.size(); p-- > 0;)
                        printf("%d\n", path[p]);
                    return 0;
                }
                queue.push({route[i], back[i], i});
            }
        }
    }
    puts("IMPOSSIBLE");
}
