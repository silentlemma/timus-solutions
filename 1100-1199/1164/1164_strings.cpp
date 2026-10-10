#include <iostream>
#include <string>

int main() {
    const int LETTERS = 26;
    int n, m, p;
    std::cin >> n >> m >> p;
    // the words take their letters out of the grid one cell each, so what is
    // left does not depend on where they lie
    int left[LETTERS] = {};
    std::string s;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        for (char c : s) {
            left[c - 'A']++;
        }
    }
    for (int i = 0; i < p; i++) {
        std::cin >> s;
        for (char c : s) {
            left[c - 'A']--;
        }
    }
    std::string answer;
    for (int c = 0; c < LETTERS; c++) {
        answer += std::string(left[c], 'A' + c);
    }
    std::cout << answer << "\n";
}
