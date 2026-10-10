#include <cstdio>
#include <vector>

int main() {
    const int TIME = 30000;
    int n;
    scanf("%d", &n);
    // the latest start among the talks that end at each minute
    std::vector<int> latest(TIME + 1, 0);
    for (int i = 0; i < n; i++) {
        int s, e;
        scanf("%d %d", &s, &e);
        if (s > latest[e]) {
            latest[e] = s;
        }
    }
    // take the talk that ends first among those starting after the last one
    int count = 0, last = 0;
    for (int e = 1; e <= TIME; e++) {
        if (latest[e] > last) {
            count++;
            last = e;
        }
    }
    printf("%d\n", count);
}
