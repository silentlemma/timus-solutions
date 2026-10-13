#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int ROW = 1002;

int n;
vector<string> grid;

// the black piece slides by (di, dj) when no white cell lies on that side
// of a black one in the same column or row
bool slides(int di, int dj) {
    for (int k = 0; k < n; k++) {
        bool seenWhite = false;
        for (int t = 0; t < n; t++) {
            // walk the line from the side the piece moves towards
            int step = (di + dj > 0) ? n - 1 - t : t;
            int i = di != 0 ? step : k, j = di != 0 ? k : step;
            if (grid[i][j] == '0')
                seenWhite = true;
            else if (seenWhite)
                return false;
        }
    }
    return true;
}

int main() {
    scanf("%d", &n);
    grid.resize(n);
    static char row[ROW];
    for (auto &line : grid) {
        scanf("%s", row);
        line = row;
    }
    // a sliding direction for either piece is the opposite one for the
    // other; a diagonal slide works only if both of its axis slides do, so
    // trying the four axis directions for the black piece is enough
    bool yes = slides(-1, 0) || slides(1, 0) || slides(0, -1) || slides(0, 1);
    puts(yes ? "Yes" : "No");
}
