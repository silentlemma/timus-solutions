#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> sortOperations(std::vector<int> values) {
    const int n = static_cast<int>(values.size());
    std::vector<int> operations;
    operations.reserve((n - 1) * (2 * n - 1));
    const auto flush = [&]() {
        while (values.back() != n) {
            const int value = values.back();
            std::swap(values.back(), values[value - 1]);
            operations.push_back(value);
        }
    };
    flush();
    int unfixed = n - 1;
    while (unfixed > 0) {
        while (unfixed > 0 && values[unfixed - 1] == unfixed)
            --unfixed;
        if (unfixed == 0)
            break;
        const int start =
            static_cast<int>(std::find(values.begin(), values.end(), 1) - values.begin());
        for (int position = start; position + 1 < n; ++position) {
            std::swap(values[position], values[position + 1]);
            operations.push_back(1);
        }
        flush();
    }
    return operations;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<int> values(n);
    for (auto &value : values)
        std::cin >> value;
    const auto operations = sortOperations(values);
    std::cout << operations.size() << '\n';
    for (int value : operations)
        std::cout << value << '\n';
}
