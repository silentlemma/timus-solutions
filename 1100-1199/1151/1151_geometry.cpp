#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

// beacons and control points lie on the grid from 1 to SIDE
const int SIDE = 200;

struct Measure {
    int x, y, r;
};

// the numbers in a line, whatever separates them
std::vector<int> numbers(const std::string &line) {
    std::vector<int> out;
    for (size_t k = 0; k < line.size();) {
        if (!isdigit((unsigned char)line[k])) {
            k++;
            continue;
        }
        int v = 0;
        for (; k < line.size() && isdigit((unsigned char)line[k]); k++)
            v = v * 10 + (line[k] - '0');
        out.push_back(v);
    }
    return out;
}

// the cells at distance exactly r from (x, y) in the max metric
std::vector<std::pair<int, int>> ring(int x, int y, int r) {
    if (r == 0)
        return {{x, y}};
    std::vector<std::pair<int, int>> cells;
    for (int d = -r; d <= r; d++)
        for (int s : {-r, r})
            cells.push_back({x + d, y + s});
    for (int d = -r + 1; d < r; d++)
        for (int s : {-r, r})
            cells.push_back({x + s, y + d});
    return cells;
}

int main() {
    std::string line;
    std::vector<int> first;
    while (first.empty() && std::getline(std::cin, line))
        first = numbers(line);
    if (first.empty())
        return 0;
    int m = first[0];
    std::map<int, std::vector<Measure>> seen;
    for (int i = 0; i < m && std::getline(std::cin, line);) {
        std::vector<int> nums = numbers(line);
        if (nums.empty())
            continue;
        i++;
        for (size_t k = 2; k + 1 < nums.size(); k += 2)
            seen[nums[k]].push_back({nums[0], nums[1], nums[k + 1]});
    }
    for (auto &[beacon, list] : seen) {
        std::vector<std::pair<int, int>> places;
        for (auto [cx, cy] : ring(list[0].x, list[0].y, list[0].r)) {
            if (cx < 1 || cx > SIDE || cy < 1 || cy > SIDE)
                continue;
            bool fits = true;
            for (const Measure &q : list)
                fits = fits && std::max(abs(cx - q.x), abs(cy - q.y)) == q.r;
            if (fits)
                places.push_back({cx, cy});
        }
        if (places.size() == 1)
            printf("%d:%d,%d\n", beacon, places[0].first, places[0].second);
        else
            printf("%d:UNKNOWN\n", beacon);
    }
}
