#include <cstdio>

// contests played by players 0 to 13, counted from the story
const int CONTESTS[] = {5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1};

int main() {
    int player;
    if (scanf("%d", &player) != 1) return 0;
    printf("%d\n", CONTESTS[player]);
    return 0;
}
