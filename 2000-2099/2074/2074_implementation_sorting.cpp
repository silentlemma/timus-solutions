#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> path;  // names of the current topic and its ancestors
    map<int, set<string>> topics;  // problem -> descriptions of its topics
    string current, line;
    while (getline(cin, line)) {
        istringstream words(line);
        string first;
        if (!(words >> first)) continue;
        if (first.back() == '.') {
            // a heading "1.2. name": its depth is the number of dots
            size_t depth = count(first.begin(), first.end(), '.');
            string name, word;
            while (words >> word) name += (name.empty() ? "" : " ") + word;
            path.resize(depth - 1);
            path.push_back(name);
            current.clear();
            for (const string& p : path) current += (current.empty() ? "" : ".") + p;
        } else {
            topics[stoi(first)].insert(current);
            for (string w; words >> w;) topics[stoi(w)].insert(current);
        }
    }
    map<string, vector<int>> groups;  // problems are visited in increasing order
    for (const auto& [problem, own] : topics) {
        string key;
        for (const string& t : own) key += (key.empty() ? "" : ", ") + t;
        groups[key].push_back(problem);
    }
    vector<string> lines;
    for (const auto& [key, problems] : groups) {
        string s;
        for (int p : problems) s += (s.empty() ? "" : ", ") + to_string(p);
        lines.push_back(s + " : " + key);
    }
    sort(lines.begin(), lines.end());
    for (const string& s : lines) cout << s << "\n";
}
