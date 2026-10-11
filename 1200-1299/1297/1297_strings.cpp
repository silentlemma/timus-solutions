#include <iostream>
#include <string>

int main() {
    std::string s;
    std::getline(std::cin, s);
    while (!s.empty() && (s.back() == '\r' || s.back() == ' '))
        s.pop_back();
    int n = s.size(), bestStart = 0, bestLen = 0;
    // every letter and every gap between two letters is a centre, 2n - 1 in all, and
    // each is expanded as far as it goes; ties keep the leftmost start
    for (int centre = 0; centre < 2 * n - 1; centre++) {
        int lo = centre / 2, hi = (centre + 1) / 2;
        while (lo >= 0 && hi < n && s[lo] == s[hi]) {
            lo--;
            hi++;
        }
        int length = hi - lo - 1, start = lo + 1;
        if (length > bestLen || (length == bestLen && start < bestStart)) {
            bestStart = start;
            bestLen = length;
        }
    }
    std::cout << s.substr(bestStart, bestLen) << "\n";
    return 0;
}
