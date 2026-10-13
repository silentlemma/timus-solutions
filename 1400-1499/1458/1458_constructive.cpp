#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<string> grid(n);
    vector<char> line(n + 1);
    for (auto &row : grid) {
        scanf("%s", line.data());
        row = line.data();
    }
    // pressing every cell of row a and column b turns only (a, b) when N is
    // even, so (i, j) is pressed when its row, its column and itself add up odd
    vector<int> row(n, 0), col(n, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] == 'B') { // the soldiers to turn, for an all-W parade
                row[i] ^= 1;
                col[j] ^= 1;
            }
    long long total = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            total += row[i] ^ col[j] ^ (grid[i][j] == 'B');
    // an all-B parade needs exactly the other cells
    int flip = 2 * total > (long long)n * n ? 1 : 0;
    if (flip)
        total = (long long)n * n - total;
    string out = to_string(total) + "\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if ((row[i] ^ col[j] ^ (grid[i][j] == 'B')) != flip)
                out += to_string(i + 1) + " " + to_string(j + 1) + "\n";
    fputs(out.c_str(), stdout);
}
