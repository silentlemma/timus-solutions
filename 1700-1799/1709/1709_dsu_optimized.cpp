#include <cstdio>

const int MAX_AIRPORTS = 100;
int parent[MAX_AIRPORTS];
char plan[MAX_AIRPORTS][MAX_AIRPORTS + 1];

int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

int main() {
    int n;
    long long d, a, cost = 0;
    scanf("%d %lld %lld", &n, &d, &a);
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        for (int j = 0; j < n; ++j)
            plan[i][j] = '0';
    }
    // n <= 100: retain only the plan and stream one input row at a time.
    char row[MAX_AIRPORTS + 1];
    for (int i = 0; i < n; ++i) {
        scanf("%100s", row);
        for (int j = i + 1; j < n; ++j) {
            if (row[j] != '1')
                continue;
            int ri = find(i), rj = find(j);
            if (ri != rj)
                parent[ri] = rj;
            else {
                plan[i][j] = plan[j][i] = 'd';
                cost += d;
            }
        }
    }
    for (int j = 1; j < n; ++j) {
        int ri = find(0), rj = find(j);
        if (ri != rj) {
            parent[rj] = ri;
            plan[0][j] = plan[j][0] = 'a';
            cost += a;
        }
    }
    // up to n(n-1)/2 cancellations at 10^6 each require a 64-bit sum.
    printf("%lld\n", cost);
    for (int i = 0; i < n; ++i)
        puts(plan[i]);
}
