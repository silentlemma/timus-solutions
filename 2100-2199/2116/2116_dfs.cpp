#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

int main() {
    long long n;
    int a, b;
    std::cin >> n >> a >> b;
    if (b == 0) {
        std::cout << n * n << '\n';
        return 0;
    }

    // Each move invariant is connected inside a board of side 2 * b.
    const int side = static_cast<int>(std::min(n, 2LL * b));
    std::vector<std::pair<int, int>> moves;
    for (int dx : {-a, a}) {
        for (int dy : {-b, b}) {
            moves.emplace_back(dx, dy);
            moves.emplace_back(dy, dx);
        }
    }

    std::vector<bool> seen(side * side, false);
    std::vector<int> stack;
    int components = 0;
    for (int start = 0; start < side * side; ++start) {
        if (seen[start]) {
            continue;
        }
        ++components;
        seen[start] = true;
        stack.push_back(start);
        while (!stack.empty()) {
            const int cell = stack.back();
            stack.pop_back();
            for (const auto &move : moves) {
                const int x = cell / side + move.first;
                const int y = cell % side + move.second;
                if (x < 0 || x >= side || y < 0 || y >= side) {
                    continue;
                }
                const int next = x * side + y;
                if (!seen[next]) {
                    seen[next] = true;
                    stack.push_back(next);
                }
            }
        }
    }
    std::cout << components << '\n';
}
