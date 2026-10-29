#include <cstdio>

int main() {
    constexpr int byteValues = 256;
    // the characters of each key in the order of presses; the space has a key of
    // its own
    const char *keys[] = {"abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " "};
    // the number of presses for every byte, looked up once per character
    int presses[byteValues] = {};
    for (const char *key : keys)
        for (int i = 0; key[i] != '\0'; ++i)
            presses[static_cast<unsigned char>(key[i])] = i + 1;
    int total = 0;
    // the whole first line, spaces included; anything else costs nothing
    for (int c; (c = getchar()) != EOF && c != '\n';)
        total += presses[c];
    printf("%d\n", total);
}
