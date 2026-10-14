#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int LETTERS = 26;

int main() {
    string s;
    if (!(cin >> s))
        return 0;
    int most = 2 * (int)s.size() + 1;
    // suffix automaton: every state is a class of substrings with the same
    // end positions, from link-length + 1 up to length characters long
    vector<int> length(most, 0), link(most, -1);
    vector<vector<int>> next(most, vector<int>(LETTERS, -1));
    int size = 1, last = 0;
    for (char ch : s) {
        int c = ch - 'a';
        int cur = size++;
        length[cur] = length[last] + 1;
        int p = last;
        while (p != -1 && next[p][c] == -1) {
            next[p][c] = cur;
            p = link[p];
        }
        if (p == -1) {
            link[cur] = 0;
        } else {
            int q = next[p][c];
            if (length[p] + 1 == length[q]) {
                link[cur] = q;
            } else {
                // split q: the clone keeps the shorter strings
                int clone = size++;
                length[clone] = length[p] + 1;
                link[clone] = link[q];
                next[clone] = next[q];
                while (p != -1 && next[p][c] == q) {
                    next[p][c] = clone;
                    p = link[p];
                }
                link[q] = clone;
                link[cur] = clone;
            }
        }
        last = cur;
    }
    long long total = 0;
    for (int v = 1; v < size; v++)
        total += length[v] - length[link[v]];
    cout << total << "\n";
}
