#include <iostream>
#include <string>
#include <vector>

const char *FAILED = "I HAVE FAILED!!!";

std::vector<int> prefixFunction(const std::string &t) {
    std::vector<int> p(t.size(), 0);
    for (size_t i = 1, k = 0; i < t.size(); i++) {
        while (k && t[i] != t[k]) k = p[k - 1];
        if (t[i] == t[k]) k++;
        p[i] = k;
    }
    return p;
}

// the first occurrence of t in s[from, to), or -1
int find(const std::string &s, int from, int to, const std::string &t,
         const std::vector<int> &p) {
    size_t k = 0;
    for (int i = from; i < to; i++) {
        while (k && s[i] != t[k]) k = p[k - 1];
        if (s[i] == t[k] && ++k == t.size()) return i - k + 1;
    }
    return -1;
}

int main() {
    std::string source, line;
    std::getline(std::cin, source);
    std::getline(std::cin, line);
    if (!source.empty() && source.back() == '\r') source.pop_back();
    if (!line.empty() && line.back() == '\r') line.pop_back();
    std::vector<std::string> target;
    for (size_t start = 0;;) {
        size_t space = line.find(' ', start);
        target.push_back(line.substr(start, space - start));
        if (space == std::string::npos) break;
        start = space + 1;
    }
    std::vector<bool> keep(source.size(), false);
    size_t j = 0;
    std::vector<int> p = prefixFunction(target[0]);
    // each wanted word goes to its earliest place in the current word, at
    // least one erased letter after the previous one there; if it does not
    // fit, the next word of the source is tried
    for (size_t begin = 0; begin < source.size() && j < target.size();) {
        size_t end = source.find(' ', begin);
        if (end == std::string::npos) end = source.size();
        size_t pos = begin;
        while (j < target.size() && end - pos >= target[j].size()) {
            int at = find(source, pos, end, target[j], p);
            if (at < 0) break;
            for (size_t i = at; i < at + target[j].size(); i++) keep[i] = true;
            pos = at + target[j].size() + 1;
            if (++j < target.size()) p = prefixFunction(target[j]);
            if (pos > end) break;
        }
        begin = end + 1;
    }
    if (j < target.size()) {
        std::cout << FAILED << "\n";
        return 0;
    }
    for (size_t i = 0; i < source.size(); i++) {
        if (source[i] != ' ' && !keep[i]) source[i] = '_';
    }
    std::cout << source << "\n";
}
