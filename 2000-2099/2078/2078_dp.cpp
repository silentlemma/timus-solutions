#include <algorithm>
#include <climits>
#include <cstdio>

using namespace std;

constexpr int FRAMES = 10;
constexpr int PINS = 10;
constexpr int ROLL = PINS + 1;  // a roll knocks down 0 to 10 pins

// low[x][y], high[x][y]: the least and the most points of the frames from the
// current one on, when the rolls from the current frame on start with x and y
int low[ROLL][ROLL], high[ROLL][ROLL], nextLow[ROLL][ROLL], nextHigh[ROLL][ROLL];

void reset(int lo[ROLL][ROLL], int hi[ROLL][ROLL]) {
    for (int x = 0; x < ROLL; x++)
        for (int y = 0; y < ROLL; y++) lo[x][y] = INT_MAX, hi[x][y] = INT_MIN;
}

void put(int lo[ROLL][ROLL], int hi[ROLL][ROLL], int x, int y, int a, int b) {
    lo[x][y] = min(lo[x][y], a);
    hi[x][y] = max(hi[x][y], b);
}

int main() {
    int total[FRAMES];
    for (int& t : total) scanf("%d", &t);
    reset(low, high);
    // rolls of the last frame: two, and a third one after a strike or a spare
    int last = total[FRAMES - 1];
    for (int r1 = 0; r1 <= PINS; r1++)
        for (int r2 = 0; r2 <= (r1 == PINS ? PINS : PINS - r1); r2++) {
            if (r1 < PINS && r1 + r2 < PINS) {
                if (r1 + r2 == last) put(low, high, r1, r2, last, last);
                continue;
            }
            bool fresh = r1 < PINS || r2 == PINS;
            int r3 = last - r1 - r2;
            if (r3 >= 0 && r3 <= (fresh ? PINS : PINS - r2)) put(low, high, r1, r2, last, last);
        }
    for (int f = FRAMES - 2; f >= 0; f--) {
        int t = total[f];
        reset(nextLow, nextHigh);
        for (int x = 0; x < ROLL; x++)
            for (int y = 0; y < ROLL; y++) {
                if (low[x][y] == INT_MAX) continue;
                int a = low[x][y] + t, b = high[x][y] + t;
                if (t < PINS) {
                    for (int r1 = 0; r1 <= t; r1++) put(nextLow, nextHigh, r1, t - r1, a, b);
                    continue;
                }
                // a strike takes the next two rolls, a spare the next one
                put(nextLow, nextHigh, PINS, x, a + x + y, b + x + y);
                for (int r1 = 0; r1 < PINS; r1++)
                    put(nextLow, nextHigh, r1, PINS - r1, a + x, b + x);
            }
        copy(&nextLow[0][0], &nextLow[0][0] + ROLL * ROLL, &low[0][0]);
        copy(&nextHigh[0][0], &nextHigh[0][0] + ROLL * ROLL, &high[0][0]);
    }
    int lo = INT_MAX, hi = INT_MIN;
    for (int x = 0; x < ROLL; x++)
        for (int y = 0; y < ROLL; y++) lo = min(lo, low[x][y]), hi = max(hi, high[x][y]);
    printf("%d %d\n", lo, hi);
}
