#include <cstdio>
#include <vector>

int main() {
    int a = 0, b = 0;
    if (scanf("%d %d", &a, &b) != 2)
        return 0;
    std::vector<int> f(b - a + 1);
    for (int &v : f) {
        if (scanf("%d", &v) != 1)
            return 0;
    }
    int pieces = 0, n = (int)f.size();
    for (int i = 0; i < n;) {
        // stretch this piece while it stays monotone; its way up or down is
        // fixed by its first step that is not flat
        pieces++;
        int way = 0, j = i;
        for (; j + 1 < n; j++) {
            int step = (f[j + 1] > f[j]) - (f[j + 1] < f[j]);
            if (step != 0 && way != 0 && step != way)
                break;
            if (way == 0)
                way = step;
        }
        i = j + 1;
    }
    printf("%d\n", pieces);
    return 0;
}
