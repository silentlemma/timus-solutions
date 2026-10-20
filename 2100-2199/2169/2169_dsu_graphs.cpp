#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

constexpr int MAX_INCOMING = 3;
constexpr int MAX_DEGREE = MAX_INCOMING + 1;
constexpr std::int64_t MODULUS = 1000000007;

class DisjointSet {
  public:
    explicit DisjointSet(int count) : parent(count, -1), edges(count, 0) {}

    int find(int vertex) {
        int root = vertex;
        while (parent[root] >= 0) {
            root = parent[root];
        }
        while (vertex != root) {
            int next = parent[vertex];
            parent[vertex] = root;
            vertex = next;
        }
        return root;
    }

    void add_edge(int first, int second) {
        first = find(first);
        second = find(second);
        if (first == second) {
            ++edges[first];
            return;
        }
        if (parent[first] > parent[second]) {
            std::swap(first, second);
        }
        parent[first] += parent[second];
        parent[second] = first;
        edges[first] += edges[second] + 1;
    }

    std::vector<int> parent;
    std::vector<int> edges;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int vertex_count, edge_count;
    if (!(std::cin >> vertex_count >> edge_count)) {
        return 0;
    }
    DisjointSet components(vertex_count);
    std::vector<int> degree(vertex_count, 0);
    bool possible = true;
    for (int edge = 0; edge < edge_count; ++edge) {
        int first, second;
        std::cin >> first >> second;
        --first;
        --second;
        ++degree[first];
        ++degree[second];
        if (degree[first] > MAX_DEGREE || degree[second] > MAX_DEGREE) {
            possible = false;
        }
        components.add_edge(first, second);
    }

    std::vector<int> sinks(vertex_count, 0);
    for (int vertex = 0; vertex < vertex_count; ++vertex) {
        if (degree[vertex] <= MAX_INCOMING) {
            ++sinks[components.find(vertex)];
        }
    }

    std::int64_t answer = possible ? 1 : 0;
    for (int root = 0; root < vertex_count; ++root) {
        if (components.parent[root] >= 0) {
            continue;
        }
        int vertices = -components.parent[root];
        int edges = components.edges[root];
        if (edges == vertices - 1) {
            // A tree has one orientation for each permitted sink.
            answer = answer * sinks[root] % MODULUS;
        } else if (edges == vertices) {
            // The unique cycle can be directed either way.
            answer = answer * 2 % MODULUS;
        } else {
            answer = 0;
        }
    }
    std::cout << answer << '\n';
    return 0;
}
