#include <algorithm>
#include <array>
#include <cstdio>
#include <functional>

constexpr int ALPHABET = 26;

int main() {
    std::array<int, ALPHABET> counts{};
    int ch = std::getchar();
    while (ch != EOF && ch <= ' ')
        ch = std::getchar();
    for (; ch >= 'a' && ch <= 'z'; ch = std::getchar())
        ++counts[ch - 'a'];
    int limit;
    if (std::scanf("%d", &limit) != 1)
        return 0;
    std::sort(counts.rbegin(), counts.rend());
    int size = 0;
    for (int i = 0; i < limit; ++i)
        size += counts[i];
    int ways = 1;
    const int boundary = counts[limit - 1];
    if (boundary != 0) {
        const auto equal =
            std::equal_range(counts.begin(), counts.end(), boundary, std::greater<int>{});
        const int tied = static_cast<int>(equal.second - equal.first);
        const int selected = limit - static_cast<int>(equal.first - counts.begin());
        for (int i = 1; i <= selected; ++i)
            ways = ways * (tied - i + 1) / i;
    }
    std::printf("%d %d\n", size, ways);
}
