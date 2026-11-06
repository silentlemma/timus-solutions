#include <array>
#include <cstdint>
#include <cstdio>

constexpr int MAX_ROUND = 50;
constexpr int MAX_PROBLEMS = 2 * MAX_ROUND;
constexpr int MAX_PAIRS = 100;

struct Edge {
    int to, next;
};

int main() {
    int round_size, pairs;
    if (std::scanf("%d%d", &round_size, &pairs) != 2) {
        return 0;
    }
    std::array<int, MAX_PROBLEMS + 1> first{};
    std::array<Edge, 2 * MAX_PAIRS + 1> edges;
    int edge_count = 0;
    const auto link = [&](int from, int to) {
        edges[++edge_count] = {to, first[from]};
        first[from] = edge_count;
    };
    for (int i = 0; i < pairs; ++i) {
        int a, b;
        std::scanf("%d%d", &a, &b);
        link(a, b);
        link(b, a);
    }

    const int total = 2 * round_size;
    std::array<int, MAX_PROBLEMS + 1> component{};
    std::array<int, MAX_PROBLEMS + 1> colour;
    std::array<std::array<int, 2>, MAX_PROBLEMS + 1> count{};
    std::array<int, MAX_PROBLEMS> queue;
    int components = 0;
    for (int start = 1; start <= total; ++start) {
        if (component[start] != 0) {
            continue;
        }
        ++components;
        queue[0] = start;
        component[start] = components;
        colour[start] = 0;
        int end = 1;
        for (int head = 0; head < end; ++head) {
            const int v = queue[head];
            ++count[components][colour[v]];
            for (int i = first[v]; i != 0; i = edges[i].next) {
                const int w = edges[i].to;
                if (component[w] == 0) {
                    component[w] = components;
                    colour[w] = 1 - colour[v];
                    queue[end++] = w;
                } else if (colour[v] == colour[w]) {
                    std::puts("IMPOSSIBLE");
                    return 0;
                }
            }
        }
    }

    // One bit per achievable size of the first round, retained for reconstruction.
    std::array<std::uint64_t, MAX_PROBLEMS + 1> reach;
    reach[0] = 1;
    for (int k = 1; k <= components; ++k) {
        const auto [left, right] = count[k];
        const auto take_left = left <= round_size ? reach[k - 1] << left : 0;
        const auto take_right = right <= round_size ? reach[k - 1] << right : 0;
        reach[k] = take_left | take_right;
    }
    if (((reach[components] >> round_size) & 1) == 0) {
        std::puts("IMPOSSIBLE");
        return 0;
    }
    std::array<int, MAX_PROBLEMS + 1> first_colour;
    for (int k = components, left = round_size; k > 0; --k) {
        const int before = left - count[k][0];
        const int side = before >= 0 && ((reach[k - 1] >> before) & 1) ? 0 : 1;
        first_colour[k] = side;
        left -= count[k][side];
    }
    for (bool first_round : {true, false}) {
        bool space = false;
        for (int v = 1; v <= total; ++v) {
            if ((colour[v] == first_colour[component[v]]) == first_round) {
                std::printf(space ? " %d" : "%d", v);
                space = true;
            }
        }
        std::putchar('\n');
    }
}
