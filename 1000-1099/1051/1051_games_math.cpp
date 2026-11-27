#include <algorithm>
#include <cstdio>

// In 2D, neighbouring stones enable three-column/row reductions; isolated rows are separate.
const int GROUP = 3;

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 0;
    int answer;
    if (std::min(m, n) == 1)
        answer = (std::max(m, n) + 1) / 2;
    else
        answer = m % GROUP == 0 || n % GROUP == 0 ? 2 : 1;
    printf("%d\n", answer);
}
