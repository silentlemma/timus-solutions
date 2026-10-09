#include <cstdio>
#include <string>
#include <vector>

const int BUFFER = 1 << 16;
// what happens to a double quote
enum { KEEP, OPEN, CLOSE, DROP };

bool blank(char c) { return c == ' ' || c == '\t' || c == '\r' || c == '\v' || c == '\f'; }

bool letter(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

int main() {
    // the text is handled as bytes: letters above 127 are copied as they are
    std::string s;
    char buf[BUFFER];
    for (size_t k; (k = fread(buf, 1, BUFFER, stdin)) > 0;)
        s.append(buf, k);
    size_t n = s.size();
    std::vector<char> mark(n, KEEP);
    std::vector<size_t> quotes;
    // pairs the quotes of the finished paragraph; an unpaired last one goes away
    auto close = [&]() {
        if (quotes.size() % 2 == 1) {
            mark[quotes.back()] = DROP;
            quotes.pop_back();
        }
        for (size_t k = 0; k < quotes.size(); k++)
            mark[quotes[k]] = k % 2 == 0 ? OPEN : CLOSE;
        quotes.clear();
    };
    for (size_t i = 0; i < n;) {
        if (s[i] == '\\') {
            // \" is an umlaut; otherwise the command name is the letters after \.
            if (i + 1 < n && s[i + 1] == '"') {
                i += 2;
                continue;
            }
            size_t j = i + 1;
            while (j < n && letter(s[j]))
                j++;
            if (s.compare(i + 1, j - i - 1, "par") == 0)
                close();
            i = j;
        } else if (s[i] == '"') {
            quotes.push_back(i++);
        } else {
            // a line of only whitespace that ends with a line break ends a paragraph
            if (s[i] == '\n') {
                size_t j = i + 1;
                while (j < n && blank(s[j]))
                    j++;
                if (j < n && s[j] == '\n')
                    close();
            }
            i++;
        }
    }
    close();
    std::string out;
    for (size_t i = 0; i < n; i++) {
        if (mark[i] == KEEP)
            out += s[i];
        else if (mark[i] == OPEN)
            out += "``";
        else if (mark[i] == CLOSE)
            out += "''";
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
