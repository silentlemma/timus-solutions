#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;

const int SHORT = 3; // any three points on both sides match

// the distinct directions as reduced p / q with q > 0, by increasing p / q
vector<pair<ll, ll>> directions(vector<pair<ll, ll>> trees) {
    for (auto &t : trees) {
        if (t.second < 0)
            t = {-t.first, -t.second};
        ll g = gcd(llabs(t.first), t.second);
        t = {t.first / g, t.second / g};
    }
    sort(trees.begin(), trees.end(), [](const pair<ll, ll> &a, const pair<ll, ll> &b) {
        return a.first * b.second < b.first * a.second;
    });
    trees.erase(unique(trees.begin(), trees.end()), trees.end());
    return trees;
}

// cross-ratio of every four consecutive directions, as small integer ids
vector<int> ratios(const vector<pair<ll, ll>> &d, map<pair<ll, ll>, int> &ids) {
    vector<int> out;
    for (size_t i = 0; i + SHORT < d.size(); i++) {
        ll p1 = d[i].first, q1 = d[i].second, p2 = d[i + 1].first, q2 = d[i + 1].second;
        ll p3 = d[i + 2].first, q3 = d[i + 2].second;
        ll p4 = d[i + SHORT].first, q4 = d[i + SHORT].second;
        // (c - a)(d - b) / ((c - b)(d - a)); the denominators q cancel
        ll num = (p3 * q1 - p1 * q3) * (p4 * q2 - p2 * q4);
        ll den = (p3 * q2 - p2 * q3) * (p4 * q1 - p1 * q4);
        ll g = gcd(num, den);
        auto key = make_pair(num / g, den / g);
        auto it = ids.find(key);
        if (it == ids.end())
            it = ids.emplace(key, (int)ids.size()).first;
        out.push_back(it->second);
    }
    return out;
}

// longest common substring of two sequences, by a suffix automaton of a
int longestCommon(const vector<int> &a, const vector<int> &b, ll symbols) {
    vector<int> link = {-1}, len = {0}, head = {-1}, edgeSymbol, edgeNext;
    // trans[state * symbols + symbol]: the next state; each state lists its symbols
    unordered_map<ll, int> trans;
    auto add = [&](int state, int symbol, int target) {
        trans[state * symbols + symbol] = target;
        edgeSymbol.push_back(symbol);
        edgeNext.push_back(head[state]);
        head[state] = (int)edgeSymbol.size() - 1;
    };
    int last = 0;
    for (int ch : a) {
        int cur = (int)len.size();
        len.push_back(len[last] + 1);
        link.push_back(0);
        head.push_back(-1);
        int p = last;
        while (p != -1 && !trans.count(p * symbols + ch)) {
            add(p, ch, cur);
            p = link[p];
        }
        if (p != -1) {
            int q = trans[p * symbols + ch];
            if (len[p] + 1 == len[q])
                link[cur] = q;
            else {
                int clone = (int)len.size();
                len.push_back(len[p] + 1);
                link.push_back(link[q]);
                head.push_back(-1);
                for (int e = head[q]; e != -1; e = edgeNext[e])
                    add(clone, edgeSymbol[e], trans[q * symbols + edgeSymbol[e]]);
                while (p != -1) {
                    auto it = trans.find(p * symbols + ch);
                    if (it == trans.end() || it->second != q)
                        break;
                    it->second = clone;
                    p = link[p];
                }
                link[q] = link[cur] = clone;
            }
        }
        last = cur;
    }
    int best = 0, state = 0, run = 0;
    for (int ch : b) {
        while (state && !trans.count(state * symbols + ch)) {
            state = link[state];
            run = len[state];
        }
        auto it = trans.find(state * symbols + ch);
        if (it != trans.end()) {
            state = it->second;
            run++;
        }
        best = max(best, run);
    }
    return best;
}

int main() {
    vector<pair<ll, ll>> upper, lower;
    ll x, y;
    while (scanf("%lld %lld", &x, &y) == 2 && (x != 0 || y != 0))
        (y > 0 ? upper : lower).push_back({x, y});
    vector<pair<ll, ll>> up = directions(upper), low = directions(lower);
    int answer = (int)min({up.size(), low.size(), (size_t)SHORT});
    if ((int)up.size() > SHORT && (int)low.size() > SHORT) {
        map<pair<ll, ll>, int> ids;
        vector<int> ra = ratios(up, ids), rb = ratios(low, ids);
        int common = longestCommon(ra, rb, (ll)ids.size());
        if (common > 0)
            answer = common + SHORT;
    }
    printf("%d\n", answer);
}
