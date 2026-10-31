#include <cstdio>

constexpr int MAX_WORD = 255;

static bool letter(int c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

int main() {
    // a word cannot cross a line, whose statement limit is 255 characters.
    char word[MAX_WORD];
    int length = 0;
    // every run of latin letters is reversed; everything else stays
    for (int c = getchar(); c != EOF; c = getchar()) {
        if (letter(c)) {
            word[length++] = static_cast<char>(c);
        } else {
            while (length > 0)
                putchar(word[--length]);
            putchar(c);
        }
    }
    while (length > 0)
        putchar(word[--length]);
}
