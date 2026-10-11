#include <cstdio>
#include <cstdlib>
#include <vector>

const long long INF = 1LL << 60;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<int> bx(n), by(n), bw(n), sx(m), sy(m), cap(m), load(m, 0);
    for (int i = 0; i < n; i++)
        scanf("%d %d %d", &bx[i], &by[i], &bw[i]);
    for (int j = 0; j < m; j++)
        scanf("%d %d %d", &sx[j], &sy[j], &cap[j]);
    std::vector<std::vector<int>> plan(n, std::vector<int>(m)), dist(n, std::vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            scanf("%d", &plan[i][j]);
            load[j] += plan[i][j];
            dist[i][j] = std::abs(bx[i] - sx[j]) + std::abs(by[i] - sy[j]) + 1;
        }
    // nodes 0..m-1 are shelters and m is the spare room; j -> k moves one
    // worker of some building from shelter j to k, j -> m uses a free place
    // at j, and m -> k lets shelter k end up one worker short
    int v = m + 1;
    std::vector<std::vector<long long>> w(v, std::vector<long long>(v, INF));
    std::vector<std::vector<int>> via(v, std::vector<int>(v, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (plan[i][j] == 0)
                continue;
            for (int k = 0; k < m; k++) {
                long long c = dist[i][k] - dist[i][j];
                if (k != j && c < w[j][k])
                    w[j][k] = c, via[j][k] = i;
            }
        }
    for (int j = 0; j < m; j++) {
        if (load[j] < cap[j])
            w[j][m] = 0;
        w[m][j] = 0;
    }
    // Bellman-Ford from all nodes at once; a change in round v means a
    // negative cycle, which the predecessors lead into
    std::vector<long long> d(v, 0);
    std::vector<int> pred(v, 0);
    int last = -1;
    for (int round = 0; round < v; round++) {
        last = -1;
        for (int j = 0; j < v; j++)
            for (int k = 0; k < v; k++)
                if (w[j][k] < INF && d[j] + w[j][k] < d[k]) {
                    d[k] = d[j] + w[j][k];
                    pred[k] = j;
                    last = k;
                }
        if (last < 0)
            break;
    }
    if (last < 0) {
        puts("OPTIMAL");
        return 0;
    }
    for (int step = 0; step < v; step++)
        last = pred[last];
    // shift one worker along each shelter-to-shelter edge of the cycle
    int k = last;
    do {
        int j = pred[k];
        if (j < m && k < m) {
            plan[via[j][k]][j]--;
            plan[via[j][k]][k]++;
        }
        k = j;
    } while (k != last);
    puts("SUBOPTIMAL");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            printf("%d%c", plan[i][j], j + 1 < m ? ' ' : '\n');
}
