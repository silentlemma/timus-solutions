#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int minimumSheets(const std::vector<int> &clearances) {
    return std::accumulate(clearances.begin(), clearances.end(), 0) +
           *std::max_element(clearances.begin(), clearances.end());
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> clearances(count);
    for (int &clearance : clearances) {
        std::cin >> clearance;
    }
    std::cout << minimumSheets(clearances) << '\n';
    return 0;
}
