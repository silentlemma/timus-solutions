#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<char> buf(n + 1);
    std::string prev, row;
    // runs ending at each cell of the previous and current row, going
    // down, down-right and down-left
    std::vector<int> down(n), right(n), left(n), down2(n), right2(n), left2(n);
    int best[2] = {0, 0}; // longest runs of s and of S
    for (int i = 0; i < n; i++) {
        scanf("%s", buf.data());
        row = buf.data();
        int across = 0;
        for (int j = 0; j < n; j++) {
            char c = row[j];
            across = j > 0 && row[j - 1] == c ? across + 1 : 1;
            down2[j] = i > 0 && prev[j] == c ? down[j] + 1 : 1;
            right2[j] = i > 0 && j > 0 && prev[j - 1] == c ? right[j - 1] + 1 : 1;
            left2[j] = i > 0 && j + 1 < n && prev[j + 1] == c ? left[j + 1] + 1 : 1;
            int &b = best[c == 'S'];
            b = std::max({b, across, down2[j], right2[j], left2[j]});
        }
        std::swap(down, down2), std::swap(right, right2), std::swap(left, left2);
        prev = row;
    }
    printf("%s\n%d\n",
           best[0] > best[1]   ? "s"
           : best[1] > best[0] ? "S"
                               : "?",
           std::max(best[0], best[1]));
}
