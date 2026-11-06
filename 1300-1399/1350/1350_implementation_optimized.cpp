#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    if (!(std::cin >> size))
        return 0;
    std::vector<std::string> menu(size);
    for (auto &name : menu)
        std::cin >> name;
    std::sort(menu.begin(), menu.end());
    menu.erase(std::unique(menu.begin(), menu.end()), menu.end());
    int students;
    std::cin >> students;
    std::vector<int> seen(menu.size(), -1), risky(students + 1);
    std::vector<unsigned char> safe(menu.size(), 1);
    int safe_count = static_cast<int>(menu.size());
    std::string name;
    for (int student = 0; student <= students; ++student) {
        int count;
        std::cin >> count;
        for (int i = 0; i < count; ++i) {
            std::cin >> name;
            const auto item = std::lower_bound(menu.begin(), menu.end(), name);
            if (item == menu.end() || *item != name)
                continue;
            const auto index = item - menu.begin();
            if (!safe[index] || seen[index] == student)
                continue;
            seen[index] = student;
            if (student == 0) {
                safe[index] = 0;
                --safe_count;
            } else {
                ++risky[student];
            }
        }
    }
    int meal;
    std::cin >> meal;
    for (int student = 1; student <= students; ++student) {
        const int risk = risky[student];
        std::cout << (meal == 0 || risk == 0 ? "YES" : (safe_count - risk < meal ? "NO" : "MAYBE"))
                  << '\n';
    }
}
