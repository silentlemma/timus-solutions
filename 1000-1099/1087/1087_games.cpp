#include <cstdio>
#include <vector>

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> moves(m);
    for (int &k : moves)
        scanf("%d", &k);
    // win[x]: the player to move with x stones left wins; with none left the
    // other player has just taken the last stone and lost
    std::vector<bool> win(n + 1, false);
    win[0] = true;
    for (int x = 1; x <= n; x++)
        for (int k : moves)
            if (k <= x && !win[x - k])
                win[x] = true;
    printf("%d\n", win[n] ? 1 : 2);
}
