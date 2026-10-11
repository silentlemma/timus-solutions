#include <iostream>
#include <string>

const int ONE_DIGIT = 4; // floors 1 to 5 show every indicator lit and unlit

const int SHORT = 5; // blocks of the second digit: 6 through 9, 0 to 2
const int LONG = 7;  // blocks of the second digit: 2 to 9, 0

const int LOW_TOP = 3; // a leading digit up to this needs blank, 1, 2 on top
const int WIDE = 3;    // blocks of the leading digit otherwise: blank through 4

int main() {
    std::string n;
    std::cin >> n;
    int digits = (int)n.size();
    if (digits == 1) {
        std::cout << ONE_DIGIT << "\n";
        return 0;
    }
    int top = n[0] - '0', second = n[1] - '0';
    int lead = 0, zeros = 0;
    if (top == 1) {
        lead = second >= 2 ? SHORT : LONG;
        zeros = digits - 2;
    } else {
        lead = top <= LOW_TOP ? 1 : WIDE;
        zeros = digits - 1;
    }
    // lead * 10^zeros + 1, written out
    if (zeros == 0)
        std::cout << lead + 1 << "\n";
    else
        std::cout << lead << std::string(zeros - 1, '0') << "1\n";
    return 0;
}
