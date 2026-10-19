#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

using Time = std::int64_t;

constexpr Time SnowScale = 100;
constexpr Time SnowFactor = 100500;
constexpr Time SnowLimit = SnowScale * (SnowFactor - 1);
constexpr int TimeBits = 30;
constexpr Time TimeMask = (Time{1} << TimeBits) - 1;
constexpr Time Infinity = std::numeric_limits<Time>::max() / 2;

struct Graph {
    std::vector<int> head, to, next, road;
    std::vector<Time> base;
    std::vector<int> offset;
    std::vector<Time> intervals;

    Graph(int vertices, int edges) : head(vertices, -1), base(edges), offset(edges + 1, 0) {
        to.reserve(2 * edges);
        next.reserve(2 * edges);
        road.reserve(2 * edges);
    }

    void add_arc(int from, int target, int edge) {
        to.push_back(target);
        next.push_back(head[from]);
        road.push_back(edge);
        head[from] = static_cast<int>(to.size()) - 1;
    }

    Time duration(int edge, Time elapsed) const {
        elapsed = std::min(elapsed, SnowLimit);
        return base[edge] + (elapsed * base[edge] + SnowScale - 1) / SnowScale;
    }

    Time earliest(int edge, Time current) const {
        Time last_finish = 0;
        for (int index = offset[edge]; index < offset[edge + 1]; ++index) {
            const Time start = intervals[index] >> TimeBits;
            const Time finish = intervals[index] & TimeMask;
            const Time departure = std::max(current, last_finish);
            if (departure < start) {
                const Time arrival = departure + duration(edge, departure - last_finish);
                // A feasible arrival precedes every later cleaning and open gap.
                if (arrival <= start) {
                    return arrival;
                }
            }
            last_finish = finish;
        }
        const Time departure = std::max(current, last_finish);
        return departure + duration(edge, departure - last_finish);
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int vertices, edges;
    std::cin >> vertices >> edges;
    Graph graph(vertices, edges);
    for (int edge = 0; edge < edges; ++edge) {
        int from, to;
        std::cin >> from >> to >> graph.base[edge];
        --from;
        --to;
        graph.add_arc(from, to, edge);
        graph.add_arc(to, from, edge);
    }

    int cleanings;
    std::cin >> cleanings;
    std::vector<int> cleaning_road(cleanings);
    std::vector<Time> unsorted(cleanings);
    for (int index = 0; index < cleanings; ++index) {
        int edge;
        Time start, finish;
        std::cin >> edge >> start >> finish;
        --edge;
        cleaning_road[index] = edge;
        unsorted[index] = (start << TimeBits) | finish;
        ++graph.offset[edge + 1];
    }
    for (int edge = 0; edge < edges; ++edge) {
        graph.offset[edge + 1] += graph.offset[edge];
    }
    graph.intervals.resize(cleanings);
    std::vector<int> cursor = graph.offset;
    for (int index = 0; index < cleanings; ++index) {
        graph.intervals[cursor[cleaning_road[index]]++] = unsorted[index];
    }
    for (int edge = 0; edge < edges; ++edge) {
        std::sort(graph.intervals.begin() + graph.offset[edge],
                  graph.intervals.begin() + graph.offset[edge + 1]);
    }

    using Entry = std::pair<Time, int>;
    std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> heap;
    std::vector<Time> distance(vertices, Infinity);
    distance[0] = 0;
    heap.emplace(0, 0);
    while (!heap.empty()) {
        const auto [current, vertex] = heap.top();
        heap.pop();
        if (current != distance[vertex]) {
            continue;
        }
        if (vertex == vertices - 1) {
            std::cout << current << '\n';
            break;
        }
        for (int arc = graph.head[vertex]; arc != -1; arc = graph.next[arc]) {
            const int target = graph.to[arc];
            const int edge = graph.road[arc];
            if (current + graph.base[edge] >= distance[target]) {
                continue;
            }
            const Time arrival = graph.earliest(edge, current);
            if (arrival < distance[target]) {
                distance[target] = arrival;
                heap.emplace(arrival, target);
            }
        }
    }
}
