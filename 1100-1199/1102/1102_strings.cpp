#include <cstdio>
#include <iostream>
#include <string>

const char *WORDS[] = {"out", "output", "puton", "in", "input", "one"};

// read backwards the words never start one another, so at most one word
// ends at each position and the line is cut greedily from its end
bool dialogue(const std::string &s) {
    size_t end = s.size();
    while (end > 0) {
        size_t cut = std::string::npos;
        for (const char *w : WORDS) {
            std::string word(w);
            if (word.size() <= end && s.compare(end - word.size(), word.size(), word) == 0)
                cut = end - word.size();
        }
        if (cut == std::string::npos)
            return false;
        end = cut;
    }
    return true;
}

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    std::cin >> n;
    std::string s, out;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        out += dialogue(s) ? "YES\n" : "NO\n";
    }
    std::cout << out;
}
