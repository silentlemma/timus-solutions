#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const int LONGEST = 140;
const int PREFIX = 6;  // "RT @" and ": "

int main() {
    string line;
    getline(cin, line);
    int n = stoi(line);
    vector<string> names(n);
    vector<vector<string>> follow_names(n);
    for (int i = 0; i < n; i++) {
        // a description is a name, a count and that many names
        vector<string> words;
        while (words.size() < 2 || (int)words.size() < 2 + stoi(words[1])) {
            getline(cin, line);
            istringstream in(line);
            string w;
            while (in >> w) words.push_back(w);
        }
        names[i] = words[0];
        follow_names[i].assign(words.begin() + 2, words.end());
    }
    string tweet;
    getline(cin, tweet);
    if (!tweet.empty() && tweet.back() == '\r') tweet.pop_back();
    map<string, int> index;
    for (int i = 0; i < n; i++) index[names[i]] = i;
    // length[u] is the shortest message u can hold; a retweet of u's message
    // is longer by the prefix and u's name
    vector<int> length(n, LONGEST + 1);
    vector<bool> done(n, false);
    length[0] = tweet.size();
    while (true) {
        int u = -1;
        for (int i = 0; i < n; i++)
            if (!done[i] && (u < 0 || length[i] < length[u])) u = i;
        if (u < 0 || length[u] > LONGEST) break;
        done[u] = true;
        int longer = length[u] + PREFIX + names[u].size();
        for (const string& f : follow_names[u]) {
            int v = index[f];
            if (longer < length[v]) length[v] = longer;
        }
    }
    // everybody who holds a message shows it to all followers
    vector<bool> knows(n, false);
    for (int u = 0; u < n; u++) {
        if (!done[u]) continue;
        knows[u] = true;
        for (const string& f : follow_names[u]) knows[index[f]] = true;
    }
    string out;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (knows[i]) {
            count++;
            out += names[i] + "\n";
        }
    }
    cout << count << "\n" << out;
    return 0;
}
