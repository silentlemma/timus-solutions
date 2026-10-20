#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m, k;
    std::cin >> n >> m >> k;
    std::vector<std::vector<int>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        std::cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    std::vector<long long> cups(k);
    for (auto &cup : cups) {
        std::cin >> cup;
    }
    std::sort(cups.begin(), cups.end(), std::greater<long long>());

    const int states = 2 * n;
    std::vector<int> distance(states, -1);
    std::vector<int> queue;
    queue.reserve(states);
    queue.push_back(0);
    distance[0] = 0;
    for (std::size_t head = 0; head < queue.size(); ++head) {
        int state = queue[head];
        int parity = (state & 1) ^ 1;
        for (int v : graph[state / 2]) {
            int next = 2 * v + parity;
            if (distance[next] == -1) {
                distance[next] = distance[state] + 1;
                queue.push_back(next);
            }
        }
    }

    std::vector<std::array<long long, 2>> suffix(k + 1, {-1, -1});
    for (int i = k - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1];
        suffix[i][cups[i] & 1] = cups[i];
    }

    std::vector<int> needed(states, -1);
    needed[0] = 0;
    std::array<int, 2> next_distance = {2, 1};
    std::array<long long, 2> smallest = {-1, -1};
    long long sum = 0;
    for (int count = 1; count <= k; ++count) {
        long long cup = cups[count - 1];
        sum += cup;
        smallest[cup & 1] = cup;
        std::array<long long, 2> best = {-1, -1};
        int parity = sum & 1;
        best[parity] = sum;
        // Changing the prefix parity needs only one exchange across its boundary.
        for (int removed = 0; removed < 2; ++removed) {
            long long added = suffix[count][removed ^ 1];
            if (smallest[removed] != -1 && added != -1) {
                best[parity ^ 1] = std::max(best[parity ^ 1], sum - smallest[removed] + added);
            }
        }
        for (int p = 0; p < 2; ++p) {
            while (next_distance[p] < states && next_distance[p] <= best[p]) {
                needed[next_distance[p]] = count;
                next_distance[p] += 2;
            }
        }
    }

    for (int v = 0; v < n; ++v) {
        int answer = -1;
        for (int parity = 0; parity < 2; ++parity) {
            int d = distance[2 * v + parity];
            if (d != -1 && needed[d] != -1 && (answer == -1 || needed[d] < answer)) {
                answer = needed[d];
            }
        }
        if (v != 0) {
            std::cout << ' ';
        }
        std::cout << answer;
    }
    std::cout << '\n';
}
