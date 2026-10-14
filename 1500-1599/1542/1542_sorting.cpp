#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

const size_t SHOWN = 10; // suggestions per query

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, string>> words(n); // (minus the count, word)
    for (auto &w : words) {
        cin >> w.second >> w.first;
        w.first = -w.first;
    }
    int m;
    cin >> m;
    vector<string> queries(m);
    unordered_map<string, vector<int>> found; // query -> indices of its words
    for (auto &q : queries) {
        cin >> q;
        found[q];
    }
    // the best words come first, so every queried prefix simply keeps the
    // first ten words that start with it
    sort(words.begin(), words.end());
    for (int i = 0; i < n; i++) {
        const string &word = words[i].second;
        for (size_t end = 1; end <= word.size(); end++) {
            auto it = found.find(word.substr(0, end));
            if (it != found.end() && it->second.size() < SHOWN)
                it->second.push_back(i);
        }
    }
    string out;
    for (int j = 0; j < m; j++) {
        if (j > 0)
            out += '\n';
        for (int i : found[queries[j]])
            out += words[i].second + '\n';
    }
    cout << out;
}
