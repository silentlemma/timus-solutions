#include <iostream>
#include <string>
#include <vector>

const std::string COLORS = "BGRWY";
const char EMPTY = '.';
const int SIDES = 4;  // neighbours of a cell

int n, m;

// the largest figure of the main colour or of the others; ties go to the
// figure holding the lowest ball, then the leftmost of the lowest balls
std::vector<int> best_figure(const std::string& board, char main_color, bool take_main) {
    std::vector<bool> seen(n * m, false);
    std::vector<int> best;
    int best_low = -1;
    for (int start = 0; start < n * m; start++) {
        char color = board[start];
        if (seen[start] || color == EMPTY || (color == main_color) != take_main) {
            continue;
        }
        seen[start] = true;
        std::vector<int> cells = {start};
        int low = start;
        for (size_t k = 0; k < cells.size(); k++) {
            int v = cells[k], r = v / m, c = v % m;
            if (r > low / m || (r == low / m && c < low % m)) {
                low = v;
            }
            int next[] = {v - m, v + m, v - 1, v + 1};
            bool ok[] = {r > 0, r < n - 1, c > 0, c < m - 1};
            for (int d = 0; d < SIDES; d++) {
                int w = next[d];
                if (ok[d] && !seen[w] && board[w] == color) {
                    seen[w] = true;
                    cells.push_back(w);
                }
            }
        }
        if (cells.size() < 2) {
            continue;
        }
        bool lower = low / m > best_low / m || (low / m == best_low / m && low % m < best_low % m);
        bool better = best.empty() || cells.size() > best.size() ||
                      (cells.size() == best.size() && lower);
        if (better) {
            best = cells;
            best_low = low;
        }
    }
    return best;
}

long long remove_figure(std::string& board, const std::vector<int>& cells) {
    for (int v : cells) {
        board[v] = EMPTY;
    }
    // balls fall down, then empty columns close up to the left
    std::vector<std::string> columns;
    for (int c = 0; c < m; c++) {
        std::string column;
        for (int r = 0; r < n; r++) {
            if (board[r * m + c] != EMPTY) {
                column += board[r * m + c];
            }
        }
        if (!column.empty()) {
            columns.push_back(std::string(n - column.size(), EMPTY) + column);
        }
    }
    for (int c = 0; c < m; c++) {
        for (int r = 0; r < n; r++) {
            board[r * m + c] = c < (int)columns.size() ? columns[c][r] : EMPTY;
        }
    }
    long long k = cells.size();
    return k * (k - 1);
}

long long play(std::string board, char main_color) {
    long long score = 0;
    while (true) {
        while (true) {
            std::vector<int> cells = best_figure(board, main_color, false);
            if (cells.empty()) {
                break;
            }
            score += remove_figure(board, cells);
        }
        std::vector<int> cells = best_figure(board, main_color, true);
        if (cells.empty()) {
            return score;
        }
        score += remove_figure(board, cells);
    }
}

int main() {
    std::cin >> n >> m;
    std::string board;
    for (int r = 0; r < n; r++) {
        std::string row;
        std::cin >> row;
        board += row;
    }
    for (char color : COLORS) {
        if (board.find(color) != std::string::npos) {
            std::cout << color << ": " << play(board, color) << "\n";
        }
    }
}
