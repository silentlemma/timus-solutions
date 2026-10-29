#include <cstdio>

const int MAX_LENGTH = 1000;

int main() {
    // the at most 1000 letters go into a fixed array, and the answer is written
    // straight from it
    char s[MAX_LENGTH];
    int length = 0;
    int ch;
    while ((ch = std::getchar()) != EOF && ch <= ' ') {
    }
    while (ch > ' ' && length < MAX_LENGTH) {
        s[length++] = static_cast<char>(ch);
        ch = std::getchar();
    }
    int n = length, bestStart = 0, bestLen = 0;
    // every letter and every gap between two letters is a centre, 2n - 1 in all, and
    // each is expanded as far as it goes; ties keep the leftmost start
    for (int centre = 0; centre < 2 * n - 1; centre++) {
        int lo = centre / 2, hi = (centre + 1) / 2;
        while (lo >= 0 && hi < n && s[lo] == s[hi]) {
            lo--;
            hi++;
        }
        int span = hi - lo - 1, start = lo + 1;
        if (span > bestLen || (span == bestLen && start < bestStart)) {
            bestStart = start;
            bestLen = span;
        }
    }
    std::fwrite(s + bestStart, 1, bestLen, stdout);
    std::putchar('\n');
}
