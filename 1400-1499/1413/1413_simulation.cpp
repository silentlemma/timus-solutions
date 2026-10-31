#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>

const int KEYS = 10;
const double HALF = sqrt(1.0 / 2); // each axis of a diagonal jump
// the numeric keypad: the jump of each key in steps east and north
const int DX[KEYS] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
const int DY[KEYS] = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string keys;
    long long times[KEYS] = {};
    bool stopped = false;
    while (std::cin >> keys) {
        for (char c : keys) {
            if (c == '0')
                stopped = true;
            if (!stopped && c > '0' && c <= '9')
                times[c - '0']++;
        }
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
