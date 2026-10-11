#include <algorithm>
#include <cstdio>
#include <string>

static bool letter(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

int main() {
    std::string text;
    for (int c = getchar(); c != EOF; c = getchar()) {
        text += (char)c;
    }
    // every run of Latin letters is reversed in place; everything else stays
    for (size_t i = 0; i < text.size(); i++) {
        size_t j = i;
        while (j < text.size() && letter(text[j])) {
            j++;
        }
        std::reverse(text.begin() + i, text.begin() + j);
        i = std::max(i, j);
    }
    fwrite(text.data(), 1, text.size(), stdout);
}
