#include <cstdio>
#include <cstring>

constexpr int MAX_LENGTH = 10000;
// latin letters occupy one byte; the extra byte terminates the input word.
char word[MAX_LENGTH + 1];
// a prefix length is at most 9999, so unsigned short holds every entry.
unsigned short border[MAX_LENGTH];

int main() {
    scanf("%10000s", word);
    int n = static_cast<int>(strlen(word));
    // build the prefix table of the reversed word without storing that copy.
    for (int i = 1; i < n; i++) {
        int k = border[i - 1];
        while (k > 0 && word[n - 1 - i] != word[n - 1 - k])
            k = border[k - 1];
        if (word[n - 1 - i] == word[n - 1 - k])
            k++;
        border[i] = static_cast<unsigned short>(k);
    }
    int longest = 0;
    // omit the first letter so even a palindrome receives a nonempty addition.
    for (int i = 1; i < n; i++) {
        while (longest > 0 && word[i] != word[n - 1 - longest])
            longest = border[longest - 1];
        if (word[i] == word[n - 1 - longest])
            longest++;
    }
    fputs(word, stdout);
    for (int i = n - longest - 1; i >= 0; i--)
        putchar(word[i]);
    putchar('\n');
}
