#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int height, width;
    std::cin >> height >> width;
    const int stride = width + 2;
    const int size = (height + 2) * stride;
    int row, column;
    std::cin >> row >> column;
    const int start = row * stride + column;
    std::cin >> row >> column;
    int drone = row * stride + column;

    std::vector<int> cost(size, 0), successor(size, 0);
    for (int r = 1; r <= height; ++r) {
        for (int c = 1; c <= width; ++c) {
            std::cin >> cost[r * stride + c];
        }
    }
    for (int r = 1; r <= height; ++r) {
        std::string wind;
        std::cin >> wind;
        for (int c = 1; c <= width; ++c) {
            const int cell = r * stride + c;
            switch (wind[c - 1]) {
            case 'U':
                successor[cell] = cell - stride;
                break;
            case 'D':
                successor[cell] = cell + stride;
                break;
            case 'L':
                successor[cell] = cell - 1;
                break;
            case 'R':
                successor[cell] = cell + 1;
                break;
            }
        }
    }

    const long long infinity = std::numeric_limits<long long>::max() / 2;
    std::vector<long long> distance(size, infinity);
    const std::vector<int> offsets = {-stride, stride, -1, 1};
    using Entry = std::pair<long long, int>;
    std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> heap;
    distance[start] = 0;
    heap.emplace(0, start);
    while (!heap.empty()) {
        const auto [time, cell] = heap.top();
        heap.pop();
        if (time != distance[cell]) {
            continue;
        }
        for (int offset : offsets) {
            const int next = cell + offset;
            if (cost[next] == 0) {
                continue;
            }
            const long long arrival = time + cost[next];
            if (arrival < distance[next]) {
                distance[next] = arrival;
                heap.emplace(arrival, next);
            }
        }
    }

    std::vector<int> first(size, -1), path;
    while (cost[drone] != 0 && first[drone] == -1) {
        first[drone] = static_cast<int>(path.size());
        path.push_back(drone);
        drone = successor[drone];
    }
    const int length = static_cast<int>(path.size());
    const int cycle_start = cost[drone] == 0 ? length : first[drone];
    const int period = length - cycle_start;
    long long answer = infinity;
    for (int time = 0; time < length; ++time) {
        const long long arrival = distance[path[time]];
        long long catch_time = time;
        if (arrival > time) {
            if (time < cycle_start) {
                continue;
            }
            // A cycle cell can be caught on its first visit after arrival.
            catch_time += ((arrival - time + period - 1) / period) * period;
        }
        if (catch_time < answer) {
            answer = catch_time;
        }
    }
    std::cout << (answer == infinity ? -1 : answer) << '\n';
}
