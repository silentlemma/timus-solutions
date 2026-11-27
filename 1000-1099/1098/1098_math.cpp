#include <cstdio>
#include <string>

const int STEP = 1999;

int main() {
    std::string text;
    for (int c; (c = getchar()) != EOF;)
        if (c != '\r' && c != '\n')
            text += (char)c;
    // Josephus: J(m) is zero-based from the original counting start.
    // After the first deletion, counting restarts STEP positions from that start.
    // Thus J(m) = (J(m - 1) + STEP) % m, with J(1) = 0.
    int survivor = 0;
    for (int m = 2; m <= (int)text.size(); m++)
        survivor = (survivor + STEP) % m;
    char last = text[survivor];
    puts(last == '?' ? "Yes" : last == ' ' ? "No" : "No comments");
}
