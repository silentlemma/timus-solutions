#include <algorithm>
#include <cctype>
#include <iostream>
#include <iterator>
#include <string>
#include <utility>
#include <vector>

const int WIDTH = 40;

bool isLetter(char c) { return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'); }

std::string lower(std::string s) {
    for (char &c : s)
        c = std::tolower(static_cast<unsigned char>(c));
    return s;
}

int main() {
    std::string data((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());
    data.erase(std::remove(data.begin(), data.end(), '\r'), data.end());
    size_t pos = data.find('\n');
    int n = std::stoi(data.substr(0, pos));
    // a rule s1-s2 matches words ending in s1s2 and carries s2 over
    std::vector<std::pair<std::string, int>> rules;
    for (int i = 0; i < n; i++) {
        size_t end = data.find('\n', pos + 1);
        std::string line = data.substr(pos + 1, end - pos - 1), clean;
        for (char c : line)
            if (!std::isspace(static_cast<unsigned char>(c)))
                clean += c;
        size_t dash = clean.find('-');
        rules.push_back(
            {lower(clean.substr(0, dash) + clean.substr(dash + 1)), int(clean.size() - dash - 1)});
        pos = end;
    }
    std::string text = pos == std::string::npos ? "" : data.substr(pos + 1), out;
    int col = 0;
    for (size_t i = 0; i < text.size();) {
        char c = text[i];
        if (c == '\n') {
            out += c;
            col = 0;
            i++;
            continue;
        }
        if (!isLetter(c)) {
            // a full line moves a separator to the next one
            if (col == WIDTH) {
                out += '\n';
                col = 0;
            }
            out += c;
            col++;
            i++;
            continue;
        }
        size_t start = i;
        while (i < text.size() && isLetter(text[i]))
            i++;
        std::string word = text.substr(start, i - start), low = lower(word);
        int len = word.size();
        if (col + len <= WIDTH) {
            out += word;
            col += len;
            continue;
        }
        // the shortest carried part whose head and '-' still fit
        int carry = 0;
        for (auto &[pattern, cut] : rules) {
            bool ends = low.size() >= pattern.size() &&
                        low.compare(low.size() - pattern.size(), pattern.size(), pattern) == 0;
            if (ends && col + len - cut + 1 <= WIDTH && (carry == 0 || cut < carry))
                carry = cut;
        }
        if (carry > 0) {
            out += word.substr(0, len - carry) + "-\n" + word.substr(len - carry);
        } else {
            out += "\n" + word;
            carry = len;
        }
        col = carry;
    }
    std::cout << out;
}
