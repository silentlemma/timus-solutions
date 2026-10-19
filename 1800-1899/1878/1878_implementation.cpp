#include <algorithm>
#include <cstdio>

const int SIDE = 4;
const int TURNS = 4;
const int HALF = SIDE / 2;
// position of each quadrant (top left, top right, bottom left, bottom right)
// in the order a quarter turn moves a square through them
const int RING[2][2] = {{0, 1}, {TURNS - 1, 2}};

int main() {
    int count[TURNS] = {0};
    for (int r = 0; r < SIDE; r++) {
        for (int c = 0; c < SIDE; c++) {
            int colour;
            if (scanf("%d", &colour) != 1) return 0;
            if (colour == 1) count[RING[r / HALF][c / HALF]]++;
        }
    }
    // every layer holds one square of each colour, one per quadrant; the
    // cube is solved when the colour 1 squares of all layers share a quadrant
    int best = SIDE * TURNS;
    for (int t = 0; t < TURNS; t++) {
        int moves = 0;
        for (int p = 0; p < TURNS; p++) {
            int d = (p - t + TURNS) % TURNS;
            moves += count[p] * std::min(d, TURNS - d);
        }
        best = std::min(best, moves);
    }
    printf("%d\n", best);
    return 0;
}
