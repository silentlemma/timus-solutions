#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n, w, h;
    scanf("%d %d %d", &n, &w, &h);
    std::vector<int> x(n), y(n);
    for (int i = 0; i < n; i++)
        scanf("%d %d", &x[i], &y[i]);
    // a largest square slides left and down until its sides meet a tree or
    // the park border, so its corner has x = 0 or a tree x and y = 0 or a tree y
    std::vector<int> xs(x), ys(y);
    xs.push_back(0);
    ys.push_back(0);
    int bestP = 0, bestQ = 0, bestL = 0;
    for (int p : xs) {
        for (int q : ys) {
            int side = std::min(w - p, h - q);
            // a tree up and to the right of the corner is inside unless the
            // side stops at its larger distance
            for (int i = 0; i < n; i++)
                if (x[i] > p && y[i] > q)
                    side = std::min(side, std::max(x[i] - p, y[i] - q));
            if (side > bestL)
                bestP = p, bestQ = q, bestL = side;
        }
    }
    printf("%d %d %d\n", bestP, bestQ, bestL);
}
