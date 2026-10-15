#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    long long d;
    if (scanf("%d %lld", &n, &d) != 2)
        return 0;
    // sell to everyone who can be served: by the end of month i at most
    // i * d yachts exist, so the running total of sales is capped there
    vector<long long> sales(n);
    long long total = 0;
    for (int i = 1; i <= n; i++) {
        long long a;
        if (scanf("%lld", &a) != 1)
            return 0;
        long long next = min(total + a, i * d);
        sales[i - 1] = next - total;
        total = next;
    }
    // build every yacht as late as possible: going backwards, whatever a
    // month cannot build is built earlier and waits one month per boundary
    long long carry = 0, storage = 0;
    for (int i = n - 1; i >= 0; i--) {
        storage += carry;
        carry = max(0LL, sales[i] + carry - d);
    }
    printf("%lld %lld\n", total, storage);
}
