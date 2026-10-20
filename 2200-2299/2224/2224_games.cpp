#include <iostream>

bool blue_wins(long long n, int r1, long long c1, int r2, long long c2) {
    // Reflect the board so Blue starts to the left of Red.
    if (c1 > c2) {
        c1 = n + 1 - c1;
        c2 = n + 1 - c2;
    }
    const long long gap = c2 - c1;
    const long long left = c1 - 1;
    const long long right = n - c2;
    if (r1 == r2) {
        return left > right || (left == right && gap % 2 == 0);
    }
    if (gap == 0 || left == right) {
        return false;
    }
    if (gap == 1) {
        return true;
    }
    // A one-column tail advantage makes the gap parity decisive.
    if (left == right + 1 || right == left + 1) {
        return gap % 2 == 1;
    }
    return left > right;
}

int main() {
    long long n, c1, c2;
    int r1, r2;
    std::cin >> n >> r1 >> c1 >> r2 >> c2;
    std::cout << (blue_wins(n, r1, c1, r2, c2) ? "Blue" : "Red") << '\n';
}
