#include <iostream>
#include <utility>

std::pair<int, int> solve(int first, int second, int emptyFirst, int emptySecond) {
    return {first - emptyFirst, second - emptySecond};
}

int main() {
    int a1, b1, a2, b2, a3, b3;
    std::cin >> a1 >> b1 >> a2 >> b2 >> a3 >> b3;
    auto result = solve(a1, b1, a3, b2);
    std::cout << result.first << ' ' << result.second << '\n';
}
