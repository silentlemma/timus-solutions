#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

constexpr int NAME = 16;  // names have at most 10 letters
constexpr long long ENDLESS = 1LL << 62;

struct Event {
    long long t, value;
    int kind;  // a pour of liqueur kind >= 0, OLEG or FIRE
};
constexpr int OLEG = -1, FIRE = -2;

// layers in order of names (the densest at the bottom), with a Fenwick tree of heights
int m, top;
vector<long long> tree, height;

void add(int i, long long delta) {
    height[i] += delta;
    for (i++; i <= m; i += i & -i) tree[i] += delta;
}

// the layer that contains level h, and how much of it lies above h
pair<int, long long> layerAt(long long h) {
    int pos = 0;
    for (int step = top; step > 0; step >>= 1)
        if (pos + step <= m && tree[pos + step] <= h) {
            pos += step;
            h -= tree[pos];
        }
    return {pos, height[pos] - h};
}

struct Sip {
    long long from, to;
    int kind;
};

int main() {
    int n;
    scanf("%d", &n);
    vector<Event> events(n);
    vector<string> raw(n);
    char word[NAME];
    for (int i = 0; i < n; i++) {
        scanf("%lld %s", &events[i].t, word);
        raw[i] = word;
        if (raw[i] != "fire") scanf("%lld", &events[i].value);
    }
    vector<string> names;
    for (const string& s : raw)
        if (s != "Oleg" && s != "fire") names.push_back(s);
    sort(names.begin(), names.end());
    names.erase(unique(names.begin(), names.end()), names.end());
    for (int i = 0; i < n; i++)
        events[i].kind = raw[i] == "Oleg"   ? OLEG
                         : raw[i] == "fire" ? FIRE
                                            : lower_bound(names.begin(), names.end(), raw[i]) -
                                                  names.begin();
    m = names.size();
    tree.assign(m + 1, 0);
    height.assign(m, 0);
    top = 1;
    while (top * 2 <= m) top *= 2;
    long long total = 0, straw = 0, clock = 0;
    bool drinking = false;
    vector<Sip> sips;
    // drink up to `amount` mm from the straw level, starting at `clock`
    auto drink = [&](long long amount) {
        while (amount > 0 && total > straw) {
            auto [layer, above] = layerAt(straw);
            long long take = min(above, amount);
            add(layer, -take);
            total -= take;
            amount -= take;
            sips.push_back({clock, clock + take, layer});
            clock += take;
        }
    };
    for (const Event& e : events) {
        if (drinking) {
            drink(e.t - clock);
            // running dry before this moment stops him; running dry exactly now does not
            // matter: a pour lets him go on, and Oleg or fire set the state anyway
            drinking = clock == e.t;
        }
        clock = e.t;
        if (e.kind == OLEG) {
            straw = e.value;
            drinking = true;
        } else if (e.kind == FIRE) {
            drinking = false;
        } else {
            add(e.kind, e.value);
            total += e.value;
        }
    }
    if (drinking) drink(ENDLESS);
    vector<Sip> merged;
    for (const Sip& s : sips)
        if (!merged.empty() && merged.back().kind == s.kind && merged.back().to == s.from)
            merged.back().to = s.to;
        else
            merged.push_back(s);
    for (const Sip& s : merged) printf("%lld-%lld %s\n", s.from, s.to, names[s.kind].c_str());
}
