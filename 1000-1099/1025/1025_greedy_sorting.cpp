#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 1;
    std::vector<int> size(k);
    for (int &s : size)
        if (scanf("%d", &s) != 1)
            return 1;
    // win a majority of the groups, choosing the smallest ones; a group of s
    // voters needs s / 2 + 1 supporters
    std::sort(size.begin(), size.end());
    int supporters = 0;
    for (int i = 0; i <= k / 2; i++)
        supporters += size[i] / 2 + 1;
    printf("%d\n", supporters);
}
