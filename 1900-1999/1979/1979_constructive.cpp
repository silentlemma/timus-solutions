#include <iostream>

constexpr int FACE_COUNT = 6;
constexpr int HALF_FACES = 3;
constexpr int BAND_COUNT = 3;
constexpr int BELT_FACES = 4;

int label(int n, int band, int row, int col) {
    int area = n * n;
    int complement = FACE_COUNT * area + 1;
    if (band == 0)
        return 2 * area + row * n + col + 1;
    if (band == 2)
        return complement - (HALF_FACES * area - row * n - n + col + 1);
    int face = col / n;
    col %= n;
    if (face < 2)
        return face * area + row * n + col + 1;
    return complement - ((face - 2) * area + row * n + n - col);
}

void writeCube(int n, std::ostream &out) {
    for (int band = 0; band < BAND_COUNT; ++band) {
        int width = band == 1 ? BELT_FACES * n : n;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < width; ++col) {
                if (col)
                    out << ' ';
                out << label(n, band, row, col);
            }
            out << '\n';
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (std::cin >> n)
        writeCube(n, std::cout);
}
