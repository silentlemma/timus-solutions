#include <iostream>
#include <string>
#include <vector>

// the line has at most 10^5 pieces of each length, fewer than the 9 * 10^5
// numbers of six digits, so the answer has at most six digits
const int DIGITS = 6, LIMIT = 1000000;

int main() {
    std::string s;
    std::cin >> s;
    std::vector<bool> seen(LIMIT + 1, false);
    int n = s.size();
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') continue;
        int value = 0;
        for (int j = i; j < n && j < i + DIGITS; j++) {
            value = value * 10 + (s[j] - '0');
            seen[value] = true;
        }
    }
    int answer = 1;
    while (seen[answer]) answer++;
    std::cout << answer << "\n";
    return 0;
}
