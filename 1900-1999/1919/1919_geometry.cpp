#include <iostream>

bool fits(long long first, long long second, long long height, long long circumference) {
    if (first > circumference) {
        return false;
    }
    if (second <= height) {
        return true;
    }
    long long residual = height * circumference - first * second;
    if (residual < 0) {
        return false;
    }
    return static_cast<__int128>(residual) * residual >=
           static_cast<__int128>(first) * first * (circumference * circumference - first * first);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long width, height;
    int count;
    std::cin >> width >> height >> count;
    while (count--) {
        long long cylinder_height, circumference;
        std::cin >> cylinder_height >> circumference;
        bool possible = fits(width, height, cylinder_height, circumference) ||
                        fits(height, width, cylinder_height, circumference);
        std::cout << (possible ? "Block the hole\n" : "Too small\n");
    }
    return 0;
}
