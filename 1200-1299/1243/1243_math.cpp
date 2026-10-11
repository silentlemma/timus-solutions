#include <iostream>
#include <string>

const int DWARFS = 7;

int main() {
    std::string digits;
    std::cin >> digits;
    // the number has up to 51 digits, so take it modulo 7 digit by digit
    int rest = 0;
    for (char d : digits)
        rest = (rest * 10 + (d - '0')) % DWARFS;
    std::cout << rest << "\n";
}
