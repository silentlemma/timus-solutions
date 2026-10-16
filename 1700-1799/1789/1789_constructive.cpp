#include <iostream>
#include <vector>

int main() {
    int n;
    if (!(std::cin >> n)) return 0;
    std::vector<int> touches;
    if (n == 2) {
        touches = {1, 1};
    } else {
        // sweep 2..n-1 and back: the first pass catches one parity of the
        // start, the second pass the other
        for (int p = 2; p <= n - 1; p++) touches.push_back(p);
        for (int p = n - 1; p >= 2; p--) touches.push_back(p);
    }
    std::cout << touches.size() << "\n";
    for (size_t i = 0; i < touches.size(); i++) {
        std::cout << (i ? " " : "") << touches[i];
    }
    std::cout << "\n";
    return 0;
}
