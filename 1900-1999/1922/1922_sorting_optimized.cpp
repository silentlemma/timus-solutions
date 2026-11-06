#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int INDEX_BITS = 10;
constexpr int INDEX_MASK = (1 << INDEX_BITS) - 1;

int main() {
    int size;
    if (std::scanf("%d", &size) != 1)
        return 0;
    std::vector<int> ordered(size);
    for (int i = 0; i < size; ++i) {
        int threshold;
        std::scanf("%d", &threshold);
        ordered[i] = (threshold << INDEX_BITS) | (i + 1);
    }
    std::sort(ordered.begin(), ordered.end());
    std::vector<int> sizes;
    for (int count = 1; count <= size; ++count) {
        if ((ordered[count - 1] >> INDEX_BITS) <= count &&
            (count == size || (ordered[count] >> INDEX_BITS) > count + 1))
            sizes.push_back(count);
    }
    std::printf("%zu\n", sizes.size());
    for (int count : sizes) {
        std::printf("%d", count);
        for (int i = 0; i < count; ++i)
            std::printf(" %d", ordered[i] & INDEX_MASK);
        std::puts("");
    }
}
