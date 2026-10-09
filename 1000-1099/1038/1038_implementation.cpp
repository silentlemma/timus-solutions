#include <cctype>
#include <cstdio>

int main() {
    int errors = 0;
    // a new sentence waits for its first letter; in_word: the previous character
    // was a letter
    bool new_sentence = true, in_word = false;
    int c;
    while ((c = getchar()) != EOF) {
        if (isalpha(c)) {
            if (islower(c) && new_sentence)
                errors++;
            if (isupper(c) && in_word)
                errors++;
            new_sentence = false;
            in_word = true;
        } else {
            in_word = false;
            if (c == '.' || c == '?' || c == '!')
                new_sentence = true;
        }
    }
    printf("%d\n", errors);
}
