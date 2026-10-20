#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string x, y;
    std::cin >> x >> y;
    const std::size_t size = std::max(x.size(), y.size());
    x.insert(0, size - x.size(), '0');
    y.insert(0, size - y.size(), '0');

    int propagating = 0;
    int longest = 0;
    for (std::size_t i = 0; i < size; ++i) {
        if (x[i] != y[i]) {
            ++propagating;
        } else {
            // A common one starts a carry through the differing bits above it.
            if (x[i] == '1') {
                longest = std::max(longest, propagating + 1);
            }
            propagating = 0;
        }
    }
    // Include the initial call and the final call with a zero second argument.
    std::cout << longest + 2 << '\n';
}
