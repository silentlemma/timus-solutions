#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

enum class Parent : std::uint8_t { below, left, right };

int main() {
    int floors, width;
    if (std::scanf("%d%d", &floors, &width) != 2)
        return 0;
    std::vector<Parent> parents(floors * width, Parent::below);
    std::vector<long long> cost(width), fee(width);
    for (int floor = 0; floor < floors; ++floor) {
        Parent *directions = parents.data() + floor * width;
        for (int room = 0; room < width; ++room) {
            std::scanf("%lld", &fee[room]);
            cost[room] += fee[room];
        }
        for (int room = 1; room < width; ++room) {
            const long long candidate = cost[room - 1] + fee[room];
            if (candidate < cost[room]) {
                cost[room] = candidate;
                directions[room] = Parent::left;
            }
        }
        for (int room = width - 2; room >= 0; --room) {
            const long long candidate = cost[room + 1] + fee[room];
            if (candidate < cost[room]) {
                cost[room] = candidate;
                directions[room] = Parent::right;
            }
        }
    }
    int room = static_cast<int>(std::min_element(cost.begin(), cost.end()) - cost.begin());
    int floor = floors - 1;
    std::vector<std::uint16_t> path;
    while (floor >= 0) {
        path.push_back(room + 1);
        switch (parents[floor * width + room]) {
        case Parent::below:
            --floor;
            break;
        case Parent::left:
            --room;
            break;
        case Parent::right:
            ++room;
            break;
        }
    }
    for (auto i = path.rbegin(); i != path.rend(); ++i)
        std::printf("%d%c", *i, i + 1 == path.rend() ? '\n' : ' ');
}
