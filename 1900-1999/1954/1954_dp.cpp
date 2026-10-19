#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

constexpr int ALPHABET = 26;
constexpr int TARGET = 5;
constexpr int INF = TARGET + 1;
constexpr int OUTER_SPLIT = 3;
struct Node {
    std::array<int, ALPHABET> next{};
    int length = 0, link = 0, diff = 0, series = 0;
    std::array<int, 2> best{{INF, INF}}, start{};
};

int main() {
    std::string text;
    std::cin >> text;
    int n = static_cast<int>(text.size());
    std::string data = " " + text;
    std::vector<Node> tree(n + 2);
    tree[0].length = -1;
    std::vector<std::array<int, 2>> best(n + 1, {{INF, INF}}), parent(n + 1);
    best[0][0] = 0;
    int count = 2, last = 1;
    for (int i = 1; i <= n; ++i) {
        int code = data[i] - 'a', current = last;
        while (data[i - tree[current].length - 1] != data[i])
            current = tree[current].link;
        int following = tree[current].next[code];
        if (following == 0) {
            following = count++;
            tree[current].next[code] = following;
            Node &node = tree[following];
            node.length = tree[current].length + 2;
            if (node.length == 1)
                node.link = 1;
            else {
                int suffix = tree[current].link;
                while (data[i - tree[suffix].length - 1] != data[i])
                    suffix = tree[suffix].link;
                node.link = tree[suffix].next[code];
            }
            node.diff = node.length - tree[node.link].length;
            node.series = node.diff == tree[node.link].diff ? tree[node.link].series : node.link;
        }
        last = following;
        for (int v = last; tree[v].length > 0; v = tree[v].series) {
            Node &node = tree[v];
            int base = i - tree[node.series].length - node.diff;
            for (int p = 0; p < 2; ++p) {
                node.best[p] = best[base][p];
                node.start[p] = base;
                if (node.diff == tree[node.link].diff && tree[node.link].best[p] < node.best[p]) {
                    node.best[p] = tree[node.link].best[p];
                    node.start[p] = tree[node.link].start[p];
                }
                if (node.best[p] + 1 < best[i][p ^ 1]) {
                    best[i][p ^ 1] = node.best[p] + 1;
                    parent[i][p ^ 1] = node.start[p];
                }
            }
        }
    }
    if (best[n][1] > TARGET) {
        std::cout << "NO\n";
        return 0;
    }
    std::vector<std::string> result;
    for (int i = n, parity = 1; i > 0; parity ^= 1) {
        int before = parent[i][parity];
        result.push_back(text.substr(before, i - before));
        i = before;
    }
    std::reverse(result.begin(), result.end());
    while (static_cast<int>(result.size()) < TARGET) {
        auto it = std::find_if(result.begin(), result.end(),
                               [](const std::string &part) { return part.size() >= OUTER_SPLIT; });
        if (it != result.end()) {
            auto offset = it - result.begin();
            std::string part = *it;
            result.erase(it);
            result.insert(
                result.begin() + offset,
                {part.substr(0, 1), part.substr(1, part.size() - 2), part.substr(part.size() - 1)});
        } else {
            int remaining = 2;
            for (int j = static_cast<int>(result.size()) - 1; j >= 0 && remaining; --j) {
                if (result[j].size() == 2) {
                    std::string part = result[j];
                    result[j] = part.substr(0, 1);
                    result.insert(result.begin() + j + 1, part.substr(1));
                    --remaining;
                }
            }
        }
    }
    std::cout << "YES\n";
    for (const auto &part : result)
        std::cout << part << '\n';
}
