#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;
typedef std::vector<double> Vec;
const ll PRIME = 1000000007;  // independence is decided exactly, modulo this prime
const double ZERO_BAND = 5e-6;  // values that print as 0.00000, kept without a minus

ll power(ll base, ll exp) {
    ll result = 1;
    for (base %= PRIME; exp > 0; exp >>= 1, base = base * base % PRIME) {
        if (exp & 1) {
            result = result * base % PRIME;
        }
    }
    return result;
}

// indices of a maximal linearly independent subset, found by Gaussian
// elimination modulo PRIME, so no rounding decides the rank
std::vector<int> independent(const std::vector<std::vector<ll>>& vectors) {
    std::vector<std::pair<int, std::vector<ll>>> basis;
    std::vector<int> chosen;
    for (int k = 0; k < (int)vectors.size(); k++) {
        std::vector<ll> row(vectors[k].size());
        for (size_t i = 0; i < row.size(); i++) {
            row[i] = ((vectors[k][i] % PRIME) + PRIME) % PRIME;
        }
        for (auto& [pivot, base] : basis) {
            ll f = row[pivot];
            if (f != 0) {
                for (size_t i = 0; i < row.size(); i++) {
                    row[i] = ((row[i] - f * base[i]) % PRIME + PRIME) % PRIME;
                }
            }
        }
        int pivot = -1;
        for (size_t i = 0; i < row.size() && pivot < 0; i++) {
            if (row[i] != 0) {
                pivot = i;
            }
        }
        if (pivot < 0) {
            continue;
        }
        ll inv = power(row[pivot], PRIME - 2);
        for (ll& x : row) {
            x = x * inv % PRIME;
        }
        basis.push_back({pivot, row});
        chosen.push_back(k);
    }
    return chosen;
}

double dot(const Vec& u, const Vec& v) {
    double s = 0;
    for (size_t i = 0; i < u.size(); i++) {
        s += u[i] * v[i];
    }
    return s;
}

// Q and R (by columns) of independent columns: Gram-Schmidt with every
// projection done twice, which keeps Q orthonormal to rounding error
void qr(const std::vector<Vec>& columns, std::vector<Vec>& q, std::vector<Vec>& r) {
    for (const Vec& col : columns) {
        Vec v = col, coef(q.size(), 0.0);
        for (int pass = 0; pass < 2; pass++) {
            for (size_t k = 0; k < q.size(); k++) {
                double c = dot(q[k], v);
                coef[k] += c;
                for (size_t i = 0; i < v.size(); i++) {
                    v[i] -= c * q[k][i];
                }
            }
        }
        double norm = std::sqrt(dot(v, v));
        for (double& x : v) {
            x /= norm;
        }
        q.push_back(v);
        coef.push_back(norm);
        r.push_back(coef);
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<std::vector<ll>> rows(m, std::vector<ll>(n));
    for (auto& row : rows) {
        for (ll& x : row) {
            scanf("%lld", &x);
        }
    }
    Vec b(n);
    for (double& x : b) {
        scanf("%lf", &x);
    }
    // engine i pushes along rows[i]; the thrust is sum of X_i rows[i]. The
    // shortest best X lies in the span of the columns c_j = (rows[i][j])_i
    std::vector<std::vector<ll>> cols(n, std::vector<ll>(m));
    std::vector<Vec> real(n, Vec(m));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cols[j][i] = rows[i][j];
            real[j][i] = rows[i][j];
        }
    }
    std::vector<Vec> picked, basis, unused;
    for (int j : independent(cols)) {
        picked.push_back(real[j]);
    }
    qr(picked, basis, unused);
    // with X = sum of w_k basis[k], the thrust is K w for K[j][k] = c_j . q_k,
    // and K has full column rank: least squares by QR of K
    int size = basis.size();
    std::vector<Vec> kCols(size, Vec(n)), q2, upper;
    for (int k = 0; k < size; k++) {
        for (int j = 0; j < n; j++) {
            kCols[k][j] = dot(real[j], basis[k]);
        }
    }
    qr(kCols, q2, upper);
    Vec w(size);
    for (int i = size - 1; i >= 0; i--) {
        double s = dot(q2[i], b);
        for (int k = i + 1; k < size; k++) {
            s -= upper[k][i] * w[k];
        }
        w[i] = s / upper[i][i];
    }
    for (int i = 0; i < m; i++) {
        double x = 0;
        for (int k = 0; k < size; k++) {
            x += w[k] * basis[k][i];
        }
        if (std::fabs(x) < ZERO_BAND) {
            x = 0;
        }
        printf("%.5f%c", x, i + 1 < m ? ' ' : '\n');
    }
}
