#include <iostream>
#include <string>

const int MAX_BASE = 36;

int main() {
    std::string s;
    std::cin >> s;
    int total = 0, top = 1;
    for (char c : s) {
        int d = c >= 'A' ? c - 'A' + 10 : c - '0';
        total += d;
        if (d > top)
            top = d;
    }
    // base k is 1 modulo k - 1, so the number is congruent to its digit sum
    for (int k = top + 1; k <= MAX_BASE; k++) {
        if (total % (k - 1) == 0) {
            std::cout << k << "\n";
            return 0;
        }
    }
    std::cout << "No solution.\n";
}
