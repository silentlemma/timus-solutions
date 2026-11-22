#include <cmath>
#include <cstdio>

constexpr int KEY_COUNT = 9;

int main() {
    const int dx[10] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
    const int dy[10] = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};
    long long times[10] = {};
    constexpr int BUFFER_SIZE = 8192;
    char buffer[BUFFER_SIZE];
    bool ended = false;
    for (size_t size; !ended && (size = fread(buffer, 1, sizeof buffer, stdin)) != 0;)
        for (size_t i = 0; i < size; ++i) {
            int c = buffer[i];
            if (c == '0') {
                ended = true;
                break;
            }
            if (c >= '1' && c <= '9')
                ++times[c - '0'];
        }
    long long straightX = 0, straightY = 0, diagonalX = 0, diagonalY = 0;
    for (int key = 1; key <= KEY_COUNT; ++key) {
        if (dx[key] && dy[key]) {
            diagonalX += dx[key] * times[key];
            diagonalY += dy[key] * times[key];
        } else {
            straightX += dx[key] * times[key];
            straightY += dy[key] * times[key];
        }
    }
    const double half = std::sqrt(0.5);
    printf("%.10f %.10f\n", straightX + diagonalX * half, straightY + diagonalY * half);
}
