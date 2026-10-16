#include <algorithm>
#include <cstdio>
#include <vector>

const int STEPS = 100;

int n;
std::vector<long long> mass, purity;
std::vector<int> order;

// gold, in grams times a thousand, in the first t grams of the bars laid
// out from the poorest to the richest
double goldBefore(double t) {
    double gold = 0;
    for (int i : order) {
        double part = std::min((double)mass[i], t);
        if (part <= 0) break;
        gold += part * purity[i];
        t -= part;
    }
    return gold;
}

int main() {
    long long need, fineness;
    if (scanf("%d %lld %lld", &n, &need, &fineness) < 1) return 0;
    mass.resize(n);
    purity.resize(n);
    long long total = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &mass[i], &purity[i]);
        total += mass[i];
        order.push_back(i);
    }
    std::stable_sort(order.begin(), order.end(),
                     [](int a, int b) { return purity[a] < purity[b]; });
    double target = (double)need * fineness;
    auto window = [&](double s) { return goldBefore(s + need) - goldBefore(s); };
    // a window of the needed weight sliding from the poorest end to the
    // richest gains gold steadily, so it hits the target if anything does
    if (total < need || window(0) > target || window(total - need) < target) {
        puts("NO");
        return 0;
    }
    double low = 0, high = total - need;
    for (int step = 0; step < STEPS; step++) {
        double mid = (low + high) / 2;
        if (window(mid) < target) low = mid;
        else high = mid;
    }
    double start = (low + high) / 2;
    std::vector<double> take(n, 0);
    double left = 0;
    for (int i : order) {
        double right = left + mass[i];
        take[i] = std::max(0.0, std::min(right, start + need) - std::max(left, start));
        left = right;
    }
    puts("YES");
    for (int i = 0; i < n; i++) printf("%.10f\n", take[i]);
    return 0;
}
