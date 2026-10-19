#include <algorithm>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>

struct Edge {
    int weight, first, second, id;
    bool operator<(const Edge &other) const {
        return std::tie(weight, first, second, id) <
               std::tie(other.weight, other.first, other.second, other.id);
    }
};

class DisjointSet {
    std::vector<int> parent;

  public:
    explicit DisjointSet(int size) : parent(size, -1) {}
    int root(int vertex) {
        while (parent[vertex] >= 0) {
            if (parent[parent[vertex]] >= 0)
                parent[vertex] = parent[parent[vertex]];
            vertex = parent[vertex];
        }
        return vertex;
    }
    bool unite(int first, int second) {
        first = root(first);
        second = root(second);
        if (first == second)
            return false;
        if (parent[first] > parent[second])
            std::swap(first, second);
        parent[first] += parent[second];
        parent[second] = first;
        return true;
    }
};

class LinkCut {
    std::vector<int> left, right, parent, minimum, key, ancestors;
    std::vector<bool> reverse;
    bool auxiliary_root(int vertex) const {
        int ancestor = parent[vertex];
        return !ancestor || (left[ancestor] != vertex && right[ancestor] != vertex);
    }
    void pull(int vertex) {
        int best = vertex;
        for (int child : {left[vertex], right[vertex]}) {
            if (key[minimum[child]] < key[best])
                best = minimum[child];
        }
        minimum[vertex] = best;
    }
    void toggle(int vertex) {
        if (vertex) {
            std::swap(left[vertex], right[vertex]);
            reverse[vertex] = !reverse[vertex];
        }
    }
    void rotate(int vertex) {
        int ancestor = parent[vertex], grandparent = parent[ancestor], child;
        if (left[ancestor] == vertex) {
            child = right[vertex];
            left[ancestor] = child;
            right[vertex] = ancestor;
        } else {
            child = left[vertex];
            right[ancestor] = child;
            left[vertex] = ancestor;
        }
        if (child)
            parent[child] = ancestor;
        if (grandparent) {
            if (left[grandparent] == ancestor)
                left[grandparent] = vertex;
            else if (right[grandparent] == ancestor)
                right[grandparent] = vertex;
        }
        parent[vertex] = grandparent;
        parent[ancestor] = vertex;
        pull(ancestor);
        pull(vertex);
    }
    void splay(int vertex) {
        ancestors.clear();
        int node = vertex;
        ancestors.push_back(node);
        while (!auxiliary_root(node)) {
            node = parent[node];
            ancestors.push_back(node);
        }
        for (auto it = ancestors.rbegin(); it != ancestors.rend(); ++it) {
            node = *it;
            if (reverse[node]) {
                toggle(left[node]);
                toggle(right[node]);
                reverse[node] = false;
            }
        }
        while (!auxiliary_root(vertex)) {
            int ancestor = parent[vertex], grandparent = parent[ancestor];
            if (!auxiliary_root(ancestor)) {
                bool aligned = (left[grandparent] == ancestor) == (left[ancestor] == vertex);
                rotate(aligned ? ancestor : vertex);
            }
            rotate(vertex);
        }
    }
    void access(int vertex) {
        int last = 0;
        for (int node = vertex; node; node = parent[node]) {
            splay(node);
            right[node] = last;
            if (last)
                parent[last] = node;
            pull(node);
            last = node;
        }
        splay(vertex);
    }
    void make_root(int vertex) {
        access(vertex);
        toggle(vertex);
    }

  public:
    LinkCut(int vertices, int edges)
        : left(2 * vertices), right(2 * vertices), parent(2 * vertices), minimum(2 * vertices),
          key(2 * vertices, edges + 1), reverse(2 * vertices) {
        std::iota(minimum.begin(), minimum.end(), 0);
    }
    void add(int first, int second, int node, int rank) {
        key[node] = rank;
        make_root(first);
        parent[first] = node;
        make_root(second);
        parent[second] = node;
    }
    int replace_minimum(int first, int second, int rank) {
        make_root(first);
        access(second);
        int edge = minimum[second];
        splay(edge);
        int old = key[edge];
        toggle(left[edge]);
        toggle(right[edge]);
        key[edge] = rank;
        pull(edge);
        return old;
    }
};

std::vector<int> solve(int vertices, const std::vector<Edge> &edges) {
    LinkCut forest(vertices, static_cast<int>(edges.size()));
    DisjointSet components(vertices);
    std::vector<bool> active(edges.size());
    int count = 0, lower = 0, best_left = 0, best_right = 0, best_width = -1;
    for (int rank = 0; rank < static_cast<int>(edges.size()); ++rank) {
        const auto &edge = edges[rank];
        if (components.unite(edge.first, edge.second)) {
            ++count;
            forest.add(edge.first + 1, edge.second + 1, vertices + count, rank);
        } else {
            active[forest.replace_minimum(edge.first + 1, edge.second + 1, rank)] = false;
        }
        active[rank] = true;
        while (!active[lower])
            ++lower;
        if (count == vertices - 1) {
            int width = edge.weight - edges[lower].weight;
            if (best_width < 0 || width < best_width) {
                best_width = width;
                best_left = lower;
                best_right = rank;
            }
            if (!best_width)
                break;
        }
    }
    DisjointSet output_components(vertices);
    std::vector<int> chosen;
    for (int rank = best_left; rank <= best_right; ++rank) {
        const auto &edge = edges[rank];
        if (output_components.unite(edge.first, edge.second)) {
            chosen.push_back(edge.id);
            if (static_cast<int>(chosen.size()) == vertices - 1)
                break;
        }
    }
    return chosen;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int vertices, count;
    std::cin >> vertices >> count;
    std::vector<Edge> edges(count);
    for (int i = 0; i < count; ++i) {
        auto &edge = edges[i];
        std::cin >> edge.first >> edge.second >> edge.weight;
        --edge.first;
        --edge.second;
        edge.id = i + 1;
    }
    std::sort(edges.begin(), edges.end());
    const auto chosen = solve(vertices, edges);
    for (int i = 0; i < static_cast<int>(chosen.size()); ++i) {
        if (i)
            std::cout << ' ';
        std::cout << chosen[i];
    }
    std::cout << '\n';
}
