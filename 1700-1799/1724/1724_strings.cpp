#include <cctype>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

// the stack after each prefix is a tree node: a push makes a new node, a
// matching close returns to the parent, a wrong close starts a lone node,
// and a piece is human exactly when it ends on the node it started on
int main() {
    std::ios::sync_with_stdio(false);
    std::string dna;
    std::cin >> dna;
    std::vector<int> parent = {-1};
    std::vector<char> letter = {0};
    std::vector<int> state(dna.size() + 1, 0);
    int cur = 0;
    for (size_t i = 0; i < dna.size(); i++) {
        char c = dna[i];
        if (isupper(c)) {
            parent.push_back(cur);
            letter.push_back(c);
            cur = parent.size() - 1;
        } else if (letter[cur] == toupper(c)) {
            cur = parent[cur];
        } else {
            parent.push_back(-1);
            letter.push_back(0);
            cur = parent.size() - 1;
        }
        state[i + 1] = cur;
    }
    int q;
    std::cin >> q;
    std::string out(q, '0');
    for (int k = 0; k < q; k++) {
        int left, right;
        std::cin >> left >> right;
        if (state[left - 1] == state[right]) out[k] = '1';
    }
    printf("%s\n", out.c_str());
}
