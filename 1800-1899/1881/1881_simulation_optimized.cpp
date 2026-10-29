#include <cstdio>

int main() {
    int height, width, count;
    scanf("%d%d%d", &height, &width, &count);
    int lines = 1;
    int used = -1;
    for (int i = 0; i < count; ++i) {
        int ch;
        do {
            ch = getchar();
        } while (ch <= ' ' && ch != EOF);
        // only the length of a word matters, so the word is never stored
        int length = 0;
        while (ch > ' ') {
            ++length;
            ch = getchar();
        }
        // a word after another one on the line needs a space before it
        if (used + 1 + length > width) {
            ++lines;
            used = -1;
        }
        used += 1 + length;
    }
    printf("%d\n", (lines + height - 1) / height);
}
