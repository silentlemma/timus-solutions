#include <cstdio>
#include <string>
#include <vector>

const int WHITE = 255;
const int HALF = 127; // the carried error always stays within [-127, 127]

int main() {
    int n = 0, m = 0;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> row(m), res(m);
    std::string out;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            if (scanf("%d", &row[j]) != 1)
                return 0;
        // carry the rounding error along the row, in alternate directions so
        // that a window at either side meets short prefixes in half its rows
        int err = 0;
        for (int k = 0; k < m; k++) {
            int j = i % 2 == 0 ? k : m - 1 - k;
            err -= row[j];
            res[j] = 0;
            if (err < -HALF) {
                err += WHITE;
                res[j] = WHITE;
            }
        }
        for (int j = 0; j < m; j++) {
            out += res[j] ? "255" : "0";
            out += j + 1 < m ? ' ' : '\n';
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
