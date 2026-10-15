#include <cstdio>

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 0;
    // every break adds one piece, so the game always lasts m * n - 1 moves
    puts((m * n - 1) % 2 ? "[:=[first]" : "[second]=:]");
}
