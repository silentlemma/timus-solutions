#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int SIDE = 3, CUBES = SIDE * SIDE * SIDE, WAYS = 6;
// the six directions; cells are numbered x * 9 + y * 3 + z
const int DX[WAYS] = {1, -1, 0, 0, 0, 0}, DY[WAYS] = {0, 0, 1, -1, 0, 0};
const int DZ[WAYS] = {0, 0, 0, 0, 1, -1}, AXIS[WAYS] = {0, 0, 1, 1, 2, 2};
const string NAMES = "RLFBUD";
const int RIGHT = 0, UP = 4;  // indices of R and U

string snake, answer;
int nearCell[CUBES][WAYS];
bool used[CUBES];

int cellOf(int x, int y, int z) {
    if (x < 0 || x >= SIDE || y < 0 || y >= SIDE || z < 0 || z >= SIDE)
        return -1;
    return (x * SIDE + y) * SIDE + z;
}

// the free cells must stay one piece for the rest of the snake
bool connected(int left) {
    int start = 0;
    while (start < CUBES && used[start])
        start++;
    if (start == CUBES)
        return true;
    bool seen[CUBES] = {};
    vector<int> stack = {start};
    seen[start] = true;
    int count = 0;
    while (!stack.empty()) {
        int at = stack.back();
        stack.pop_back();
        count++;
        for (int next : nearCell[at])
            if (next >= 0 && !used[next] && !seen[next]) {
                seen[next] = true;
                stack.push_back(next);
            }
    }
    return count == left;
}

// place cube k + 1 after cube k, which sits at cell at
bool fold(int k, int at, int way) {
    if (k == CUBES - 1)
        return true;
    for (int d = 0; d < WAYS; d++) {
        // a straight cube keeps the direction, a turning one changes axis
        if (snake[k] == 'F' ? d != way : AXIS[d] == AXIS[way])
            continue;
        int next = nearCell[at][d];
        if (next < 0 || used[next])
            continue;
        used[next] = true;
        answer.push_back(NAMES[d]);
        if (connected(CUBES - 2 - k) && fold(k + 1, next, d))
            return true;
        answer.pop_back();
        used[next] = false;
    }
    return false;
}

int main() {
    cin >> snake;
    for (int x = 0; x < SIDE; x++)
        for (int y = 0; y < SIDE; y++)
            for (int z = 0; z < SIDE; z++)
                for (int d = 0; d < WAYS; d++)
                    nearCell[cellOf(x, y, z)][d] = cellOf(x + DX[d], y + DY[d], z + DZ[d]);
    // the cube colours 14 cells one way and 13 the other, and the snake
    // alternates, so it starts on the larger colour: a corner or the centre
    // of a face; up to symmetry that leaves three first moves
    int corner = cellOf(0, 0, 0), face = cellOf(1, 1, 0);
    pair<int, int> roots[] = {{corner, RIGHT}, {face, UP}, {face, RIGHT}};
    for (auto [start, d] : roots) {
        int next = nearCell[start][d];
        fill(used, used + CUBES, false);
        used[start] = used[next] = true;
        answer = string(1, NAMES[d]);
        if (connected(CUBES - 2) && fold(1, next, d)) {
            cout << answer << '\n';
            return 0;
        }
    }
    cout << "IMPOSSIBLE\n";
}
