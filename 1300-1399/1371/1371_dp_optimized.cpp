#include <cstdint>
#include <cstdio>
#include <vector>

const int INPUT_SIZE = 4096;

struct Input {
    unsigned char bytes[INPUT_SIZE];
    int position = 0, length = 0;

    int next() {
        if (position == length) {
            length = int(fread(bytes, 1, sizeof(bytes), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return bytes[position++];
    }

    int number() {
        int c = next(), value = 0;
        while (c && c <= ' ')
            c = next();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = next();
        }
        return value;
    }
};

struct Edge {
    uint32_t next;
    uint16_t vertex, weight;
};

constexpr long long DECIMAL_SCALE = 10000;

int main() {
    Input input;
    int n = input.number();
    std::vector<uint32_t> head(n + 1);
    std::vector<Edge> edges(2 * n - 1);
    uint32_t used = 0;
    auto add = [&](int a, int b, int weight) {
        edges[++used] = {head[a], uint16_t(b), uint16_t(weight)};
        head[a] = used;
    };
    for (int i = 1; i < n; ++i) {
        int a = input.number(), b = input.number(), weight = input.number();
        add(a, b, weight);
        add(b, a, weight);
    }
    std::vector<uint16_t> parent(n + 1), cost(n + 1), size(n + 1, 1), order;
    order.reserve(n);
    order.push_back(1);
    for (size_t i = 0; i < order.size(); ++i) {
        uint16_t vertex = order[i];
        for (uint32_t edge = head[vertex]; edge; edge = edges[edge].next) {
            uint16_t target = edges[edge].vertex;
            if (target == parent[vertex])
                continue;
            parent[target] = vertex;
            cost[target] = edges[edge].weight;
            order.push_back(target);
        }
    }
    long long total = 0;
    // An edge contributes weight*s*(N-s), using64 bits before the first product.
    for (int i = n - 1; i > 0; --i) {
        uint16_t vertex = order[i];
        total += 1LL * cost[vertex] * size[vertex] * (n - size[vertex]);
        size[parent[vertex]] += size[vertex];
    }
    long long numerator = 2 * total, denominator = 1LL * n * (n - 1);
    long long whole = numerator / denominator;
    long long fraction =
        ((numerator % denominator) * DECIMAL_SCALE + denominator / 2) / denominator;
    if (fraction == DECIMAL_SCALE) {
        ++whole;
        fraction = 0;
    }
    printf("%lld.%04lld\n", whole, fraction);
}
