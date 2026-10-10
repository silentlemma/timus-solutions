#include <iostream>
#include <string>
#include <vector>

int main() {
    const long long WHOLE = 10000, NONE = -1;
    int n;
    std::cin >> n;
    std::vector<long long> given(n, NONE);
    for (auto &g : given) {
        std::string name;
        int shown;
        std::cin >> name >> shown;
        if (shown) {
            std::cin >> g;
        }
    }
    // shares never grow down the list, so an unknown share is at least the
    // next given one (or 1) and at most the last given one before it (or
    // 100%); every total between the two extremes can be reached
    long long low = 0, high = 0, floor = 1, ceiling = WHOLE;
    for (int i = n - 1; i >= 0; i--) {
        floor = given[i] != NONE ? given[i] : floor;
        low += floor;
    }
    for (int i = 0; i < n; i++) {
        ceiling = given[i] != NONE ? given[i] : ceiling;
        high += ceiling;
    }
    std::cout << (low <= WHOLE && WHOLE <= high ? "YES" : "NO") << "\n";
}
