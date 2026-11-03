#include <algorithm>
#include <cstdio>
#include <vector>

const int PERCENT = 100;

int main() {
    int n, start;
    scanf("%d %d", &n, &start);
    if (start > n) {
        puts("0");
        return 0;
    }
    std::vector<int> jobs(n + 1);
    jobs[start] = 1;
    int answer = 1;
    // Salaries form a DAG. Divisibility tests the exact percentage.
    // the subtracted old salary contributes an integer100percent.
    for (int salary = start; salary <= n; salary++) {
        if (!jobs[salary])
            continue;
        answer = std::max(answer, jobs[salary]);
        for (int following = salary + 1; following <= n; following++)
            if (PERCENT * following % salary == 0)
                jobs[following] = std::max(jobs[following], jobs[salary] + 1);
    }
    printf("%d\n", answer);
}
