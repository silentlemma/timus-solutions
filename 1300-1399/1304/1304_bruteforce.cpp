#include <algorithm>
#include <cstdio>
#include <string>
#include <utility>
#include <vector>

typedef long long ll;

const ll SCALE = 100; // coordinates have at most two decimals
const size_t DIGITS = 2;
const ll VOLUME_CENT = SCALE * SCALE; // a hundredth of a volume unit, counted in 1 / SCALE^3
const int WORD = 32;

ll scaled(const char *token) {
    std::string s(token);
    size_t dot = s.find('.');
    std::string whole = s.substr(0, dot), frac;
    if (dot != std::string::npos)
        frac = s.substr(dot + 1);
    frac = (frac + "00").substr(0, DIGITS);
    return (whole.empty() ? 0 : std::stoll(whole)) * SCALE + std::stoll(frac);
}

ll readScaled() {
    char word[WORD];
    if (scanf("%31s", word) != 1)
        return 0;
    return scaled(word);
}

int main() {
    ll u = readScaled(), v = readScaled(), w = readScaled();
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<ll> px, py, pz;
    for (int i = 0; i < n; i++) {
        ll x = readScaled(), y = readScaled(), z = readScaled();
        // a point outside A can never be inside G
        if (x <= u && y <= v && z <= w) {
            px.push_back(x);
            py.push_back(y);
            pz.push_back(z);
        }
    }
    n = px.size();
    std::vector<ll> xs = {0, u};
    for (int i = 0; i < n; i++)
        xs.push_back(px[i]);
    std::sort(xs.begin(), xs.end());
    xs.erase(std::unique(xs.begin(), xs.end()), xs.end());
    ll best = 0;
    for (size_t i = 0; i < xs.size(); i++) {
        for (size_t j = xs.size() - 1; j > i; j--) {
            ll x1 = xs[i], x2 = xs[j], width = x2 - x1;
            if (width * v * w <= best)
                break; // the remaining x2 are closer still
            std::vector<std::pair<ll, ll>> inside;
            for (int p = 0; p < n; p++) {
                if (x1 < px[p] && px[p] < x2)
                    inside.push_back({py[p], pz[p]});
            }
            std::sort(inside.begin(), inside.end());
            int m = inside.size();
            // the lower y face lies on the floor or on a point; the upper
            // face sweeps down from the top, and every point it passes
            // leaves the slab, so neighbouring z gaps merge into one
            for (int k = -1; k < m; k++) {
                ll y1 = k < 0 ? 0 : inside[k].first;
                if (width * (v - y1) * w <= best)
                    break;
                std::vector<ll> zs = {0, w};
                for (int q = k + 1; q < m; q++) {
                    // a point on the floor or the ceiling never splits a gap
                    if (0 < inside[q].second && inside[q].second < w)
                        zs.push_back(inside[q].second);
                }
                std::sort(zs.begin(), zs.end());
                int size = zs.size();
                std::vector<int> prev(size), next(size);
                ll gap = 0;
                for (int t = 0; t < size; t++) {
                    prev[t] = t - 1;
                    next[t] = t + 1;
                    if (t > 0)
                        gap = std::max(gap, zs[t] - zs[t - 1]);
                }
                ll y2 = v;
                for (int q = m - 1; q > k; q--) {
                    best = std::max(best, width * (y2 - y1) * gap);
                    y2 = inside[q].first;
                    if (inside[q].second <= 0 || inside[q].second >= w)
                        continue;
                    int t = std::lower_bound(zs.begin(), zs.end(), inside[q].second) - zs.begin();
                    int lo = prev[t], hi = next[t];
                    next[lo] = hi;
                    prev[hi] = lo;
                    gap = std::max(gap, zs[hi] - zs[lo]);
                }
                best = std::max(best, width * (y2 - y1) * gap);
            }
        }
    }
    ll cents = (best + VOLUME_CENT / 2) / VOLUME_CENT;
    printf("%lld.%02lld\n", cents / SCALE, cents % SCALE);
    return 0;
}
