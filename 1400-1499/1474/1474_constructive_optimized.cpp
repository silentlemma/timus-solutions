#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;

    printf("%d\n", n * (n + 2));
    std::vector<std::string> token(2 * n + 1);
    for (int i = 0; i <= 2 * n; ++i)
        token[i] = " " + std::to_string(i);

    int hole = n, direction = 1;
    std::string line;
    for (int run = 0; run <= 2 * n; ++run) {
        int length = std::min({run + 1, n, 2 * n - run + 1});
        // Rising runs slide last and falling runs slide first.
        int slide = run < n ? length - 1 : (run > n ? 0 : -1);
        line.clear();
        for (int i = 0; i < length; ++i) {
            hole += (i == slide ? 1 : 2) * direction;
            line += token[hole];
        }
        size_t skip = run == 0 ? 1 : 0;
        fwrite(line.data() + skip, 1, line.size() - skip, stdout);
        direction = -direction;
    }
    putchar('\n');
}
