#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <utility>
#include <vector>

constexpr int END_OF_INPUT = -1;

struct Statement {
    int left, right;
    bool odd;
};

class Sets {
    std::vector<std::uint16_t> link;
    std::vector<unsigned char> rank;

  public:
    explicit Sets(int count) : link(count), rank(count) {
        for (int i = 0; i < count; ++i)
            link[i] = i << 1;
    }

    std::pair<int, int> find(int node) {
        const int parent = link[node] >> 1;
        if (parent == node)
            return {node, 0};
        const auto [root, parity] = find(parent);
        const int from_node = parity ^ (link[node] & 1);
        link[node] = (root << 1) | from_node;
        return {root, from_node};
    }

    bool unite(int a, int b, bool odd) {
        auto [root_a, parity_a] = find(a);
        auto [root_b, parity_b] = find(b);
        const int required = parity_a ^ parity_b ^ odd;
        if (root_a == root_b)
            return required == 0;
        if (rank[root_a] < rank[root_b])
            std::swap(root_a, root_b);
        link[root_b] = (root_a << 1) | required;
        if (rank[root_a] == rank[root_b])
            ++rank[root_a];
        return true;
    }
};

int main() {
    int length;
    while (std::scanf("%d", &length) == 1 && length != END_OF_INPUT) {
        int size;
        if (std::scanf("%d", &size) != 1)
            return 0;
        std::vector<Statement> statements;
        statements.reserve(size);
        std::vector<int> points;
        points.reserve(2 * size);
        for (int i = 0; i < size; ++i) {
            int left, right;
            char word[] = "even";
            std::scanf("%d%d%4s", &left, &right, word);
            statements.push_back({left - 1, right, word[0] == 'o'});
            points.push_back(left - 1);
            points.push_back(right);
        }
        std::sort(points.begin(), points.end());
        points.erase(std::unique(points.begin(), points.end()), points.end());
        Sets sets(static_cast<int>(points.size()));
        const auto id = [&](int point) {
            return static_cast<int>(std::lower_bound(points.begin(), points.end(), point) -
                                    points.begin());
        };
        int answer = 0;
        while (answer < size) {
            const auto &[left, right, odd] = statements[answer];
            if (!sets.unite(id(left), id(right), odd))
                break;
            ++answer;
        }
        std::printf("%d\n", answer);
    }
}
