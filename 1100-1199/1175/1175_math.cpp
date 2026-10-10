#include <cstdio>
#include <utility>

typedef long long ll;
typedef std::pair<ll, ll> Pair;

ll a1, a2, a3, a4, b1, b2, c;

Pair step(const Pair &s) {
    ll x = s.first, y = s.second;
    ll h = a1 * x * y + a2 * x + a3 * y + a4;
    if (h > b1 && h > b2 && c > 0) {
        h -= (h - b2 + c - 1) / c * c;
    }
    return {y, h};
}

int main() {
    ll x1, x2;
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld %lld", &a1, &a2, &a3, &a4, &b1, &b2, &c, &x1,
          &x2);
    // the next term depends only on the last two, so the pairs of
    // neighbouring terms run into a cycle; Brent's method finds it in O(1)
    // memory: the length first, then where it starts
    ll power = 1, length = 1;
    Pair slow = {x1, x2}, fast = step(slow);
    while (slow != fast) {
        if (power == length) {
            slow = fast;
            power *= 2;
            length = 0;
        }
        fast = step(fast);
        length++;
    }
    slow = fast = {x1, x2};
    for (ll k = 0; k < length; k++) {
        fast = step(fast);
    }
    ll start = 1;
    while (slow != fast) {
        slow = step(slow);
        fast = step(fast);
        start++;
    }
    printf("%lld %lld\n", start, length);
}
