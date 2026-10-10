#include <algorithm>
#include <cstdio>
#include <tuple>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::tuple<int, int, int>> students(n);
    for (auto &[ready, talk, deadline] : students) {
        scanf("%d %d %d", &ready, &talk, &deadline);
    }
    std::sort(students.begin(), students.end());
    // moving the start earlier changes nobody's order or wait, it only adds
    // the same amount to every deadline: the answer is the worst lateness
    int busyUntil = 0, worst = 0;
    for (auto [ready, talk, deadline] : students) {
        busyUntil = std::max(busyUntil, ready) + talk;
        worst = std::max(worst, busyUntil - deadline);
    }
    printf("%d\n", worst);
}
