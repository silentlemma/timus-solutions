#include <cstdio>
#include <vector>

int main() {
    long long limit = 0;
    if (scanf("%lld", &limit) != 1)
        return 0;
    // going back from the last replacement: reach is the longest run that
    // the replacements chosen so far turn into a single space
    std::vector<long long> plan;
    long long reach = 1;
    while (reach < limit) {
        long long step = (reach + 1) / 2 + 1; // the best length to replace here
        long long groups = reach + 2 - step;  // most groups in a run that still fits
        reach = groups * step + step - 2;
        plan.push_back(step);
    }
    printf("%d\n", (int)plan.size());
    for (int i = (int)plan.size() - 1; i >= 0; i--)
        printf("%lld\n", plan[i]);
    return 0;
}
