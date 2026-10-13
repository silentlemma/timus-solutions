#include <iostream>
#include <string>

const int SHIFT = 5; // added to the first letter
const int LETTERS = 26;

int main() {
    std::string word;
    std::cin >> word;
    // each code is the previous code plus the letter, modulo 26: take differences
    int prev = SHIFT;
    for (char &ch : word) {
        int code = ch - 'a';
        ch = char('a' + ((code - prev) % LETTERS + LETTERS) % LETTERS);
        prev = code;
    }
    std::cout << word << std::endl;
}
