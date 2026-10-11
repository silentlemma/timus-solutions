#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

// a line without its line break; text keeps carriage returns as data
bool readLine(std::string &s, bool word = true) {
    if (!std::getline(std::cin, s))
        return false;
    if (word && !s.empty() && s.back() == '\r')
        s.pop_back();
    return true;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::string s;
    readLine(s);
    int n = std::stoi(s);
    std::vector<std::string> words(n);
    size_t total = 1;
    for (auto &w : words) {
        readLine(w);
        total += w.size();
    }
    // build the trie as first-child / next-sibling lists
    std::vector<int> child(total, -1), sibling(total, -1), ends(total);
    std::vector<unsigned char> byte(total);
    int nodes = 1;
    for (auto &w : words) {
        int v = 0;
        for (unsigned char c : w) {
            int u = child[v];
            while (u >= 0 && byte[u] != c)
                u = sibling[u];
            if (u < 0) {
                u = nodes++;
                byte[u] = c;
                sibling[u] = child[v];
                child[v] = u;
            }
            v = u;
        }
        ends[v] = std::max(ends[v], (int)w.size());
    }
    words.clear();
    words.shrink_to_fit();
    // renumber in breadth-first order: the children of v then take the
    // numbers first[v] .. first[v] + count[v] - 1, and label[u] is the
    // byte leading to u
    std::vector<int> first(nodes), count(nodes), longest(nodes), old = {0};
    std::vector<unsigned char> label(nodes);
    for (int v = 0; v < nodes; v++) {
        first[v] = old.size();
        for (int u = child[old[v]]; u >= 0; u = sibling[u]) {
            label[old.size()] = byte[u];
            longest[old.size()] = ends[u];
            old.push_back(u);
        }
        count[v] = old.size() - first[v];
    }
    // the child of v along byte c, or -1
    auto go = [&](int v, unsigned char c) {
        const void *hit = std::memchr(label.data() + first[v], c, count[v]);
        return hit ? int((const unsigned char *)hit - label.data()) : -1;
    };
    // failure links in the same order; a node also takes the longest word
    // of its failure node, which comes earlier
    std::vector<int> fail(nodes);
    for (int v = 1; v < nodes; v++)
        for (int u = first[v]; u < first[v] + count[v]; u++) {
            int f = fail[v], g;
            while ((g = go(f, label[u])) < 0 && f)
                f = fail[f];
            fail[u] = std::max(g, 0);
            longest[u] = std::max(longest[u], longest[fail[u]]);
        }
    readLine(s);
    int m = std::stoi(s);
    for (int row = 1; row <= m && readLine(s, false); row++) {
        int v = 0, best = s.size() + 1;
        for (int i = 0; i < (int)s.size(); i++) {
            int g;
            while ((g = go(v, s[i])) < 0 && v)
                v = fail[v];
            v = std::max(g, 0);
            if (longest[v])
                best = std::min(best, i + 2 - longest[v]);
        }
        if (best <= (int)s.size()) {
            printf("%d %d\n", row, best);
            return 0;
        }
    }
    printf("Passed\n");
}
