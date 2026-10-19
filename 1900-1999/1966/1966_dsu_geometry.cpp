#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

struct Point {
    std::int64_t x, y;
};

std::int64_t cross(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

bool between(std::int64_t value, std::int64_t a, std::int64_t b) {
    if (a > b)
        std::swap(a, b);
    return a <= value && value <= b;
}

bool overlap(std::int64_t a, std::int64_t b, std::int64_t c, std::int64_t d) {
    if (a > b)
        std::swap(a, b);
    if (c > d)
        std::swap(c, d);
    return a <= d && c <= b;
}

bool onSegment(Point point, Point a, Point b) {
    return cross(a, b, point) == 0 && between(point.x, a.x, b.x) && between(point.y, a.y, b.y);
}

bool straddles(std::int64_t first, std::int64_t second) {
    return (first <= 0 && second >= 0) || (second <= 0 && first >= 0);
}

bool intersects(Point a, Point b, Point c, Point d) {
    return overlap(a.x, b.x, c.x, d.x) && overlap(a.y, b.y, c.y, d.y) &&
           straddles(cross(a, b, c), cross(a, b, d)) && straddles(cross(c, d, a), cross(c, d, b));
}

class DisjointSets {
    std::vector<int> parent, weights;

  public:
    explicit DisjointSets(int size) : parent(size), weights(size, 1) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int vertex) {
        while (parent[vertex] != vertex) {
            parent[vertex] = parent[parent[vertex]];
            vertex = parent[vertex];
        }
        return vertex;
    }

    void unite(int first, int second) {
        first = find(first);
        second = find(second);
        if (first == second)
            return;
        if (weights[first] < weights[second])
            std::swap(first, second);
        parent[second] = first;
        weights[first] += weights[second];
    }
};

bool allReachable(const std::vector<Point> &points, const std::vector<std::pair<int, int>> &edges) {
    int size = static_cast<int>(points.size());
    DisjointSets sets(size);
    for (auto [a, b] : edges)
        sets.unite(a, b);
    for (std::size_t i = 0; i < edges.size(); ++i) {
        auto [a, b] = edges[i];
        for (std::size_t j = 0; j < i; ++j) {
            auto [c, d] = edges[j];
            if (intersects(points[a], points[b], points[c], points[d]))
                sets.unite(a, c);
        }
        for (int vertex = 0; vertex < size; ++vertex) {
            if (onSegment(points[vertex], points[a], points[b]))
                sets.unite(a, vertex);
        }
    }
    int root = sets.find(0);
    for (int vertex = 0; vertex < size; ++vertex) {
        if (sets.find(vertex) != root)
            return false;
    }
    return true;
}

int main() {
    int size, count;
    std::cin >> size >> count;
    std::vector<Point> points(size);
    for (auto &point : points)
        std::cin >> point.x >> point.y;
    std::vector<std::pair<int, int>> edges(count);
    for (auto &[a, b] : edges) {
        std::cin >> a >> b;
        --a;
        --b;
    }
    std::cout << (allReachable(points, edges) ? "YES\n" : "NO\n");
}
