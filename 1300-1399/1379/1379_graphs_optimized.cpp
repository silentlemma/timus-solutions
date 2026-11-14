#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int DAY = 24 * 60;
constexpr int TRUCK = 3000000;
constexpr int CUP = 100;
constexpr int ORDER = 10000000;
constexpr int BUFFER_SIZE = 16384;
constexpr int NONE = -1;

class Input {
    unsigned char buffer[BUFFER_SIZE];
    std::size_t index = 0, size = 0;

    int byte() {
        if (index == size) {
            size = std::fread(buffer, 1, sizeof buffer, stdin);
            index = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[index++];
    }

  public:
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        int result = 0;
        for (; c >= '0' && c <= '9'; c = byte())
            result = result * 10 + c - '0';
        return result;
    }
};

struct Edge {
    int cups;
    int next;
    std::uint16_t to, minutes;
};

int main() {
    Input input;
    const int vertices = input.number();
    const int roads = input.number();
    if (vertices == 1) {
        std::printf("%d\n", ORDER);
        return 0;
    }
    std::vector<int> first(vertices, NONE), limits;
    std::vector<Edge> edges;
    const auto add = [&](int from, int to, int minutes, int cups) {
        edges.push_back({cups, first[from], static_cast<std::uint16_t>(to),
                         static_cast<std::uint16_t>(minutes)});
        first[from] = static_cast<int>(edges.size()) - 1;
    };
    for (int i = 0; i < roads; ++i) {
        const int a = input.number() - 1;
        const int b = input.number() - 1;
        const int minutes = input.number();
        const int weight = input.number();
        if (minutes > DAY || weight < TRUCK + CUP)
            continue;
        const int cups = std::min(ORDER, (weight - TRUCK) / CUP);
        add(a, b, minutes, cups);
        add(b, a, minutes, cups);
        limits.push_back(cups);
    }
    std::sort(limits.begin(), limits.end());
    limits.erase(std::unique(limits.begin(), limits.end()), limits.end());

    std::vector<int> distance(vertices), next(vertices), previous(vertices);
    std::array<int, DAY + 1> bucket;
    const auto possible = [&](int cups) {
        std::fill(distance.begin(), distance.end(), DAY + 1);
        bucket.fill(NONE);
        const auto insert = [&](int v, int time) {
            distance[v] = time;
            previous[v] = NONE;
            next[v] = bucket[time];
            if (next[v] != NONE)
                previous[next[v]] = v;
            bucket[time] = v;
        };
        insert(0, 0);
        for (int time = 0; time <= DAY; ++time) {
            while (bucket[time] != NONE) {
                const int v = bucket[time];
                bucket[time] = next[v];
                if (next[v] != NONE)
                    previous[next[v]] = NONE;
                if (v == vertices - 1)
                    return true;
                for (int i = first[v]; i != NONE; i = edges[i].next) {
                    const auto &edge = edges[i];
                    const int to = edge.to;
                    const int arrival = time + edge.minutes;
                    const int old = distance[to];
                    if (edge.cups < cups || arrival >= old)
                        continue;
                    // Decrease-key keeps just one list entry per junction.
                    if (old <= DAY) {
                        if (previous[to] == NONE)
                            bucket[old] = next[to];
                        else
                            next[previous[to]] = next[to];
                        if (next[to] != NONE)
                            previous[next[to]] = previous[to];
                    }
                    insert(to, arrival);
                }
            }
        }
        return false;
    };

    std::size_t left = 0, right = limits.size();
    while (left < right) {
        const std::size_t middle = left + (right - left) / 2;
        if (possible(limits[middle]))
            left = middle + 1;
        else
            right = middle;
    }
    std::printf("%d\n", left == 0 ? 0 : limits[left - 1]);
}
