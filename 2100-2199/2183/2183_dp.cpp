#include <algorithm>
#include <cstdio>

int main() {
    int n, value;
    if (scanf("%d %d", &n, &value) != 2)
        return 0;
    int untouched = value, ending = -value, used = ending;
    // Ending flips the last value. Used allows the flip to end anywhere.
    for (int i = 1; i < n; ++i) {
        scanf("%d", &value);
        ending = std::min(-value, std::max(ending, untouched));
        used = std::max(ending, std::min(value, used));
        untouched = std::min(value, untouched);
    }
    printf("%d\n", used);
}
