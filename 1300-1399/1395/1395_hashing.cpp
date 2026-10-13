#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int TABLE = 1 << 15; // over three times the number of values: short probes
const unsigned HASH = 2654435761u;
const long long MAX_VALUE = 1000000000;

int keys[TABLE], where[TABLE]; // a value and its first position, or position 0 for empty

int slot(int v) {
    unsigned h = (unsigned)v * HASH % TABLE;
    while (where[h] && keys[h] != v)
        h = (h + 1) % TABLE;
    return h;
}

// the position of a value, or 0 when it is not there
int find(long long v) {
    if (v < 1 || v > MAX_VALUE)
        return 0;
    return where[slot((int)v)];
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a;
    for (int i = 1; i <= n; i++) {
        int v;
        scanf("%d", &v);
        int h = slot(v);
        if (!where[h]) {
            keys[h] = v;
            where[h] = i;
            a.push_back(v);
        }
    }
    sort(a.begin(), a.end());
    int m = a.size(), best = min(m, 2), first = a[0];
    long long step = m > 1 ? a[1] - a[0] : 0;
    // a progression is walked only from its smallest element, so every pair of
    // neighbours in a progression is visited once: O(n^2) look-ups in all
    for (int i = 0; i + best < m; i++)
        for (int j = i + 1; j < m; j++) {
            long long d = a[j] - a[i];
            if (a[i] + best * d > a[m - 1])
                break; // larger differences cannot beat the best either
            if (!find(a[j] + d) || find(a[i] - d))
                continue; // no third element, or not the smallest one
            int length = 2;
            for (long long x = a[j] + d; find(x); x += d)
                length++;
            if (length > best) {
                best = length;
                first = a[i];
                step = d;
            }
        }
    printf("%d\n", best);
    for (int k = 0; k < best; k++)
        printf(k + 1 < best ? "%d " : "%d\n", find(first + k * step));
}
