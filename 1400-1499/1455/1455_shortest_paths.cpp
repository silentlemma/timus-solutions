#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;

bool startsWith(const string &s, const string &prefix) {
    return s.size() >= prefix.size() && s.compare(0, prefix.size(), prefix) == 0;
}

int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (auto &w : words)
        cin >> w;
    // a state is the tail by which one parse runs ahead of the other; the
    // cost is the length of the text so far, and Dijkstra finds the shortest text
    map<string, int> dist;
    map<string, pair<string, string>> back; // the previous tail and the new piece of text
    map<string, bool> first;                // tails that start a search
    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> heap;
    auto relax = [&](const string &tail, int cost, const string &from, const string &piece,
                     bool start) {
        auto it = dist.find(tail);
        if (it != dist.end() && it->second <= cost)
            return;
        dist[tail] = cost;
        back[tail] = {from, piece};
        first[tail] = start;
        heap.push({cost, tail});
    };
    for (auto &u : words)
        for (auto &v : words)
            if (u != v && startsWith(v, u))
                relax(v.substr(u.size()), v.size(), "", v, true);
    while (!heap.empty()) {
        auto [cost, tail] = heap.top();
        heap.pop();
        if (cost > dist[tail])
            continue;
        for (auto &w : words) {
            if (w == tail) { // both parses end together: rebuild the text from its pieces
                vector<string> pieces;
                for (string t = tail;;) {
                    pieces.push_back(back[t].second);
                    if (first[t])
                        break;
                    t = back[t].first;
                }
                reverse(pieces.begin(), pieces.end());
                string text;
                for (auto &p : pieces)
                    text += p;
                cout << "YES\n" << text << "\n";
                return 0;
            }
            if (startsWith(w, tail)) {
                string rest = w.substr(tail.size());
                relax(rest, cost + rest.size(), tail, rest, false);
            } else if (startsWith(tail, w)) {
                relax(tail.substr(w.size()), cost, tail, "", false);
            }
        }
    }
    cout << "NO\n";
}
