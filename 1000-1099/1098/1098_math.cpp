#include <cstdio>
#include <string>

const int STEP = 1999;

int main() {
    std::string text;
    for (int c; (c = getchar()) != EOF;)
        if (c != '\r' && c != '\n')
            text += (char)c;
    // Josephus: with m characters left, the one that stays last sits at
    // (survivor of m - 1) + STEP, counted from where the first deletion was
    int survivor = 0;
    for (int m = 2; m <= (int)text.size(); m++)
        survivor = (survivor + STEP) % m;
    char last = text[survivor];
    puts(last == '?' ? "Yes" : last == ' ' ? "No" : "No comments");
}
