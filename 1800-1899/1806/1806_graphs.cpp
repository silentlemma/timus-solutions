#include <cstdio>
#include <functional>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

const int DIGITS = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<long long> cost(DIGITS), place(DIGITS);
    for (auto &c : cost) scanf("%lld", &c);
    place[DIGITS - 1] = 1;
    for (int p = DIGITS - 2; p >= 0; p--) place[p] = place[p + 1] * DIGITS;
    std::vector<long long> number(n);
    std::unordered_map<long long, int> index;
    index.reserve(2 * n);
    char buffer[DIGITS + 2];
    for (int i = 0; i < n; i++) {
        scanf("%s", buffer);
        number[i] = std::stoll(buffer);
        index[number[i]] = i;
    }
    const long long none = -1;
    std::vector<long long> best(n, none);
    std::vector<int> before(n, -1);
    std::priority_queue<std::pair<long long, int>, std::vector<std::pair<long long, int>>,
                        std::greater<>>
        heap;
    best[0] = 0;
    heap.push({0, 0});
    auto relax = [&](long long value, long long time, int from) {
        auto it = index.find(value);
        if (it == index.end()) return;
        int v = it->second;
        if (best[v] == none || time < best[v]) {
            best[v] = time;
            before[v] = from;
            heap.push({time, v});
        }
    };
    while (!heap.empty()) {
        auto [d, u] = heap.top();
        heap.pop();
        if (d > best[u]) continue;
        if (u == n - 1) break;
        long long value = number[u];
        int digit[DIGITS];
        for (int p = 0; p < DIGITS; p++) digit[p] = value / place[p] % DIGITS;
        // neighbours with the first change at digit p share a prefix of p
        for (int p = 0; p < DIGITS; p++) {
            long long low = value - digit[p] * place[p];
            for (int other = 0; other < DIGITS; other++) {
                if (other != digit[p]) relax(low + other * place[p], d + cost[p], u);
            }
            for (int q = p + 1; q < DIGITS; q++) {
                if (digit[q] != digit[p]) {
                    relax(value + (digit[q] - digit[p]) * (place[p] - place[q]), d + cost[p], u);
                }
            }
        }
    }
    if (best[n - 1] == none) {
        puts("-1");
        return 0;
    }
    std::vector<int> path = {n - 1};
    while (path.back() != 0) path.push_back(before[path.back()]);
    printf("%lld\n%d\n", best[n - 1], (int)path.size());
    for (size_t i = path.size(); i-- > 0;) printf("%d%c", path[i] + 1, i ? ' ' : '\n');
    return 0;
}
