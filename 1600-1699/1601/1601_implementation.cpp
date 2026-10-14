#include <cstdio>
#include <cstring>

const char *ENDS = ".!?"; // marks that end a sentence

int main() {
    bool start = true; // the next letter opens a sentence
    int c;
    while ((c = getchar()) != EOF) {
        if (c >= 'A' && c <= 'Z') {
            if (!start)
                c += 'a' - 'A';
            start = false;
        } else if (c != 0 && strchr(ENDS, c)) {
            start = true;
        }
        putchar(c);
    }
}
