#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;
// a cost is pegs * PEG + inches cut: fewer pegs first, then less cutting
const ll PEG = 1000000, NONE = -1;

struct Shelf {
    ll y, left, length, a, b;
};

// cheapest way to get a shelf out of the open strip (lo, hi) of the tome,
// keeping its plank inside the niche [0, width]
ll clear(const Shelf &s, ll lo, ll hi, ll width) {
    if (s.left + s.length <= lo || s.left >= hi) {
        return 0;
    }
    ll best = 2 * PEG + s.length;
    for (auto [start, end] : {std::pair<ll, ll>{0, lo}, {hi, width}}) {
        // pegs stay: a plank of length t in [start, end] over both pegs with
        // its middle between them exists for b - a <= t <= this bound
        if (start <= s.a && s.b <= end) {
            ll longest = std::min({s.length, 2 * (s.b - start), end - start, 2 * (end - s.a)});
            if (longest >= s.b - s.a) {
                best = std::min(best, s.length - longest);
            }
        }
        // one peg moves anywhere, so only the kept peg and the room matter
        bool kept = (start <= s.a && s.a <= end) || (start <= s.b && s.b <= end);
        if (end > start && kept) {
            best = std::min(best, PEG + std::max(0LL, s.length - (end - start)));
        }
    }
    return best;
}

// cost of making a shelf hold the tome over [x, x + tome], or NONE
ll carry(const Shelf &s, ll x, ll tome, ll width) {
    if (s.length < tome) {
        return NONE;
    }
    // pegs stay: limits on the new left end, doubled to stay in integers
    ll low = std::max({0LL, 2 * (s.b - s.length), 2 * s.a - s.length, 2 * (x + tome - s.length)});
    ll high = std::min({2 * s.a, 2 * x, 2 * s.b - s.length, 2 * (width - s.length)});
    if (low <= high) {
        return 0;
    }
    // one peg moves: the plank only has to reach over the tome and the peg
    // that stays
    for (ll p : {s.a, s.b}) {
        if (std::max(x + tome, p) - std::min(x, p) <= s.length) {
            return PEG;
        }
    }
    return NONE;
}

int main() {
    ll width, height, tomeW, tomeH;
    int n;
    scanf("%lld %lld %lld %lld %d", &width, &height, &tomeW, &tomeH, &n);
    std::vector<Shelf> shelves(n);
    for (auto &s : shelves) {
        ll x1, x2;
        scanf("%lld %lld %lld %lld %lld", &s.y, &s.left, &s.length, &x1, &x2);
        s.a = s.left + x1;
        s.b = s.left + x2;
    }
    std::sort(shelves.begin(), shelves.end(),
              [](const Shelf &p, const Shelf &q) { return p.y < q.y; });
    int spots = width - tomeW + 1;
    // prefix[k][x]: total cost of clearing the strip at x from the k lowest
    // shelves
    std::vector<std::vector<ll>> prefix(n + 1, std::vector<ll>(spots, 0));
    for (int k = 0; k < n; k++) {
        for (int x = 0; x < spots; x++) {
            prefix[k + 1][x] = prefix[k][x] + clear(shelves[k], x, x + tomeW, width);
        }
    }
    ll best = NONE;
    for (int i = 0; i < n; i++) {
        ll y = shelves[i].y;
        if (y + tomeH > height) {
            continue;
        }
        // the shelves strictly between the tome bottom and top are in the way
        int top = i + 1;
        while (top < n && shelves[top].y < y + tomeH) {
            top++;
        }
        for (int x = 0; x < spots; x++) {
            ll base = carry(shelves[i], x, tomeW, width);
            if (base != NONE) {
                ll total = base + prefix[top][x] - prefix[i + 1][x];
                if (best == NONE || total < best) {
                    best = total;
                }
            }
        }
    }
    printf("%lld %lld\n", best / PEG, best % PEG);
}
