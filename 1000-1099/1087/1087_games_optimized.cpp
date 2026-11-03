#include <algorithm>
#include <cstdio>

const int MAX_STONES = 10000, MAX_MOVES = 50;
int moves[MAX_MOVES];
unsigned char win[MAX_STONES + 1];

int main() {
    int stones, count;
    if (scanf("%d%d", &stones, &count) != 2)
        return 0;
    for (int i = 0; i < count; i++)
        scanf("%d", &moves[i]);
    std::sort(moves, moves + count);
    count = int(std::unique(moves, moves + count) - moves);
    // Taking the last stone loses, so only strictly smaller moves may win.
    for (int left = 1; left <= stones; left++)
        for (int i = 0; i < count && moves[i] < left; i++)
            if (!win[left - moves[i]]) {
                win[left] = 1;
                break;
            }
    printf("%d\n", win[stones] ? 1 : 2);
}
