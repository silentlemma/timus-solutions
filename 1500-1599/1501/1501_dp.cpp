#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

const int TEXT = 1002;

int main() {
    int n;
    static char a[TEXT], b[TEXT];
    scanf("%d %s %s", &n, a, b);
    // after taking i cards of the first pile and j of the second, the red and
    // the black piles differ by d1[i] + d2[j], where d = 2 * reds - taken
    vector<int> d1(n + 1, 0), d2(n + 1, 0);
    for (int i = 0; i < n; i++) {
        d1[i + 1] = d1[i] + (a[i] == '1' ? 1 : -1);
        d2[i + 1] = d2[i] + (b[i] == '1' ? 1 : -1);
    }
    // reach[i][j]: the state is allowed and comes from (i - 1, j) or (i, j - 1)
    vector<vector<char>> reach(n + 1, vector<char>(n + 1, 0));
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= n; j++) {
            if (abs(d1[i] + d2[j]) > 1)
                continue;
            reach[i][j] =
                (i == 0 && j == 0) || (i > 0 && reach[i - 1][j]) || (j > 0 && reach[i][j - 1]);
        }
    if (!reach[n][n]) {
        puts("Impossible");
        return 0;
    }
    // walk back from (n, n): a step left took a card of the second pile
    string moves;
    for (int i = n, j = n; i || j;) {
        if (j && reach[i][j - 1]) {
            moves += '2';
            j--;
        } else {
            moves += '1';
            i--;
        }
    }
    reverse(moves.begin(), moves.end());
    puts(moves.c_str());
}
