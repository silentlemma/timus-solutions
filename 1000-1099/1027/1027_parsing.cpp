#include <cstdio>
#include <cstring>
#include <string>

// characters allowed inside an arithmetic expression besides the brackets
const char *const EXPRESSION = "=+-*/0123456789\r\n";

bool valid(const std::string &s) {
    int depth = 0;
    for (size_t i = 0; i < s.size(); i++) {
        if (s.compare(i, 2, "(*") == 0) {
            // a comment ends at the first *) after its opening pair
            size_t end = s.find("*)", i + 2);
            if (end == std::string::npos)
                return false;
            i = end + 1;
        } else if (s[i] == '(') {
            depth++;
        } else if (s[i] == ')') {
            if (depth == 0)
                return false;
            depth--;
        } else if (depth > 0 && !strchr(EXPRESSION, s[i])) {
            return false;
        }
    }
    return depth == 0;
}

int main() {
    std::string text;
    for (int c; (c = getchar()) != EOF;)
        text += (char)c;
    puts(valid(text) ? "YES" : "NO");
}
