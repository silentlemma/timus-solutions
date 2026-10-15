#include <cstdio>
#include <map>
#include <string>
#include <utility>
#include <vector>

typedef std::pair<int, int> Cell;
typedef std::vector<Cell> Path;
const int BLOCK = 4;  // rows or columns added at a time
const int SMALLEST = 4;  // boards with a shorter side have no tour, apart from 2 x 2
const int BOTTOM = SMALLEST - 1;  // the last row of a strip

const Cell NO_TOUR = {5, 5};  // the one board with both sides at least 4 and no tour
const Cell ODD_BASE = {5, 9};  // the base when both sides are of the form 4k + 1

// closed tours of small boards, as flat (row, column) lists ending at the start,
// printed by 1674_constructive_table.py
const std::map<Cell, std::vector<int>> BASES = {
    {{5, 6}, {0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5, 3,
              5, 3, 4, 4, 5, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0,
              1, 1, 0, 0}},
    {{5, 7}, {0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2,
              5, 2, 6, 3, 6, 3, 5, 4, 6, 4, 5, 3, 4, 2, 4, 3, 3, 4, 4, 4, 3, 3, 2, 4, 2, 3, 1, 4, 1,
              4, 0, 3, 0, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0}},
    {{6, 6}, {0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5, 3, 5, 3, 4, 2,
              3, 2, 2, 3, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 4, 4, 3, 5, 3, 5, 2, 4, 2, 5, 1, 5, 0, 4, 0,
              4, 1, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0}},
    {{6, 7}, {0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4, 3,
              5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 4, 4, 5, 4, 4, 3, 3, 4, 2, 3, 2, 2, 3, 3, 3, 2,
              4, 2, 5, 3, 5, 2, 4, 1, 5, 1, 5, 0, 4, 0, 3, 1, 3, 0, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0}},
    {{7, 7}, {0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4, 3,
              5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 6, 6, 6, 5, 5, 4, 6, 4, 5, 3, 4, 4, 3, 4, 2, 3,
              2, 2, 3, 3, 3, 2, 4, 3, 4, 2, 5, 2, 6, 3, 6, 2, 5, 1, 6, 1, 6, 0, 5, 0, 4, 1, 4, 0, 3,
              0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0}},
    {{5, 9}, {0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 2, 4, 2, 5, 1, 5, 0, 4, 0, 5, 1,
              6, 0, 6, 0, 7, 1, 7, 0, 8, 1, 8, 2, 7, 2, 8, 3, 8, 3, 7, 4, 8, 4, 7, 3, 6, 2, 6, 3, 5,
              4, 6, 4, 5, 3, 4, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1,
              0, 1, 1, 0, 0}},
};

// a closed tour of the 4 x m board: along the top two rows in a zigzag, down
// the right end, back along the bottom two rows, up the left end
Path strip(int m) {
    Path path = {{0, 0}, {0, 1}, {1, 1}};
    for (int c = 2; c < m - 1; c++) {
        path.push_back({0, c});
        if (c < m - 2) {
            path.push_back({1, c});
        }
    }
    for (Cell cell : {Cell{0, m - 1}, {1, m - 1}, {1, m - 2}, {2, m - 1}, {BOTTOM, m - 1}}) {
        path.push_back(cell);
    }
    for (int c = m - 2; c > 1; c--) {
        path.push_back({BOTTOM, c});
        path.push_back({2, c});
    }
    for (Cell cell : {Cell{BOTTOM, 1}, {BOTTOM, 0}, {2, 0}, {2, 1}, {1, 0}, {0, 0}}) {
        path.push_back(cell);
    }
    return path;
}

Path flip(Path path) {
    for (Cell& cell : path) {
        std::swap(cell.first, cell.second);
    }
    return path;
}

Path base(int n, int m) {
    if (n == SMALLEST) {
        return strip(m);
    }
    if (m == SMALLEST) {
        return flip(strip(n));
    }
    bool swapped = !BASES.count({n, m});
    const std::vector<int>& flat = BASES.at(swapped ? Cell{m, n} : Cell{n, m});
    Path path;
    for (size_t i = 0; i < flat.size(); i += 2) {
        path.push_back({flat[i], flat[i + 1]});
    }
    return swapped ? flip(path) : path;
}

std::vector<std::string> grid;

// draw the move between cells a and b, or with ch = ' ' erase it
void mark(Cell a, Cell b, char ch = 0) {
    if (ch == 0) {
        if (a.first == b.first) {
            ch = '-';
        } else if (a.second == b.second) {
            ch = '|';
        } else {
            ch = b.first - a.first == b.second - a.second ? '\\' : '/';
        }
    }
    grid[a.first + b.first][a.second + b.second] = ch;
}

void draw(const Path& path, int dr, int dc, bool swap) {
    for (size_t i = 0; i + 1 < path.size(); i++) {
        Cell a = swap ? Cell{path[i].second, path[i].first} : path[i];
        Cell b = swap ? Cell{path[i + 1].second, path[i + 1].first} : path[i + 1];
        mark({a.first + dr, a.second + dc}, {b.first + dr, b.second + dc});
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    grid.assign(2 * n - 1, std::string(2 * m - 1, ' '));
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            grid[2 * r][2 * c] = 'o';
        }
    }
    if (n == 2 && m == 2) {
        draw({{0, 0}, {0, 1}, {1, 1}, {1, 0}, {0, 0}}, 0, 0, false);
    } else if (n < SMALLEST || m < SMALLEST || Cell{n, m} == NO_TOUR) {
        printf("No\n");
        return 0;
    } else {
        // a base board whose sides leave multiples of 4; two sides of the
        // form 4k + 1 start from 5 x 9 instead, as 5 x 5 has no tour
        int bn = SMALLEST + (n - SMALLEST) % BLOCK, bm = SMALLEST + (m - SMALLEST) % BLOCK;
        if (n % BLOCK == 1 && m % BLOCK == 1) {
            bool wide = m >= ODD_BASE.second;
            bn = wide ? ODD_BASE.first : ODD_BASE.second;
            bm = wide ? ODD_BASE.second : ODD_BASE.first;
        }
        draw(base(bn, bm), 0, 0, false);
        // each new 4-wide block has its own strip tour; three edges at the
        // seam are swapped for three others, which joins the two cycles
        for (int cur = bm; cur < m; cur += BLOCK) {
            draw(strip(bn), 0, cur, true);
            mark({0, cur - 1}, {1, cur - 1}, ' ');
            mark({0, cur}, {1, cur}, ' ');
            mark({2, cur}, {1, cur + 1}, ' ');
            mark({0, cur - 1}, {1, cur});
            mark({1, cur - 1}, {2, cur});
            mark({0, cur}, {1, cur + 1});
        }
        for (int cur = bn; cur < n; cur += BLOCK) {
            draw(strip(m), cur, 0, false);
            mark({cur - 1, 0}, {cur - 1, 1}, ' ');
            mark({cur, 0}, {cur, 1}, ' ');
            mark({cur, 2}, {cur + 1, 1}, ' ');
            mark({cur - 1, 0}, {cur, 1});
            mark({cur - 1, 1}, {cur, 2});
            mark({cur, 0}, {cur + 1, 1});
        }
    }
    std::string out = "Yes\n";
    for (const std::string& row : grid) {
        out += row + "\n";
    }
    printf("%s", out.c_str());
}
