#include <algorithm>
#include <iostream>

int main() {
    int k, n;
    if (!(std::cin >> k >> n)) return 0;
    int jam = 0;
    for (int i = 0; i < n; i++) {
        int cars;
        std::cin >> cars;
        // the light lets k cars through, but never more than are waiting
        jam = std::max(0, jam + cars - k);
    }
    std::cout << jam << "\n";
    return 0;
}
