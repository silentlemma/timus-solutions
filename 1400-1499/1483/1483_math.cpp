#include <cstdio>

const int WIN = 3;

int main() {
    int n;
    scanf("%d", &n);
    // every match gives out at least 2 points (a draw) and at most WIN,
    // so the leader has at least the average of all draws and the last team
    // at most the average of all wins; both bounds can be reached
    printf("%d %d\n", n - 1, WIN * (n - 1) / 2);
}
