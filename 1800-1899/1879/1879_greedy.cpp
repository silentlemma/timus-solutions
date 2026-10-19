#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

const int LETTERS = 100000;

vector<ll> read_counts(ll& length) {
    vector<ll> count(LETTERS + 1, 0);
    scanf("%lld", &length);
    for (ll i = 0; i < length; i++) {
        int c;
        scanf("%d", &c);
        count[c]++;
    }
    return count;
}

int main() {
    ll n, m;
    vector<ll> a = read_counts(n), b = read_counts(m);
    // every position of t meets every position of the cyclic s exactly once,
    // so the distance is n m minus the number of equal pairs
    ll p = a[0], q = b[0];
    a[0] = b[0] = 0;
    ll equal = 0, same = 0;
    for (int c = 1; c <= LETTERS; c++) {
        equal += a[c] * b[c];
        same = max(same, p * b[c] + q * a[c]);
    }
    // the gain is linear in the letters chosen for the question marks of one
    // string, so all of them take one letter: the same letter for both
    // strings, or the best letter for each
    same += p * q;
    ll apart = p * *max_element(b.begin(), b.end()) + q * *max_element(a.begin(), a.end());
    printf("%lld\n", n * m - equal - max(same, apart));
    return 0;
}
