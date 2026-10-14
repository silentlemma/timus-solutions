#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int ALPHABET = 26;

int main() {
    int n;
    string a, b;
    cin >> n >> a >> b;
    // suffix automaton of a: every state is a class of substrings with the
    // same end positions; len is the longest of them, link the suffix link
    vector<vector<int>> next(1, vector<int>(ALPHABET, -1));
    vector<int> link = {-1}, len = {0};
    int last = 0;
    for (char ch : a) {
        int c = ch - 'A', cur = next.size();
        next.push_back(vector<int>(ALPHABET, -1));
        link.push_back(0);
        len.push_back(len[last] + 1);
        int p = last;
        while (p != -1 && next[p][c] == -1) {
            next[p][c] = cur;
            p = link[p];
        }
        if (p != -1) {
            int q = next[p][c];
            if (len[p] + 1 == len[q])
                link[cur] = q;
            else {
                int clone = next.size();
                next.push_back(next[q]);
                link.push_back(link[q]);
                len.push_back(len[p] + 1);
                for (; p != -1 && next[p][c] == q; p = link[p])
                    next[p][c] = clone;
                link[q] = link[cur] = clone;
            }
        }
        last = cur;
    }
    // walk b through the automaton, keeping the longest suffix of the read
    // part of b that occurs in a
    int state = 0, run = 0, best = 0, end = 0;
    for (int i = 0; i < (int)b.size(); i++) {
        int c = b[i] - 'A';
        while (state != 0 && next[state][c] == -1) {
            state = link[state];
            run = len[state];
        }
        if (next[state][c] != -1) {
            state = next[state][c];
            run++;
        }
        if (run > best)
            best = run, end = i + 1;
    }
    cout << b.substr(end - best, best) << "\n";
}
