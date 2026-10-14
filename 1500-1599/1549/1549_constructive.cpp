#include <algorithm>
#include <cstdio>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, int> Cell;
const int CORNERS = 4;        // a loop turns at least four times, by 90 degrees each
const int FIRST_STAIR = 12;   // all-turn loops have 4 or at least 12 turns
const int NOTCHED_HEIGHT = 3; // rows of the box when a corner is cut in

// F, L or R for every cell of a closed loop of cells
string letters(const vector<Cell> &cells) {
    string out;
    int n = cells.size();
    for (int i = 0; i < n; i++) {
        Cell a = cells[(i + n - 1) % n], b = cells[i], c = cells[(i + 1) % n];
        int dx1 = b.first - a.first, dy1 = b.second - a.second;
        int dx2 = c.first - b.first, dy2 = c.second - b.second;
        out += dx1 == dx2 && dy1 == dy2 ? 'F' : dx1 * dy2 - dy1 * dx2 > 0 ? 'L' : 'R';
    }
    return out;
}

// the border of a width x height box, counterclockwise from the lower left
// corner, with bumps (2 cells wide, 1 high) on the top and bottom rows, and
// with the lower left corner cut in if notch is set
vector<Cell> ring(int width, int height, int bumps, bool notch) {
    vector<int> freeTop, freeBottom; // pairs (x, x - 1) on top, (x - 1, x) at the bottom
    for (int x = width - 2; x > 1; x -= 2)
        freeTop.push_back(x);
    for (int x = 2 + notch; x < width - 1; x += 2)
        freeBottom.push_back(x);
    int up = min(bumps, (int)freeTop.size());
    set<int> upAt(freeTop.begin(), freeTop.begin() + up);
    set<int> downAt(freeBottom.begin(), freeBottom.begin() + (bumps - up));
    vector<Cell> cells;
    if (notch)
        cells = {{1, 1}, {1, 0}};
    else
        cells = {{0, 0}};
    for (int x = cells.back().first + 1; x < width; x++) { // the bottom row, going east
        if (downAt.count(x))
            cells.insert(cells.end(), {{x - 1, -1}, {x, -1}});
        cells.push_back({x, 0});
    }
    for (int y = 1; y < height; y++)
        cells.push_back({width - 1, y});
    for (int x = width - 2; x >= 0; x--) { // the top row, going west
        cells.push_back({x, height - 1});
        if (upAt.count(x)) {
            cells.insert(cells.end(), {{x, height}, {x - 1, height}, {x - 1, height - 1}});
            x--;
        }
    }
    // the left column, going south; with a notch its last cell (0, 1) leads
    // into (1, 1) instead of the corner
    for (int y = height - 2; y > 0; y--)
        cells.push_back({0, y});
    return cells;
}

string build(int straights, int turns) {
    if (straights == 0 && turns >= FIRST_STAIR) {
        // a staircase loop: four corners and steps LR on the sides
        int steps = (turns - CORNERS) / CORNERS;
        string sideA, sideB = "LR";
        for (int i = 1; i < steps; i++)
            sideA += "LR";
        string half = "L" + sideA + "L" + sideB;
        return half + half;
    }
    bool notch = turns % CORNERS == 2;
    int bumps = (turns - CORNERS) / CORNERS; // a notch takes the other 2 turns
    int width = 2 + straights / 2 + bumps;
    return letters(ring(width, notch ? NOTCHED_HEIGHT : 2, bumps, notch));
}

int main() {
    int s, t;
    if (scanf("%d %d", &s, &t) != 2)
        return 0;
    // both counts even, at least 4 turns, and without straights the turns
    // must be 4 or a multiple of 4 from 12
    int straights = s - s % 2, turns = t - t % 2;
    if (turns < CORNERS) {
        printf("Atawazu\n");
        return 0;
    }
    if (straights == 0) {
        turns -= turns % CORNERS;
        if (turns < FIRST_STAIR)
            turns = CORNERS;
    }
    string path = build(straights, turns);
    printf("%d\n%s\n", (int)path.size(), path.c_str());
}
