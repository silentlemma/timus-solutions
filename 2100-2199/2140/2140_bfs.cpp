#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

constexpr int PADDING = 2;
constexpr int DIRECTION_COUNT = 4;
constexpr int WALK = 0;
constexpr int JUMP = 1;
constexpr int DROP = 2;
constexpr int CLIMB = 3;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int a, b, h;
    std::cin >> a >> b >> h;
    const int width = b + 2 * PADDING;
    const int rows = a + 2 * PADDING;
    const int plane = width * rows;
    const int size = (h + 2) * plane;
    std::vector<unsigned char> air(size, 0), standing(size, 0);
    for (int z = 1; z <= h; ++z) {
        for (int x = 1; x <= a; ++x) {
            std::string row;
            std::cin >> row;
            for (int y = 1; y <= b; ++y) {
                const int cell = z * plane + (x + 1) * width + y + 1;
                air[cell] = row[y - 1] == '.';
                standing[cell] = air[cell] && !air[cell - plane];
            }
        }
    }
    auto read_cell = [&]() {
        int x, y, z;
        std::cin >> x >> y >> z;
        return z * plane + (x + 1) * width + y + 1;
    };
    const int start = read_cell();
    const int goal = read_cell();
    const int deltas[DIRECTION_COUNT] = {-width, 1, width, -1};
    const std::string directions[DIRECTION_COUNT] = {"north", "east", "south", "west"};
    const std::string types[] = {"walk", "jump", "drop", "climb"};
    std::vector<int> parent(size, -1), queue;
    std::vector<unsigned char> action(size, 0);
    queue.reserve(size);
    queue.push_back(start);
    parent[start] = start;
    for (std::size_t head = 0; head < queue.size() && parent[goal] == -1; ++head) {
        const int cell = queue[head];
        auto visit = [&](int next, int type, int direction) {
            if (standing[next] && parent[next] == -1) {
                parent[next] = cell;
                action[next] = type * DIRECTION_COUNT + direction;
                queue.push_back(next);
            }
        };
        for (int direction = 0; direction < DIRECTION_COUNT; ++direction) {
            const int delta = deltas[direction];
            const int near = cell + delta;
            visit(near, WALK, direction);
            if (air[near] && air[near - plane]) {
                visit(near + delta, JUMP, direction);
            }
            if (air[near]) {
                visit(near - plane, DROP, direction);
            }
            if (air[cell + plane]) {
                visit(near + plane, CLIMB, direction);
            }
        }
    }
    if (parent[goal] == -1) {
        std::cout << "NO\n";
        return 0;
    }
    std::vector<int> path;
    for (int cell = goal; cell != start; cell = parent[cell]) {
        path.push_back(action[cell]);
    }
    std::reverse(path.begin(), path.end());
    std::cout << "YES\n" << path.size() << '\n';
    for (int move : path) {
        std::cout << types[move / DIRECTION_COUNT] << ' ';
        std::cout << directions[move % DIRECTION_COUNT] << '\n';
    }
}
