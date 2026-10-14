#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

typedef vector<uint64_t> Mat; // boolean matrix, one bitmask per row

Mat multiply(const Mat &x, const Mat &y) {
    Mat out(x.size(), 0);
    for (size_t i = 0; i < x.size(); i++)
        for (size_t j = 0; j < y.size(); j++)
            if (x[i] >> j & 1)
                out[i] |= y[j];
    return out;
}

int main() {
    int n;
    scanf("%d", &n);
    // only whether an entry is zero matters: all entries are non-negative
    Mat a(n, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            int v;
            scanf("%d", &v);
            if (v != 0)
                a[i] |= uint64_t(1) << j;
        }
    int low = n * (n - 1), high = n * (n + 1);
    // A^low by repeated squaring
    Mat cur(n), base = a;
    for (int i = 0; i < n; i++)
        cur[i] = uint64_t(1) << i;
    for (int e = low; e > 0; e >>= 1) {
        if (e & 1)
            cur = multiply(cur, base);
        base = multiply(base, base);
    }
    Mat seen(n, 0);
    for (int k = low; k <= high; k++) {
        for (int i = 0; i < n; i++)
            seen[i] |= cur[i];
        cur = multiply(cur, a);
    }
    uint64_t full = (uint64_t(1) << n) - 1;
    bool positive = true;
    for (uint64_t s : seen)
        positive = positive && s == full;
    puts(positive ? "Yes" : "No");
}
