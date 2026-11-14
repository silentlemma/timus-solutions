#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int FLIGHT_FIELDS = 3;

struct City {
    int joy = 0;
    int degree = 0, neighbors = 0, weights = 0;
    int first = 0, second = 0;
    int first_child = 0, second_child = 0;
};

int main() {
    int cities, flights;
    if (std::scanf("%d%d", &cities, &flights) != 2)
        return 0;
    std::vector<City> tree(cities + 1);
    for (int i = 1; i <= cities; ++i) {
        if (std::scanf("%d", &tree[i].joy) != 1)
            return 0;
    }
    const auto add = [&](int city, int neighbor, int joy) {
        ++tree[city].degree;
        tree[city].neighbors ^= neighbor;
        tree[city].weights ^= joy;
    };
    for (int i = 0; i < flights; ++i) {
        int a, b, joy;
        if (std::scanf("%d%d%d", &a, &b, &joy) != FLIGHT_FIELDS)
            return 0;
        add(a, b, joy);
        add(b, a, joy);
    }

    std::vector<int> order;
    order.reserve(cities);
    for (int i = 1; i <= cities; ++i) {
        if (tree[i].degree <= 1)
            order.push_back(i);
    }
    int best = -1, center = 0;
    for (std::size_t i = 0; i < order.size(); ++i) {
        const int v = order[i];
        const City &city = tree[v];
        const int through = city.joy + city.first + city.second;
        if (through > best) {
            best = through;
            center = v;
        }
        if (city.degree == 0)
            continue;

        // At a leaf the two XOR accumulators identify its only remaining edge.
        const int parent = city.neighbors;
        const int weight = city.weights;
        City &above = tree[parent];
        above.neighbors ^= v;
        above.weights ^= weight;
        if (--above.degree == 1)
            order.push_back(parent);

        const int branch = weight + city.joy + city.first;
        if (branch > above.first) {
            above.second = above.first;
            above.second_child = above.first_child;
            above.first = branch;
            above.first_child = v;
        } else if (branch > above.second) {
            above.second = branch;
            above.second_child = v;
        }
    }

    order.clear();
    for (int v = tree[center].first_child; v; v = tree[v].first_child)
        order.push_back(v);
    std::reverse(order.begin(), order.end());
    order.push_back(center);
    for (int v = tree[center].second_child; v; v = tree[v].first_child)
        order.push_back(v);
    std::printf("%d\n%zu\n", best, order.size());
    for (std::size_t i = 0; i < order.size(); ++i)
        std::printf("%d%c", order[i], i + 1 == order.size() ? '\n' : ' ');
}
