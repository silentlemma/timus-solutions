#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

const int ALPHABET = 26;

int main() {
    int n;
    std::string word;
    std::cin >> n >> word;
    int size = word.size();
    // placing the remaining letter whose next occurrence is farthest moves at
    // least k places when k letters remain, so a universal word needs
    // n + (n - 1) + ... + 1 letters
    if (size < n * (n + 1) / 2) {
        printf("NO\n");
        return 0;
    }
    int fail = size + 1;
    // after[c][p]: the place just after the first c at or after place p
    std::vector<std::vector<short>> after(ALPHABET, std::vector<short>(size + 2, fail));
    for (int c = 0; c < ALPHABET; c++) {
        for (int p = size - 1; p >= 0; p--) {
            after[c][p] = word[p] - 'a' == c ? p + 1 : after[c][p + 1];
        }
    }
    // reach[mask]: how far the greedy embedding gets for the worst order of
    // the letters in mask; submasks come first in increasing order, and one
    // failing mask makes the whole set fail, so the table stops there
    std::vector<short> reach = {0};
    for (long long mask = 1; mask < (1LL << n); mask++) {
        short best = 0;
        for (long long rest = mask; rest; rest &= rest - 1) {
            int letter = __builtin_ctzll(rest);
            short pos = after[letter][reach[mask ^ (1LL << letter)]];
            if (pos > best) {
                best = pos;
            }
        }
        if (best == fail) {
            printf("NO\n");
            return 0;
        }
        reach.push_back(best);
    }
    printf("YES\n");
}
