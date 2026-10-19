#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<long long> s(n), r(n);
    for (int i = 0; i < n; ++i) scanf("%lld %lld", &s[i], &r[i]);
    // v, u are best friends exactly when every other point lies on the
    // segment vu: all points collinear, v and u the two extreme ones
    int low = 0, high = 0;
    for (int i = 1; i < n; ++i) {
        if ((s[1] - s[0]) * (r[i] - r[0]) != (s[i] - s[0]) * (r[1] - r[0])) {
            printf("0\n");
            return 0;
        }
        if (s[i] < s[low] || (s[i] == s[low] && r[i] < r[low])) low = i;
        if (s[i] > s[high] || (s[i] == s[high] && r[i] > r[high])) high = i;
    }
    printf("1\n%d %d\n", low + 1, high + 1);
}
