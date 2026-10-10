#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

typedef std::string Bytes;
const int BYTES = 256;

// the text between quotes starting at p, with doubled quotes undone; p moves
// past the closing quote
Bytes quoted(const Bytes &line, size_t &p) {
    Bytes out;
    for (p++; p < line.size(); p++) {
        if (line[p] == '\'') {
            if (p + 1 < line.size() && line[p + 1] == '\'') {
                out += '\'';
                p++;
                continue;
            }
            p++;
            break;
        }
        out += line[p];
    }
    return out;
}

bool like(const Bytes &text, const Bytes &pattern) {
    size_t n = text.size(), m = pattern.size();
    // reach[i]: the pattern so far can match exactly the first i bytes
    std::vector<bool> reach(n + 1, false), next(n + 1);
    reach[0] = true;
    for (size_t j = 0; j < m;) {
        unsigned char c = pattern[j];
        next.assign(n + 1, false);
        if (c == '%') {
            bool seen = false;
            for (size_t i = 0; i <= n; i++) {
                seen = seen || reach[i];
                next[i] = seen;
            }
            j++;
        } else if (c == '[') {
            // a set of bytes, negated after ^, with ranges a-b unless b is ]
            size_t k = j + 1;
            bool negated = k < m && pattern[k] == '^';
            k += negated;
            std::vector<bool> accepted(BYTES, false);
            while (k < m && pattern[k] != ']') {
                unsigned char lo = pattern[k], hi = lo;
                if (k + 2 < m && pattern[k + 1] == '-' && pattern[k + 2] != ']') {
                    hi = pattern[k + 2];
                    k += 2;
                }
                for (int x = lo; x <= hi; x++) {
                    accepted[x] = true;
                }
                k++;
            }
            if (k == m) {
                return false; // a [ with no closing ] never matches
            }
            for (size_t i = 0; i < n; i++) {
                next[i + 1] = reach[i] && accepted[(unsigned char)text[i]] != negated;
            }
            j = k + 1;
        } else {
            for (size_t i = 0; i < n; i++) {
                next[i + 1] = reach[i] && (c == '_' || text[i] == pattern[j]);
            }
            j++;
        }
        reach.swap(next);
    }
    return reach[n];
}

int main() {
    std::string line;
    std::getline(std::cin, line);
    int n = std::stoi(line);
    for (int q = 0; q < n; q++) {
        std::getline(std::cin, line);
        if (!line.empty() && line.back() == '\r') {
            line.pop_back();
        }
        size_t p = line.find('\'');
        Bytes text = quoted(line, p);
        p = line.find('\'', p);
        Bytes pattern = quoted(line, p);
        puts(like(text, pattern) ? "YES" : "NO");
    }
}
