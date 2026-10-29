#include <cstdio>

const int MAX_ENTRIES = 1000;
const int WORD_LENGTH = 2;

int main() {
    int count;
    if (scanf("%d", &count) != 1)
        return 0;
    // every entry is two letters: a fixed array of short C strings
    char words[MAX_ENTRIES][WORD_LENGTH + 1];
    for (int i = 0; i < count; ++i)
        scanf("%2s", words[i]);
    char letter;
    scanf(" %c", &letter);
    // the dictionary order is kept, repeated entries are printed every time
    for (int i = 0; i < count; ++i)
        if (words[i][0] == letter)
            puts(words[i]);
}
