#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

// bridgeless cubic maps with the whole border built, found by a search
const vector<vector<string>> BLOCKS = {
    {R"(O-O-O-O)", R"(|\|/ /|)", R"(O O O-O)", R"(|\   \|)", R"(O-O O O)", R"(|/ /|\|)",
     R"(O-O-O-O)"},
    {R"(O-O-O-O)", R"(|\ \|/|)", R"(O-O O O)", R"(| |  /|)", R"(O-O-O-O)", R"(|     |)",
     R"(O-O O-O)", R"(|/| |\|)", R"(O-O-O-O)"},
    {R"(O-O-O-O)", R"(|\|/ /|)", R"(O O O-O)", R"(|\   \|)", R"(O-O-O O)", R"(|   |\|)",
     R"(O-O O O)", R"(|/|/ \|)", R"(O O O O)", R"(|/ /|\|)", R"(O-O-O-O)"},
    {R"(O-O-O-O)", R"(|\ \|/|)", R"(O O O O)", R"(|\|\ /|)", R"(O O O-O)", R"(|\|   |)",
     R"(O-O O-O)", R"(|   |\|)", R"(O-O-O O)", R"(| |  \|)", R"(O-O O O)", R"(|/ /|\|)",
     R"(O-O-O-O)"},
    {R"(O-O-O-O-O-O)", R"(|\ \|  \|/|)", R"(O-O O-O O O)", R"(| |  /|  /|)", R"(O-O O O O-O)",
     R"(|/ /| |\ \|)", R"(O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O)", R"(|\ \ \ \|/|)", R"(O-O-O O O O)", R"(|    \|\ /|)", R"(O-O-O-O O O)",
     R"(| | |  / /|)", R"(O-O O O O-O)", R"(|/ /| |\ \|)", R"(O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O)", R"(|\|  \| |/|)", R"(O-O O O-O O)", R"(|  /|\   /|)", R"(O-O-O O O-O)",
     R"(|  / /|/  |)", R"(O O-O O O-O)", R"(|\ \ \|/ \|)", R"(O-O O O O O)", R"(|/ /|  /|\|)",
     R"(O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O)", R"(|\| |  \|/|)", R"(O-O O O O O)", R"(|  /|/|\ /|)", R"(O-O-O O-O O)",
     R"(|     |  /|)", R"(O-O-O O O-O)", R"(| | |\|\| |)", R"(O-O O O O-O)", R"(|  \|\ \  |)",
     R"(O-O O O O-O)", R"(|/| | |\ \|)", R"(O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O-O-O)", R"(|\ \ \| | |/ /|)", R"(O-O O O O O O-O)", R"(|/ /| | |\ \ \|)",
     R"(O-O-O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O-O-O-O-O)", R"(|\ \ \|  \| |/ / /|)", R"(O-O O O O-O O O O-O)",
     R"(|/ /| | |\  | |\ \|)", R"(O-O-O-O-O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O-O-O-O-O-O-O)", R"(|\ \ \ \|/ /  | | |/ /|)", R"(O-O O O O O-O O-O O O-O)",
     R"(|/ /| |\  | |\ \ \ \ \|)", R"(O-O-O-O-O-O-O-O-O-O-O-O)"},
    {R"(O-O-O-O-O-O-O-O-O-O-O-O-O-O)", R"(|\ \| |/   \ \|/ /  |/ / /|)",
     R"(O-O O O O-O-O O O O-O O O-O)", R"(|/ / / /| | |  /| |\  |\ \|)",
     R"(O-O-O-O-O-O-O-O-O-O-O-O-O-O)"},
};
const int MIN_SIDE = 3;
const int FLAT = 3; // a strip this high needs at least FLAT_STEP columns
const int FLAT_STEP = 8;
const int FLAT_TOP = 14;
const int STEP = 4;
const int WIDE_TOP = 6;
const int TALL_TOP = 7;
const string NO_WORLD = "Imaginary world";

vector<int> split(int n, int step, int top) {
    vector<int> parts;
    while (n > top) {
        parts.push_back(step);
        n -= step;
    }
    parts.push_back(n);
    return parts;
}

const vector<string> &shape(int w, int h) {
    for (const auto &b : BLOCKS)
        if ((int)b[0].size() / 2 + 1 == w && (int)b.size() / 2 + 1 == h)
            return b;
    return BLOCKS[0];
}

int main() {
    int w, h;
    cin >> w >> h;
    if (w * h % 2 == 1 || min(w, h) < MIN_SIDE) {
        cout << NO_WORLD << "\n";
        return 0;
    }
    bool turned = w % 2 == 1; // then h is even: build the turned map
    if (turned)
        swap(w, h);
    vector<int> widths, heights;
    if (h == FLAT) {
        if (w < FLAT_STEP) {
            cout << NO_WORLD << "\n";
            return 0;
        }
        widths = split(w, FLAT_STEP, FLAT_TOP);
        heights = {FLAT};
    } else {
        widths = split(w, STEP, WIDE_TOP);
        heights = split(h, STEP, TALL_TOP);
    }
    vector<string> grid(2 * h - 1, string(2 * w - 1, ' '));
    int top = 0;
    for (size_t j = 0; j < heights.size(); j++) {
        int bh = heights[j], left = 0;
        for (size_t i = 0; i < widths.size(); i++) {
            int bw = widths[i], y = 2 * top, x = 2 * left;
            const vector<string> &block = shape(bw, bh);
            for (size_t r = 0; r < block.size(); r++)
                grid[y + r].replace(x, block[r].size(), block[r]);
            if (i > 0) {
                // two vertical bridges at the seam, in the lowest two rows,
                // give way to two horizontal ones
                int z = 2 * (top + bh - 2);
                grid[z + 1][x - 2] = grid[z + 1][x] = ' ';
                grid[z][x - 1] = grid[z + 2][x - 1] = '-';
            }
            left += bw;
        }
        if (j > 0) {
            // the same exchange across a horizontal seam, in the last two columns
            int y = 2 * top, x = 2 * (w - 2);
            grid[y - 2][x + 1] = grid[y][x + 1] = ' ';
            grid[y - 1][x] = grid[y - 1][x + 2] = '|';
        }
        top += bh;
    }
    if (turned) {
        vector<string> flipped(grid[0].size(), string(grid.size(), ' '));
        for (size_t r = 0; r < grid.size(); r++)
            for (size_t c = 0; c < grid[r].size(); c++) {
                char ch = grid[r][c];
                flipped[c][r] = ch == '-' ? '|' : ch == '|' ? '-' : ch;
            }
        grid = flipped;
    }
    string out;
    for (const string &row : grid)
        out += row + "\n";
    cout << out;
}
