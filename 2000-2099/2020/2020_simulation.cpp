#include <iostream>
#include <string>

int solve(const std::string &south, const std::string &north) {
    std::size_t i = 0, j = 0;
    int elapsed = 0;
    while (i < south.size() && j < north.size()) {
        char a = south[i], b = north[j];
        bool go_a = a != 'L' || b == 'L';
        bool go_b = b != 'L' || a == 'L';
        i += go_a;
        j += go_b;
        ++elapsed;
    }
    return elapsed + static_cast<int>(south.size() - i + north.size() - j);
}

int main() {
    std::string south, north;
    std::cin >> south >> north;
    std::cout << solve(south, north) << '\n';
    return 0;
}
