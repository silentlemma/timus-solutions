#include <array>
#include <cstdint>
#include <cstdio>

using Mask = std::uint32_t;

constexpr int MAX_VERTICES = 30;
constexpr int GROUP_BITS = 5;
constexpr int GROUPS = 4;
constexpr int INPUT_FIELDS = 3;
constexpr Mask GROUP_MASK = (Mask{1} << GROUP_BITS) - 1;
constexpr Mask HOME = 1;
constexpr Mask WORK = 2;

struct Graph {
    std::array<std::array<std::array<Mask, GROUP_MASK + 1>, GROUPS>, MAX_VERTICES> adjacent{};

    void add(int a, int b, int category) {
        const int group = category / GROUP_BITS;
        const Mask bit = Mask{1} << (category % GROUP_BITS);
        adjacent[a][group][bit] |= Mask{1} << b;
        adjacent[b][group][bit] |= Mask{1} << a;
    }

    void fill() {
        for (auto &vertex : adjacent)
            for (auto &group : vertex)
                for (Mask mask = 1; mask <= GROUP_MASK; ++mask) {
                    const Mask previous = mask & (mask - 1);
                    group[mask] |= group[previous] | group[mask ^ previous];
                }
    }

    bool connects(Mask categories) const {
        const auto a = categories & GROUP_MASK;
        const auto b = (categories >> GROUP_BITS) & GROUP_MASK;
        const auto c = (categories >> (2 * GROUP_BITS)) & GROUP_MASK;
        const auto d = categories >> (3 * GROUP_BITS);
        Mask reached = HOME, pending = HOME;
        while (pending) {
            const auto &vertex = adjacent[__builtin_ctz(pending)];
            pending &= pending - 1;
            const Mask fresh =
                (vertex[0][a] | vertex[1][b] | vertex[2][c] | vertex[GROUPS - 1][d]) & ~reached;
            if (fresh & WORK)
                return true;
            reached |= fresh;
            pending |= fresh;
        }
        return false;
    }
};

int main() {
    int categories, vertices, roads;
    if (std::scanf("%d%d%d", &categories, &vertices, &roads) != INPUT_FIELDS)
        return 0;
    Graph graph;
    for (int i = 0; i < roads; ++i) {
        int a, b, category;
        if (std::scanf("%d%d%d", &a, &b, &category) != INPUT_FIELDS)
            return 0;
        graph.add(a, b, category);
    }
    graph.fill();

    const Mask limit = Mask{1} << categories;
    for (int count = 1; count <= categories; ++count) {
        Mask mask = (Mask{1} << count) - 1;
        while (mask < limit) {
            if (graph.connects(mask)) {
                std::printf("%d\n", count);
                const char *separator = "";
                for (int category = 0; category < categories; ++category) {
                    if (mask & (Mask{1} << category)) {
                        std::printf("%s%d", separator, category);
                        separator = " ";
                    }
                }
                std::putchar('\n');
                return 0;
            }
            // Move to the next mask with the same number of set bits.
            const Mask raised = mask + (mask & -mask);
            mask = raised | ((raised ^ mask) >> (__builtin_ctz(mask) + 2));
        }
    }
}
