#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;

const ll NEG = -(1LL << 62);
const int KINDS = 3;  // a count of teams: none, one, two or more

int size;
// every node of the tree over f keeps its total, its count of teams (capped
// at 2), its best prefix and suffix with exactly 0, 1 or 2+ teams, and its
// best range with at least two teams
std::vector<ll> total, best;
std::vector<int> kind;
std::vector<ll> pre[KINDS], suf[KINDS];

void reset() {
    std::fill(total.begin(), total.end(), 0);
    std::fill(kind.begin(), kind.end(), 0);
    std::fill(best.begin(), best.end(), NEG);
    for (int k = 0; k < KINDS; k++) {
        std::fill(pre[k].begin(), pre[k].end(), k == 0 ? 0 : NEG);
        std::fill(suf[k].begin(), suf[k].end(), k == 0 ? 0 : NEG);
    }
}

void pull(int v) {
    int a = 2 * v, b = a + 1;
    total[v] = total[a] + total[b];
    kind[v] = std::min(kind[a] + kind[b], 2);
    for (int k = 0; k < KINDS; k++) {
        pre[k][v] = pre[k][a];
        suf[k][v] = suf[k][b];
    }
    for (int j = 0; j < KINDS; j++) {
        // prefixes: inside the left child, or all of it and more
        if (pre[j][b] != NEG) {
            int k = std::min(kind[a] + j, 2);
            pre[k][v] = std::max(pre[k][v], total[a] + pre[j][b]);
        }
        if (suf[j][a] != NEG) {
            int k = std::min(kind[b] + j, 2);
            suf[k][v] = std::max(suf[k][v], suf[j][a] + total[b]);
        }
    }
    // ranges: inside a child, or across with two or more teams
    ll top = std::max(best[a], best[b]);
    for (int i = 0; i < KINDS; i++) {
        for (int j = std::max(0, 2 - i); j < KINDS; j++) {
            if (suf[i][a] != NEG && pre[j][b] != NEG) {
                top = std::max(top, suf[i][a] + pre[j][b]);
            }
        }
    }
    best[v] = top;
}

void add(int fi, ll s) {
    int v = size + fi;
    total[v] += s;
    kind[v] = std::min(kind[v] + 1, 2);
    for (int k = 0; k < KINDS; k++) {
        pre[k][v] = suf[k][v] = k == kind[v] ? total[v] : NEG;
    }
    best[v] = kind[v] == 2 ? total[v] : NEG;
    for (v /= 2; v > 0; v /= 2) {
        pull(v);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<ll> a(n), f(n), s(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld", &a[i], &f[i], &s[i]);
    }
    std::vector<ll> ages(a), fs(f);
    std::sort(ages.begin(), ages.end());
    ages.erase(std::unique(ages.begin(), ages.end()), ages.end());
    std::sort(fs.begin(), fs.end());
    fs.erase(std::unique(fs.begin(), fs.end()), fs.end());
    int na = ages.size(), nf = fs.size();
    std::vector<std::vector<std::pair<int, ll>>> by_age(na);
    for (int i = 0; i < n; i++) {
        int ai = std::lower_bound(ages.begin(), ages.end(), a[i]) - ages.begin();
        int fi = std::lower_bound(fs.begin(), fs.end(), f[i]) - fs.begin();
        by_age[ai].push_back({fi, s[i]});
    }
    size = 1;
    while (size < nf) {
        size *= 2;
    }
    total.resize(2 * size);
    best.resize(2 * size);
    kind.resize(2 * size);
    for (int k = 0; k < KINDS; k++) {
        pre[k].resize(2 * size);
        suf[k].resize(2 * size);
    }
    ll answer = NEG;
    int best_left = 0, best_right = 0;
    for (int left = 0; left < na; left++) {
        reset();
        for (int right = left; right < na; right++) {
            for (auto& team : by_age[right]) {
                add(team.first, team.second);
            }
            if (best[1] > answer) {
                answer = best[1];
                best_left = left;
                best_right = right;
            }
        }
    }
    // the range of f values with the largest total holding at least two
    // teams: for each right end the best left end has the least prefix sum
    // among those leaving at least two teams inside
    std::vector<ll> prefix(nf + 1, 0);
    std::vector<int> inside(nf + 1, 0);
    for (int r = best_left; r <= best_right; r++) {
        for (auto& team : by_age[r]) {
            prefix[team.first + 1] += team.second;
            inside[team.first + 1]++;
        }
    }
    for (int i = 0; i < nf; i++) {
        prefix[i + 1] += prefix[i];
        inside[i + 1] += inside[i];
    }
    ll top = NEG, low = NEG;
    int lo = 0, hi = 0, low_at = 0;
    for (int r = 1, t = 0; r <= nf; r++) {
        for (; t < r && inside[t] <= inside[r] - 2; t++) {
            if (low == NEG || prefix[t] < low) {
                low = prefix[t];
                low_at = t;
            }
        }
        if (low != NEG && prefix[r] - low > top) {
            top = prefix[r] - low;
            lo = low_at;
            hi = r - 1;
        }
    }
    printf("%lld %lld\n%lld %lld\n", ages[best_left], ages[best_right], fs[lo], fs[hi]);
}
