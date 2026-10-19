#include <algorithm>
#include <iostream>
#include <vector>

std::vector<long long> solve(long long x, long long y, long long total) {
    long long a = std::min(x, total), b = total - a;
    if (b > y)
        return {};
    return {a, b};
}

int main() {
    long long x, y, total;
    if (!(std::cin >> x >> y >> total))
        return 0;
    auto answer = solve(x, y, total);
    if (answer.empty())
        std::cout << "Impossible\n";
    else
        std::cout << answer[0] << ' ' << answer[1] << '\n';
}
