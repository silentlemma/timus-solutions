#include <iostream>
#include <utility>
#include <vector>

constexpr long long MODULUS = 1000000007;

class Network {
    std::vector<long long> direct, broadcast;
    std::vector<int> parent;
    int root;

  public:
    Network(const std::vector<long long> &initial, const std::vector<std::pair<int, int>> &edges,
            int start = 0)
        : direct(initial), broadcast(initial.size()), parent(initial.size(), -1), root(start) {
        std::vector<std::vector<int>> neighbors(initial.size());
        for (auto edge : edges) {
            neighbors[edge.first].push_back(edge.second);
            neighbors[edge.second].push_back(edge.first);
        }
        std::vector<int> order{root};
        parent[root] = root;
        for (std::size_t at = 0; at < order.size(); ++at) {
            int vertex = order[at];
            for (int next : neighbors[vertex]) {
                if (parent[next] == -1) {
                    parent[next] = vertex;
                    order.push_back(next);
                }
            }
        }
    }

    long long process(int kind, int vertex) {
        long long value = direct[vertex];
        if (vertex != root) {
            value += broadcast[parent[vertex]];
            if (value >= MODULUS)
                value -= MODULUS;
        }
        if (kind == 2)
            return value;
        broadcast[vertex] += value;
        if (broadcast[vertex] >= MODULUS)
            broadcast[vertex] -= MODULUS;
        if (vertex != root) {
            long long &above = direct[parent[vertex]];
            above += value;
            if (above >= MODULUS)
                above -= MODULUS;
        }
        return -1;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    if (!(std::cin >> size))
        return 0;
    std::vector<long long> initial(size);
    for (auto &value : initial)
        std::cin >> value;
    std::vector<std::pair<int, int>> edges;
    edges.reserve(size - 1);
    for (int i = 1; i < size; ++i) {
        int a, b;
        std::cin >> a >> b;
        edges.emplace_back(a - 1, b - 1);
    }
    Network network(initial, edges);
    int count;
    std::cin >> count;
    while (count--) {
        int kind, vertex;
        std::cin >> kind >> vertex;
        long long answer = network.process(kind, vertex - 1);
        if (answer >= 0)
            std::cout << answer << '\n';
    }
}
