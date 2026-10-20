#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int MIN_SIDE = 3;

struct Board {
    int left, bottom, right, top;
};

struct Event {
    int coordinate, low, high, board, side;
};

class DisjointSet {
    std::vector<int> parent;
    std::vector<int> size;

  public:
    explicit DisjointSet(int count) : parent(count), size(count, 1) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int vertex) {
        while (parent[vertex] != vertex) {
            parent[vertex] = parent[parent[vertex]];
            vertex = parent[vertex];
        }
        return vertex;
    }

    void unite(int first, int second) {
        first = find(first);
        second = find(second);
        if (first == second) {
            return;
        }
        if (size[first] < size[second]) {
            std::swap(first, second);
        }
        parent[second] = first;
        size[first] += size[second];
    }

    int component_size(int vertex) { return size[find(vertex)]; }
};

void connect(std::vector<Event> &events, DisjointSet &components) {
    std::sort(events.begin(), events.end(), [](const Event &first, const Event &second) {
        if (first.coordinate != second.coordinate) {
            return first.coordinate < second.coordinate;
        }
        return first.low < second.low;
    });
    int coordinate = 0;
    std::array<int, 2> last = {-1, -1};
    std::array<int, 2> high = {0, 0};
    for (const Event &event : events) {
        if (event.coordinate != coordinate) {
            coordinate = event.coordinate;
            last = {-1, -1};
        }
        const int opposite = 1 - event.side;
        // Sides of the same kind at this coordinate have disjoint closed intervals.
        if (last[opposite] != -1 && high[opposite] >= event.low) {
            components.unite(event.board, last[opposite]);
        }
        last[event.side] = event.board;
        high[event.side] = event.high;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count, limit, x, y;
    std::cin >> count >> limit >> x >> y;
    std::vector<Board> boards(count);
    int start = 0;
    bool isolated = false;
    for (int index = 0; index < count; ++index) {
        Board &board = boards[index];
        std::cin >> board.left >> board.bottom >> board.right >> board.top;
        if (board.left <= x && x < board.right && board.bottom <= y && y < board.top) {
            start = index;
            isolated = board.right - board.left == MIN_SIDE &&
                       board.top - board.bottom == MIN_SIDE && x == board.left + 1 &&
                       y == board.bottom + 1;
        }
    }
    if (isolated) {
        std::cout << 1 << '\n';
        return 0;
    }

    DisjointSet components(count);
    std::vector<Event> events;
    events.reserve(2 * count);
    for (int axis = 0; axis < 2; ++axis) {
        events.clear();
        for (int index = 0; index < count; ++index) {
            const Board &board = boards[index];
            if (axis == 0) {
                events.push_back({board.right + 1, board.bottom, board.top, index, 0});
                events.push_back({board.left, board.bottom, board.top, index, 1});
            } else {
                events.push_back({board.top + 1, board.left, board.right, index, 0});
                events.push_back({board.bottom, board.left, board.right, index, 1});
            }
        }
        connect(events, components);
    }
    std::cout << components.component_size(start) << '\n';
}
