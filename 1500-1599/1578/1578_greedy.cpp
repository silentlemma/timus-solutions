#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int total = n + 2;
    vector<long long> x(total), y(total);
    for (int i = 0; i < total; i++)
        if (scanf("%lld %lld", &x[i], &y[i]) != 2)
            return 0;
    // always run to the farthest point not visited yet: the point before had
    // this one as its farthest, so it was at least as far as the next one,
    // which makes every turn acute
    vector<bool> seen(total, false);
    int at = 0;
    seen[0] = true;
    printf("YES\n1");
    for (int step = 1; step < total; step++) {
        int far = -1;
        long long best = -1;
        for (int j = 0; j < total; j++) {
            long long d = (x[j] - x[at]) * (x[j] - x[at]) + (y[j] - y[at]) * (y[j] - y[at]);
            if (!seen[j] && d > best)
                best = d, far = j;
        }
        seen[far] = true;
        at = far;
        printf(" %d", far + 1);
    }
    printf("\n");
}
