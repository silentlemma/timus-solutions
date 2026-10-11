#include <cstdio>
#include <vector>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<std::vector<int>> first(n, std::vector<int>(m)), second = first;
    for (auto &row : first) {
        for (int &v : row) {
            scanf("%d", &v);
        }
    }
    int label = 0;
    // cover every 2 x 2 block with two bricks: lying flat unless a brick of
    // the first layer fills its top or bottom row, and then standing, which
    // no first-layer brick can match, as that brick holds a cell of each column
    for (int i = 0; i < n; i += 2) {
        for (int j = 0; j < m; j += 2) {
            bool flat = first[i][j] != first[i][j + 1] && first[i + 1][j] != first[i + 1][j + 1];
            int a = ++label, b = ++label;
            if (flat) {
                second[i][j] = second[i][j + 1] = a;
                second[i + 1][j] = second[i + 1][j + 1] = b;
            } else {
                second[i][j] = second[i + 1][j] = a;
                second[i][j + 1] = second[i + 1][j + 1] = b;
            }
        }
    }
    for (auto &row : second) {
        for (int j = 0; j < m; j++) {
            printf("%d%c", row[j], j + 1 < m ? ' ' : '\n');
        }
    }
}
