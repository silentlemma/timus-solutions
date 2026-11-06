#include <cstdio>

bool simple(int ch) { return ch == ' ' || (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'); }

int main() {
    int short_limit, long_limit;
    if (std::scanf("%d%d", &short_limit, &long_limit) != 2)
        return 0;
    for (int ch = std::getchar(); ch != EOF && ch != '\n'; ch = std::getchar()) {
    }
    int length = 0, messages = 0;
    bool plain = true;
    for (int ch = std::getchar(); ch != EOF && ch != '\n' && ch != '\r'; ch = std::getchar()) {
        const bool letter = simple(ch);
        if (length == long_limit || (length >= short_limit && (!plain || !letter))) {
            ++messages;
            length = 0;
            plain = true;
        }
        ++length;
        plain &= letter;
    }
    std::printf("%d\n", messages + (length > 0));
}
