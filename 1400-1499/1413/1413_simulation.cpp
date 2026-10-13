#include <cmath>
#include <cstdio>
#include <string>

const int KEYS = 10;
const int BUFFER = 1 << 16;
const double HALF = sqrt(0.5); // each axis of a diagonal jump
// the numeric keypad: the jump of each key in steps east and north
const int DX[KEYS] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
const int DY[KEYS] = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};

int main() {
    std::string keys;
    char buffer[BUFFER];
    for (size_t got; (got = fread(buffer, 1, sizeof buffer, stdin)) > 0;)
        keys.append(buffer, got);
    long long times[KEYS] = {};
    for (char c : keys) {
        if (c == '0')
            break;
        if (c > '0' && c <= '9')
            times[c - '0']++;
    }
    // straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
    long long sx = 0, sy = 0, dx = 0, dy = 0;
    for (int k = 0; k < KEYS; k++)
        if (DX[k] && DY[k]) {
            dx += DX[k] * times[k];
            dy += DY[k] * times[k];
        } else {
            sx += DX[k] * times[k];
            sy += DY[k] * times[k];
        }
    double x = sx + dx * HALF, y = sy + dy * HALF;
    printf("%.10f %.10f\n", x, y);
}
