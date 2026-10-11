#include <algorithm>
#include <cstdio>
#include <vector>

const int MANY = 2;

int main() {
    int weight, n;
    scanf("%d %d", &weight, &n);
    std::vector<int> card(n + 1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &card[i]);
    // ways[i][s]: how many sets of the first i cards weigh s, counted up to 2
    std::vector<std::vector<unsigned char>> ways(n + 1, std::vector<unsigned char>(weight + 1, 0));
    ways[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        ways[i] = ways[i - 1];
        for (int s = card[i]; s <= weight; s++)
            ways[i][s] = std::min(MANY, ways[i][s] + ways[i - 1][s - card[i]]);
    }
    if (ways[n][weight] == 0) {
        puts("0");
        return 0;
    }
    if (ways[n][weight] == MANY) {
        puts("-1");
        return 0;
    }
    // the only set: card i is in it exactly when the rest cannot be made
    // from the cards before it
    std::vector<bool> missing(n + 1);
    for (int i = n, s = weight; i >= 1; i--) {
        if (ways[i - 1][s] == 1)
            missing[i] = true;
        else
            s -= card[i];
    }
    bool first = true;
    for (int i = 1; i <= n; i++)
        if (missing[i]) {
            printf(first ? "%d" : " %d", i);
            first = false;
        }
    printf("\n");
}
