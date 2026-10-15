#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const int TOLL = 1000;

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> people(n);
    for (int& x : people) {
        scanf("%d", &x);
    }
    if (n == 2) {
        printf("1 2\n");
        return 0;
    }
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    auto smaller = [&](int a, int b) { return people[a] < people[b]; };
    std::stable_sort(order.begin(), order.end(), smaller);
    std::vector<long long> p(n), q(n);
    for (int i = 0; i < n; i++) {
        p[i] = people[order[i]];
        q[i] = TOLL / p[i];
    }
    // towns sorted by size: the best tour climbs to the last town on one path
    // and comes back on the other; up[j] costs a climb ending at the newest
    // town and a return ending at town j, down[j] the other way round
    std::vector<long long> up = {q[0] * p[1]}, down = {q[1] * p[0]};
    long long shiftUp = 0, shiftDown = 0;
    std::vector<int> fromDown = {0, 0}, fromUp = {0, 0};
    for (int m = 1; m < n - 2; m++) {
        int nxt = m + 1, bestUp = 0, bestDown = 0;
        for (int j = 1; j < m; j++) {
            if (down[j] + q[j] * p[nxt] < down[bestUp] + q[bestUp] * p[nxt]) {
                bestUp = j;
            }
            if (up[j] + q[nxt] * p[j] < up[bestDown] + q[nxt] * p[bestDown]) {
                bestDown = j;
            }
        }
        long long newUp = down[bestUp] + shiftDown + q[bestUp] * p[nxt];
        long long newDown = up[bestDown] + shiftUp + q[nxt] * p[bestDown];
        shiftUp += q[m] * p[nxt];
        shiftDown += q[nxt] * p[m];
        up.push_back(newUp - shiftUp);
        down.push_back(newDown - shiftDown);
        fromDown.push_back(bestUp);
        fromUp.push_back(bestDown);
    }
    int last = n - 1, m = n - 2;
    bool climbing = true;
    int j = 0;
    long long best = -1;
    for (int k = 0; k < m; k++) {
        long long closeUp = up[k] + shiftUp + q[m] * p[last] + q[last] * p[k];
        long long closeDown = down[k] + shiftDown + q[k] * p[last] + q[last] * p[m];
        if (best < 0 || closeUp < best) {
            best = closeUp, climbing = true, j = k;
        }
        if (closeDown < best) {
            best = closeDown, climbing = false, j = k;
        }
    }
    // walk back: town m is on the climbing path or not, the other path ends at j
    std::vector<bool> onUp(n, false);
    for (; m >= 1; m--) {
        onUp[m] = climbing;
        if (j == m - 1) {
            j = climbing ? fromDown[m] : fromUp[m];
            climbing = !climbing;
        }
    }
    std::vector<int> tour = {0};
    for (int k = 1; k < n - 1; k++) {
        if (onUp[k]) {
            tour.push_back(k);
        }
    }
    tour.push_back(n - 1);
    for (int k = n - 2; k >= 1; k--) {
        if (!onUp[k]) {
            tour.push_back(k);
        }
    }
    int start = 0;
    for (int i = 0; i < n; i++) {
        tour[i] = order[tour[i]];
        if (tour[i] == 0) {
            start = i;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d%c", tour[(start + i) % n] + 1, i + 1 < n ? ' ' : '\n');
    }
}
