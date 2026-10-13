#include <cstdio>
#include <vector>

using namespace std;

// key presses from the start to every character, by breadth-first search
vector<int> distances(int n, int m, int start) {
    vector<int> dist(n, -1), queue = {start};
    dist[start] = 0;
    for (size_t h = 0; h < queue.size(); h++) {
        int v = queue[h];
        // left and right run on through the rows; up and down stop at the edges
        int next[] = {(v + n - 1) % n, (v + 1) % n, v >= m ? v - m : v, v + m < n ? v + m : v};
        for (int u : next)
            if (dist[u] < 0) {
                dist[u] = dist[v] + 1;
                queue.push_back(u);
            }
    }
    return dist;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> best;
    long long bestSum = -1;
    for (int s = 0; s < n; s++) {
        vector<int> d = distances(n, m, s);
        long long sum = 0;
        for (int x : d)
            sum += x;
        if (bestSum < 0 || sum < bestSum) {
            bestSum = sum;
            best = d;
        }
    }
    printf("Mean = %.2f\n", (double)bestSum / n);
    for (int i = 0; i < n; i++)
        printf(i % m == m - 1 || i == n - 1 ? "%d\n" : "%d ", best[i]);
}
