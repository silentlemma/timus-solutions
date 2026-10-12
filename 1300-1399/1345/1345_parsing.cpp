#include <cctype>
#include <iostream>
#include <iterator>
#include <set>
#include <string>

const std::set<std::string> KEYWORDS = {
    "and",       "array",  "begin", "case", "class",    "const",     "div",
    "do",        "else",   "end",   "for",  "function", "if",        "implementation",
    "interface", "mod",    "not",   "of",   "or",       "procedure", "program",
    "record",    "repeat", "shl",   "shr",  "string",   "then",      "to",
    "type",      "unit",   "until", "uses", "var",      "with",      "while"};

bool isDigit(char c) { return c >= '0' && c <= '9'; }
bool isWord(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_'; }

std::string wrap(const std::string &kind, const std::string &text) {
    return "<span class=" + kind + ">" + text + "</span>";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::string raw((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());
    std::string text;
    for (size_t k = 0; k < raw.size(); k++) {
        if (!(raw[k] == '\r' && k + 1 < raw.size() && raw[k + 1] == '\n'))
            text += raw[k];
    }
    std::string out;
    size_t i = 0, n = text.size();
    while (i < n) {
        char c = text[i];
        size_t j = i + 1;
        if (c == '{') {
            j = text.find('}', i);
            j = j == std::string::npos ? n : j + 1;
            out += wrap("comment", text.substr(i, j - i));
        } else if (c == '/' && i + 1 < n && text[i + 1] == '/') {
            j = text.find('\n', i); // the line break is not part of it
            j = j == std::string::npos ? n : j;
            out += wrap("comment", text.substr(i, j - i));
        } else if (c == '\'') {
            j = text.find('\'', i + 1);
            j = j == std::string::npos ? n : j + 1;
            out += wrap("string", text.substr(i, j - i));
        } else if (c == '#' && i + 1 < n && isDigit(text[i + 1])) {
            for (j = i + 1; j < n && isDigit(text[j]); j++) {
            }
            out += wrap("string", text.substr(i, j - i));
        } else if (isDigit(c)) {
            for (j = i; j < n && isDigit(text[j]); j++) {
            }
            // one point is allowed, but only with digits after it
            if (j + 1 < n && text[j] == '.' && isDigit(text[j + 1])) {
                for (j++; j < n && isDigit(text[j]); j++) {
                }
            }
            out += wrap("number", text.substr(i, j - i));
        } else if (isWord(c)) {
            for (j = i; j < n && (isWord(text[j]) || isDigit(text[j])); j++) {
            }
            std::string word = text.substr(i, j - i), lower = word;
            for (char &ch : lower)
                ch = (char)std::tolower((unsigned char)ch);
            out += KEYWORDS.count(lower) ? wrap("keyword", word) : word;
        } else {
            out += c;
        }
        i = j;
    }
    std::cout << out;
    return 0;
}
