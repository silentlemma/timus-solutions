#include <cstdint>
#include <cstdio>
#include <vector>

int main() {
    int size, start;
    if (std::scanf("%d%d", &size, &start) != 2)
        return 0;
    std::vector<std::vector<std::uint16_t>> incoming(size + 1);
    int missing = 0;
    for (int from = 1; from <= size; ++from) {
        for (int to = 1; to <= size; ++to) {
            int ch = std::getchar();
            while (ch != EOF && ch <= ' ')
                ch = std::getchar();
            if (ch == '0' && from != to) {
                incoming[to].push_back(from);
                ++missing;
            }
        }
    }

    // Traverse reversed channels so Hierholzer's pop order gives the forward route.
    std::vector<std::uint16_t> path;
    path.reserve(missing + 1);
    path.push_back(start);
    int previous = 0;
    while (!path.empty()) {
        const int city = path.back();
        auto &edges = incoming[city];
        if (!edges.empty()) {
            path.push_back(edges.back());
            edges.pop_back();
        } else {
            if (previous != 0)
                std::printf("%d %d\n", previous, city);
            previous = city;
            path.pop_back();
        }
    }
}
