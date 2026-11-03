#include <algorithm>
#include <cstdio>
#include <cstring>

const int MAX_LENGTH = 5000;
char text[MAX_LENGTH + 1];
const char *suffixes[MAX_LENGTH];

int main() {
    if (scanf("%5000s", text) != 1)
        return 0;
    int size = std::strlen(text);
    for (int i = 0; i < size; i++)
        suffixes[i] = text + i;
    // Every suffix shares the original terminating zero; no suffix is copied.
    std::sort(suffixes, suffixes + size,
              [](const char *a, const char *b) { return std::strcmp(a, b) < 0; });
    int answer = size * (size + 1) / 2;
    for (int i = 1; i < size; i++) {
        int common = 0;
        while (suffixes[i - 1][common] && suffixes[i - 1][common] == suffixes[i][common])
            common++;
        answer -= common;
    }
    printf("%d\n", answer);
}
