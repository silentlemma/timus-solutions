#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
const ll MOD = 1000000007;

ll power(ll b, ll e) {
    ll r = 1;
    for (b %= MOD; e > 0; e >>= 1, b = b * b % MOD)
        if (e & 1)
            r = r * b % MOD;
    return r;
}

// monic polynomial, lowest coefficient first, whose roots are
// 4 cos^2(j pi / (m + 1)) for j = 1 .. ceil(m / 2)
vector<ll> rootsPoly(int m) {
    // S_k(x) = U_k(x / 2) grows by S_(k+1) = x S_k - S_(k-1) from S_0 = 1 and
    // S_1 = x, and its roots are 2 cos(j pi / (m + 1)) for j = 1 .. m
    vector<ll> prev = {1}, cur = {0, 1};
    for (int k = 1; k < m; k++) {
        vector<ll> next(cur.size() + 1, 0);
        for (size_t i = 0; i < cur.size(); i++)
            next[i + 1] = cur[i];
        for (size_t i = 0; i < prev.size(); i++)
            next[i] = (next[i] - prev[i] + MOD) % MOD;
        prev = cur;
        cur = next;
    }
    // the roots come in pairs +-x, plus 0 when m is odd, so an extra factor x
    // when m is odd makes every power even, and x^2 -> y keeps one per pair
    if (m % 2 == 1)
        cur.insert(cur.begin(), 0);
    vector<ll> result;
    for (size_t i = 0; i < cur.size(); i += 2)
        result.push_back(cur[i]);
    return result;
}

ll det(vector<vector<ll>> a) {
    int size = a.size();
    ll result = 1;
    for (int col = 0; col < size; col++) {
        int pivot = col;
        while (pivot < size && a[pivot][col] == 0)
            pivot++;
        if (pivot == size)
            return 0;
        if (pivot != col) {
            swap(a[pivot], a[col]);
            result = (MOD - result) % MOD;
        }
        result = result * a[col][col] % MOD;
        ll inv = power(a[col][col], MOD - 2);
        for (int r = col + 1; r < size; r++) {
            ll f = a[r][col] * inv % MOD;
            if (f == 0)
                continue;
            for (int c = col; c < size; c++)
                a[r][c] = ((a[r][c] - f * a[col][c]) % MOD + MOD) % MOD;
        }
    }
    return result;
}

// Res(p, q) as the determinant of the Sylvester matrix
ll resultant(const vector<ll> &p, const vector<ll> &q) {
    int d = p.size() - 1, e = q.size() - 1, size = d + e;
    vector<vector<ll>> rows;
    for (int i = 0; i < e; i++) {
        vector<ll> row(size, 0);
        for (int k = 0; k <= d; k++)
            row[i + k] = p[d - k];
        rows.push_back(row);
    }
    for (int i = 0; i < d; i++) {
        vector<ll> row(size, 0);
        for (int k = 0; k <= e; k++)
            row[i + k] = q[e - k];
        rows.push_back(row);
    }
    return det(rows);
}

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 0;
    // Kasteleyn: the number of tilings is the product of a_j + b_k over the
    // roots a_j of rootsPoly(m) and b_k of rootsPoly(n), which is the
    // resultant of the first with the monic polynomial whose roots are -b_k
    vector<ll> p = rootsPoly(m), q = rootsPoly(n);
    // (-1)^e q(-y) is monic with roots -b_k: coefficient i gets (-1)^(e - i)
    int e = q.size() - 1;
    for (int i = 0; i <= e; i++)
        if ((e - i) % 2 == 1)
            q[i] = (MOD - q[i]) % MOD;
    printf("%lld\n", resultant(p, q));
}
