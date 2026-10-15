#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

struct Suffix {
    int word;
    int pos;
};

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    std::cin >> n;
    std::vector<std::string> words(n);
    for (std::string& w : words) {
        std::cin >> w;
    }
    auto tail = [&](const Suffix& s) {
        return words[s.word].c_str() + s.pos;
    };
    // every suffix of every command, sorted; a substring starting at some
    // position is in another command exactly when it is a prefix of another
    // command's suffix, and the nearest such suffixes in the order share most
    std::vector<Suffix> suffixes;
    for (int i = 0; i < n; i++) {
        for (int p = 0; p < (int)words[i].size(); p++) {
            suffixes.push_back({i, p});
        }
    }
    std::sort(suffixes.begin(), suffixes.end(), [&](const Suffix& a, const Suffix& b) {
        return std::strcmp(tail(a), tail(b)) < 0;
    });
    int total = suffixes.size();
    std::vector<int> adjacent(total, 0);
    for (int k = 0; k + 1 < total; k++) {
        const char *a = tail(suffixes[k]), *b = tail(suffixes[k + 1]);
        int l = 0;
        while (a[l] && a[l] == b[l]) {
            l++;
        }
        adjacent[k] = l;
    }
    std::vector<int> shared(total, 0);  // the longest prefix shared with another command
    int run = 0;
    for (int k = 1; k < total; k++) {
        bool other = suffixes[k].word != suffixes[k - 1].word;
        run = other ? adjacent[k - 1] : std::min(run, adjacent[k - 1]);
        shared[k] = run;
    }
    run = 0;
    for (int k = total - 2; k >= 0; k--) {
        bool other = suffixes[k].word != suffixes[k + 1].word;
        run = other ? adjacent[k] : std::min(run, adjacent[k]);
        shared[k] = std::max(shared[k], run);
    }
    std::vector<std::string> best(n);
    for (int k = 0; k < total; k++) {
        const Suffix& s = suffixes[k];
        int need = shared[k] + 1;
        int left = words[s.word].size() - s.pos;
        if (need <= left && (best[s.word].empty() || need < (int)best[s.word].size())) {
            best[s.word] = words[s.word].substr(s.pos, need);
        }
    }
    for (const std::string& b : best) {
        std::cout << b << "\n";
    }
}
