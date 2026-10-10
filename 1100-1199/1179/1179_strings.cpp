#include <cstdio>

// anything that is not a digit acts like a digit too large for every base
const int WALL = 36, SMALLEST = 2;

int value(int ch) {
    if (ch >= '0' && ch <= '9') {
        return ch - '0';
    }
    if (ch >= 'A' && ch <= 'Z') {
        return ch - 'A' + 10;
    }
    return WALL;
}

int main() {
    // a number in base k starts at every digit below k whose left neighbour
    // is k or more, so each neighbouring pair (left, right) with right < left
    // starts a number in the bases right + 1 .. left
    static long long pairs[WALL + 1][WALL + 1];
    int left = WALL, ch;
    while ((ch = getchar()) != EOF) {
        int right = value(ch);
        pairs[left][right]++;
        left = right;
    }
    long long count[WALL + 2] = {};
    for (int l = 1; l <= WALL; l++) {
        for (int r = 0; r < l; r++) {
            count[r + 1 > SMALLEST ? r + 1 : SMALLEST] += pairs[l][r];
            count[l + 1] -= pairs[l][r];
        }
    }
    long long best = -1, running = 0;
    int bestK = SMALLEST;
    for (int k = 0; k <= WALL; k++) {
        running += count[k];
        if (k >= SMALLEST && running > best) {
            best = running;
            bestK = k;
        }
    }
    printf("%d %lld\n", bestK, best);
}
