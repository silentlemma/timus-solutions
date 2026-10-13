#include <cstdio>
#include <string>
#include <vector>

using namespace std;

struct Square {
    int top, left, side, holeRow, holeCol;
};

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    int size = 1 << n, count = 0;
    vector<vector<int>> board(size, vector<int>(size, 0));
    // each square has one cell that is already taken: the hole or a piece of
    // the tromino in the middle of the square above it
    vector<Square> stack = {{0, 0, size, x - 1, y - 1}};
    while (!stack.empty()) {
        Square s = stack.back();
        stack.pop_back();
        if (s.side == 1)
            continue;
        int half = s.side / 2;
        count++;
        for (int dr = 0; dr < 2; dr++)
            for (int dc = 0; dc < 2; dc++) {
                int r0 = s.top + dr * half, c0 = s.left + dc * half;
                if (r0 <= s.holeRow && s.holeRow < r0 + half && c0 <= s.holeCol &&
                    s.holeCol < c0 + half)
                    stack.push_back({r0, c0, half, s.holeRow, s.holeCol});
                else {
                    // the cell of this quarter next to the middle of the square
                    int r = s.top + half - 1 + dr, c = s.left + half - 1 + dc;
                    board[r][c] = count;
                    stack.push_back({r0, c0, half, r, c});
                }
            }
    }
    string out;
    for (auto &row : board)
        for (int c = 0; c < size; c++) {
            out += to_string(row[c]);
            out += c + 1 < size ? ' ' : '\n';
        }
    fputs(out.c_str(), stdout);
}
