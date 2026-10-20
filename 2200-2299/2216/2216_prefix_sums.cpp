#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int floors, elevators;
    std::cin >> floors >> elevators;
    std::vector<int> difference(floors + 1, 0);
    for (int i = 0; i < elevators; ++i) {
        int left, right;
        std::cin >> left >> right;
        ++difference[left];
        --difference[right];
    }
    if (floors == 1) {
        std::cout << -1 << '\n';
        return 0;
    }

    int crossing = 0;
    int answer = elevators;
    // Every route crosses each gap; cover all elevators crossing the cheapest gap.
    for (int floor = 1; floor < floors; ++floor) {
        crossing += difference[floor];
        answer = std::min(answer, crossing);
    }
    std::cout << answer << '\n';
}
