#include <cstdio>

const int LETTERS = 26;

// every occurrence of a spell starts with an occurrence of its first
// letter, so a most frequent single letter is a strongest spell
int main() {
    int count[LETTERS] = {};
    int best = 0;
    int c;
    // the letters are counted as they are read; the string is never stored
    while ((c = std::getchar()) != EOF) {
        if (c < 'a' || c > 'z')
            continue;
        count[c - 'a']++;
        if (count[c - 'a'] > count[best])
            best = c - 'a';
    }
    std::putchar('a' + best);
    std::putchar('\n');
}
