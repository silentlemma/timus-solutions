#include <cstdio>

const int MAX_N = 200;
// state i (1 to MAX_N+1) stands on cell i of the minuses; state SEEK+d
// still has to move d cells to the left before reaching the survivor
const int SEEK = 300;
// states that cross the minuses to the right of the survivor, walk back
// over it, cross those to its left and return to it
const int RIGHT = 600, BACK = 601, LEFT = 602, RETURNED = 603;
const int MAX_RULES = 1000;
const int ROW = 32;

char rules[MAX_RULES][ROW];
int count = 0;

void rule(int state, char read, int next, char write, char move) {
    snprintf(rules[count++], ROW, "%d %c %d %c %c", state, read, next, write, move);
}

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    // survivor = 0-based position of the minus that stays out of n, by the
    // Josephus recurrence
    int survivor = 0;
    for (int n = 1; n <= MAX_N; n++) {
        survivor = (survivor + k) % n;
        rule(n, '-', n + 1, '-', '>');
        // the head stands on the # after n minuses and moves onto cell n
        rule(n + 1, '#', SEEK + n - 1 - survivor, '#', '<');
    }
    for (int d = 1; d < MAX_N; d++)
        rule(SEEK + d, '-', SEEK + d - 1, '-', '<');
    rule(SEEK, '-', RIGHT, '-', '>');
    rule(RIGHT, '-', RIGHT, '+', '>');
    rule(RIGHT, '+', RIGHT, '+', '>');
    rule(RIGHT, '#', BACK, '#', '<');
    rule(BACK, '+', BACK, '+', '<');
    rule(BACK, '-', LEFT, '-', '<');
    rule(LEFT, '-', LEFT, '+', '<');
    rule(LEFT, '+', LEFT, '+', '<');
    rule(LEFT, '#', RETURNED, '#', '>');
    rule(RETURNED, '+', RETURNED, '+', '>');
    printf("%d\n", count);
    for (int i = 0; i < count; i++)
        printf("%s\n", rules[i]);
}
