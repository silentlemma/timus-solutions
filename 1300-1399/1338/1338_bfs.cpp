#include <iostream>
#include <string>
#include <vector>

const int SOUTH = 0, NORTH = 1, WEST = 2, EAST = 3; // also the order cars prefer
const int SIDES = 4;

int main() {
    std::ios::sync_with_stdio(false);
    int w = 0, h = 0;
    std::cin >> w >> h;
    std::string line;
    std::getline(std::cin, line);
    int width = w + 2;
    // the plan with a frame of buildings, as one flat array
    std::vector<std::string> rows(h);
    for (auto &row : rows) {
        std::getline(std::cin, row);
        if (!row.empty() && row.back() == '\r')
            row.pop_back();
        row.resize(w, '.');
    }
    std::vector<char> road(width * (h + 2), 0);
    for (int r = 0; r < h; r++) {
        for (int c = 0; c < w; c++)
            road[(r + 1) * width + c + 1] = rows[r][c] == '#' || rows[r][c] == 'o';
    }
    // control points numbered from the bottom row up, left to right
    std::vector<int> points;
    for (int r = h - 1; r >= 0; r--) {
        for (int c = 0; c < w; c++) {
            if (rows[r][c] == 'o')
                points.push_back((r + 1) * width + c + 1);
        }
    }
    const int steps[SIDES] = {width, -width, -1, 1}; // south, north, west, east
    int m = 0;
    std::cin >> m;
    std::vector<int> dist(road.size()), side(road.size()), order;
    for (int number = 1; number <= m; number++) {
        int target = 0;
        std::cin >> target;
        int goal = points[target - 1];
        std::fill(dist.begin(), dist.end(), -1);
        dist[goal] = 0;
        order.assign(1, goal);
        for (size_t head = 0; head < order.size(); head++) {
            int cell = order[head];
            for (int step : steps) {
                int near = cell + step;
                if (road[near] && dist[near] < 0) {
                    dist[near] = dist[cell] + 1;
                    order.push_back(near);
                }
            }
        }
        // every cell inherits the side its car arrives from from the cell it
        // moves to; cells one step away arrive straight from their own side
        for (size_t i = 1; i < order.size(); i++) {
            int cell = order[i];
            for (int k = 0; k < SIDES; k++) {
                int near = cell + steps[k];
                if (dist[near] == dist[cell] - 1) {
                    // stepping in one direction onto the goal arrives from the opposite side
                    side[cell] = near != goal ? side[near] : k ^ 1;
                    break;
                }
            }
        }
        int counts[SIDES] = {0, 0, 0, 0};
        for (int p : points) {
            if (p != goal && dist[p] > 0)
                counts[side[p]]++;
        }
        std::cout << "Experiment #" << number << ": North: " << counts[NORTH]
                  << ", South: " << counts[SOUTH] << ", East: " << counts[EAST]
                  << ", West: " << counts[WEST] << "\n";
    }
    return 0;
}
