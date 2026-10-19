#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

constexpr int DIRECTION_COUNT = 4;
constexpr int ROW_STEP[DIRECTION_COUNT] = {-1, 0, 1, 0};
constexpr int COL_STEP[DIRECTION_COUNT] = {0, 1, 0, -1};
const string TURN = "FR?L";

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int rows, cols;
    cin >> rows >> cols;
    int stride = cols + 2;
    int capacity = (rows + 2) * stride;
    string border(2 * cols + 1, '.');
    vector<string> grid(1, border);
    int root = 0;
    for (int row = 0; row < 2 * rows - 1; ++row) {
        string line;
        cin >> line;
        line = "." + line + ".";
        auto depot_col = line.find('S');
        if (depot_col != string::npos) {
            root = (row / 2 + 1) * stride + (static_cast<int>(depot_col) + 1) / 2;
        }
        grid.push_back(line);
    }
    grid.push_back(border);

    vector<int> parent(capacity), depth(capacity), first(capacity), sibling(capacity);
    vector<int> incoming(capacity), tin(capacity), size(capacity, 1), heavy(capacity);
    vector<int> preferred(capacity), head(capacity), order, stack(1, root);
    vector<char> turn(capacity);
    const int offsets[DIRECTION_COUNT] = {-stride, 1, stride, -1};
    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();
        tin[node] = static_cast<int>(order.size());
        order.push_back(node);
        int map_row = 2 * (node / stride) - 1;
        int map_col = 2 * (node % stride) - 1;
        for (int direction = 0; direction < DIRECTION_COUNT; ++direction) {
            char edge = grid[map_row + ROW_STEP[direction]][map_col + COL_STEP[direction]];
            if (edge != '-' && edge != '|') {
                continue;
            }
            int child = node + offsets[direction];
            if (child == parent[node]) {
                continue;
            }
            parent[child] = node;
            depth[child] = depth[node] + 1;
            incoming[child] = direction;
            int relative = (direction - incoming[node] + DIRECTION_COUNT) % DIRECTION_COUNT;
            turn[child] = TURN[relative];
            sibling[child] = first[node];
            first[node] = child;
            stack.push_back(child);
        }
    }

    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        int node = *it;
        char state = grid[2 * (node / stride) - 1][2 * (node % stride) - 1];
        if (state == 'X') {
            preferred[node] = node;
        }
        for (int child = first[node]; child; child = sibling[child]) {
            size[node] += size[child];
            if (!heavy[node] || size[child] > size[heavy[node]]) {
                heavy[node] = child;
            }
            if (state == 'S' || turn[child] == state) {
                preferred[node] = preferred[child];
            }
        }
    }
    head[root] = root;
    for (int node : order) {
        for (int child = first[node]; child; child = sibling[child]) {
            head[child] = child == heavy[node] ? head[node] : child;
        }
    }

    int base = 1;
    while (base < static_cast<int>(order.size())) {
        base *= 2;
    }
    vector<int> recent(2 * base);
    int count;
    cin >> count;
    vector<int> destinations(count + 1);
    vector<tuple<int, int, char>> events;
    int previous = preferred[root];
    for (int index = 1; index <= count; ++index) {
        int departure, row, col;
        cin >> departure >> row >> col;
        int destination = row * stride + col;
        destinations[index] = destination;
        if (destination == previous) {
            continue;
        }
        int endpoint = previous;
        while (endpoint != destination) {
            int left = destination;
            int right = endpoint;
            while (head[left] != head[right]) {
                if (depth[head[left]] > depth[head[right]]) {
                    left = parent[head[left]];
                } else {
                    right = parent[head[right]];
                }
            }
            int junction = depth[left] < depth[right] ? left : right;
            int child = first[junction];
            int position = tin[destination];
            while (!(tin[child] <= position && position < tin[child] + size[child])) {
                child = sibling[child];
            }
            events.emplace_back(departure + depth[junction], junction, turn[child]);

            // The latest visitor fixes the selected path in this subtree.
            left = base + tin[child];
            right = left + size[child];
            int latest = 0;
            while (left < right) {
                if (left & 1) {
                    latest = max(latest, recent[left++]);
                }
                if (right & 1) {
                    latest = max(latest, recent[--right]);
                }
                left /= 2;
                right /= 2;
            }
            endpoint = latest ? destinations[latest] : preferred[child];
        }
        for (int position = base + tin[destination]; position; position /= 2) {
            recent[position] = index;
        }
        previous = destination;
    }

    sort(events.begin(), events.end());
    cout << events.size() << '\n';
    for (const auto &event : events) {
        int time, node;
        char direction;
        tie(time, node, direction) = event;
        cout << time << ' ' << node / stride << ' ' << node % stride << ' ' << direction << '\n';
    }
}
