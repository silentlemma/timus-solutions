#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr std::int64_t kModulus = 1000000007;

std::int64_t seatingCount(int size, const std::vector<int> &requests) {
    if (size == 2)
        return 1;
    std::vector<std::vector<int>> neighbors(size);
    for (int person = 0; person < static_cast<int>(requests.size()); ++person) {
        int target = requests[person];
        const auto &adjacent = neighbors[person];
        if (std::find(adjacent.begin(), adjacent.end(), target) == adjacent.end()) {
            neighbors[person].push_back(target);
            neighbors[target].push_back(person);
            if (neighbors[person].size() > 2 || neighbors[target].size() > 2)
                return 0;
        }
    }
    std::vector<bool> visited(size, false);
    int components = 0, paths = 0;
    for (int start = 0; start < size; ++start) {
        if (visited[start])
            continue;
        std::vector<int> stack{start};
        visited[start] = true;
        int vertices = 0, degrees = 0;
        while (!stack.empty()) {
            int person = stack.back();
            stack.pop_back();
            ++vertices;
            degrees += static_cast<int>(neighbors[person].size());
            for (int target : neighbors[person]) {
                if (!visited[target]) {
                    visited[target] = true;
                    stack.push_back(target);
                }
            }
        }
        if (degrees == 2 * vertices)
            return vertices == size ? 2 : 0;
        ++components;
        paths += vertices > 1;
    }
    std::int64_t answer = 1;
    for (int path = 0; path < paths; ++path)
        answer = answer * 2 % kModulus;
    for (int factor = 2; factor < components; ++factor)
        answer = answer * factor % kModulus;
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, count;
    std::cin >> size >> count;
    std::vector<int> requests(count);
    for (int &target : requests) {
        std::cin >> target;
        --target;
    }
    std::cout << seatingCount(size, requests) << '\n';
}
