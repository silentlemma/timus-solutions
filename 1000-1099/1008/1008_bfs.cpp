#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

const int MAX_COORD = 10, SIDE = MAX_COORD + 2, DIRECTIONS = 4;
const int DX[DIRECTIONS] = {1, 0, -1, 0}, DY[DIRECTIONS] = {0, 1, 0, -1};
const char LETTERS[] = "RTLB";

bool black[SIDE][SIDE];

// Neighbour description: breadth-first search from the lowest of the leftmost
// pixels, each line naming the neighbours seen for the first time.
void describe(int count) {
    int sx = 0, sy = 0;
    for (int x = 1; x <= MAX_COORD && !sx; x++)
        for (int y = 1; y <= MAX_COORD && !sx; y++)
            if (black[x][y])
                sx = x, sy = y;
    std::vector<std::pair<int, int>> queue = {{sx, sy}};
    black[sx][sy] = false;
    printf("%d %d\n", sx, sy);
    for (int head = 0; head < count; head++) {
        auto [x, y] = queue[head];
        std::string line;
        for (int d = 0; d < DIRECTIONS; d++)
            if (black[x + DX[d]][y + DY[d]]) {
                black[x + DX[d]][y + DY[d]] = false;
                queue.push_back({x + DX[d], y + DY[d]});
                line += LETTERS[d];
            }
        printf("%s%c\n", line.c_str(), head + 1 < count ? ',' : '.');
    }
}

// Pixel list: replay the same search, the lines tell which pixels it adds.
void list(int sx, int sy, const std::vector<std::string> &lines) {
    std::vector<std::pair<int, int>> queue = {{sx, sy}};
    for (size_t head = 0; head < lines.size(); head++) {
        auto [x, y] = queue[head];
        for (char c : lines[head]) {
            const char *letter = std::find(LETTERS, LETTERS + DIRECTIONS, c);
            if (letter != LETTERS + DIRECTIONS)
                queue.push_back({x + DX[letter - LETTERS], y + DY[letter - LETTERS]});
        }
    }
    std::sort(queue.begin(), queue.end());
    printf("%d\n", (int)queue.size());
    for (auto [x, y] : queue)
        printf("%d %d\n", x, y);
}

int main() {
    std::vector<std::string> tokens;
    for (std::string t; std::cin >> t;)
        tokens.push_back(t);
    // only the description ends with a full stop
    if (tokens.back().back() == '.') {
        std::vector<std::string> lines(tokens.begin() + 2, tokens.end());
        list(std::stoi(tokens[0]), std::stoi(tokens[1]), lines);
    } else {
        int count = std::stoi(tokens[0]);
        for (int i = 0; i < count; i++)
            black[std::stoi(tokens[1 + 2 * i])][std::stoi(tokens[2 + 2 * i])] = true;
        describe(count);
    }
}
