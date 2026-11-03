#include <cstdint>
#include <cstdio>

const int MAX_LENGTH = 75000;
const std::uint32_t CUT = 1u << 31;
char word[MAX_LENGTH + 1], text[MAX_LENGTH + 1];
std::uint32_t prefix[MAX_LENGTH], matched[MAX_LENGTH + 1];

int main() {
    if (scanf("%75000s%75000s", word, text) != 2)
        return 0;
    int size = 0, n = 0;
    while (word[size])
        size++;
    while (text[n])
        n++;
    for (int i = 1; i < size; i++) {
        std::uint32_t k = prefix[i - 1];
        while (k && word[k] != word[i])
            k = prefix[k - 1];
        if (word[k] == word[i])
            k++;
        prefix[i] = k;
    }
    std::uint32_t k = 0;
    for (int end = 1; end <= n; end++) {
        while (k && (k == static_cast<std::uint32_t>(size) || word[k] != text[end - 1]))
            k = prefix[k - 1];
        if (word[k] == text[end - 1])
            k++;
        matched[end] = k;
    }
    for (int end = n; end;) {
        std::uint32_t length = matched[end];
        if (!length) {
            puts("Yes");
            return 0;
        }
        // Lengths use at most 17 bits; preserve selected cuts in the high bit.
        matched[end] |= CUT;
        end -= length;
    }
    fputs("No\n", stdout);
    int begin = 0;
    for (int end = 1; end <= n; end++)
        if (matched[end] & CUT) {
            if (begin)
                putchar(' ');
            fwrite(text + begin, 1, end - begin, stdout);
            begin = end;
        }
    putchar('\n');
    return 0;
}
