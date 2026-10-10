#include <iostream>
#include <string>

int main() {
    const int SPLIT = 3;
    std::string digits;
    std::cin >> digits;
    // no power of two is divisible by 3, so from a multiple of 3 every move
    // leaves a non-multiple, and from a non-multiple taking 1 or 2 stones
    // leaves a multiple; the remainder is also the smallest such move
    int rest = 0;
    for (char c : digits) {
        rest = (rest + c - '0') % SPLIT;
    }
    if (rest == 0) {
        std::cout << "2\n";
    } else {
        std::cout << "1\n" << rest << "\n";
    }
}
