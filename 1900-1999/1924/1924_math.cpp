#include <iostream>

int main() {
    int size;
    std::cin >> size;
    int total = size * (size + 1) / 2;
    std::cout << (total % 2 == 0 ? "black" : "grimy") << '\n';
    return 0;
}
