#include <algorithm>
#include <cstdio>
const int MAX_STUDENTS = 40;
struct Student {
    int ready, talk, deadline;
};
// at most forty students: fixed storage avoids the heap allocation.
Student students[MAX_STUDENTS];
int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; i++)
        scanf("%d%d%d", &students[i].ready, &students[i].talk, &students[i].deadline);
    std::sort(students, students + n,
              [](const Student &a, const Student &b) { return a.ready < b.ready; });
    // moving the start earlier changes nobody's order or wait, it only adds
    // the same amount to every deadline: the answer is the worst lateness
    int busy = 0, worst = 0;
    for (int i = 0; i < n; i++) {
        busy = std::max(busy, students[i].ready) + students[i].talk;
        worst = std::max(worst, busy - students[i].deadline);
    }
    printf("%d\n", worst);
}
