#include <cctype>
#include <climits>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const long long NONE = -1; // no term starts here
const int BASE = 10;

struct Parser {
    string s;
    size_t pos = 0;

    bool accept(char c) {
        if (pos < s.size() && s[pos] == c) {
            pos++;
            return true;
        }
        return false;
    }

    // a number, an operation with its arguments, or a bracket
    long long term() {
        if (pos < s.size() && isdigit((unsigned char)s[pos])) {
            long long v = 0;
            while (pos < s.size() && isdigit((unsigned char)s[pos]))
                v = v * BASE + (s[pos++] - '0');
            return v;
        }
        for (char sign : string("+*/"))
            if (accept(sign))
                return fold(sign);
        if (accept('(')) {
            long long x = glue(false);
            accept(')');
            return x;
        }
        return NONE;
    }

    // the arguments of an operation are glued terms split by ';'
    long long fold(char sign) {
        long long a = glue(true);
        while (accept(';')) {
            long long b = glue(true);
            if (sign == '+')
                a += b;
            else if (sign == '*')
                a *= b;
            else
                a = b == 0 ? 0 : a / b;
        }
        return a;
    }

    // terms one after another are glued as decimal strings; inside an
    // operation ';' ends the argument, elsewhere it glues the whole rest,
    // and a missing term counts as 1
    long long glue(bool inside) {
        vector<long long> parts;
        for (long long x = term(); x != NONE || parts.empty(); x = term()) {
            parts.push_back(x);
            if (pos < s.size() && s[pos] == ';') {
                if (inside)
                    break;
                pos++;
                parts.push_back(glue(false));
            }
        }
        string text;
        for (long long x : parts)
            text += to_string(x < 0 ? -x : x);
        // a glued number that does not fit is cut to the largest one
        long long v = 0;
        for (char c : text) {
            if (v > (LLONG_MAX - (c - '0')) / BASE)
                return LLONG_MAX;
            v = v * BASE + (c - '0');
        }
        return v;
    }
};

int main() {
    ios::sync_with_stdio(false);
    string line;
    for (int i = 1; getline(cin, line); i++) {
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        Parser p;
        p.s = line;
        printf("Expression %d evaluates to: %lld\n", i, p.glue(false));
    }
}
