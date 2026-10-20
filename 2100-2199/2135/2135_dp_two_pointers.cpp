#include <deque>
#include <iostream>
#include <vector>

struct ProductWindow {
    long long bound;
    long long product = 1;
    int left = 0;

    explicit ProductWindow(long long limit) : bound(limit) {}

    void extend(const std::vector<int> &values, int index) {
        const int value = values[index];
        if (value > bound) {
            left = index + 1;
            product = 1;
            return;
        }
        // Divide first so that the stored product never exceeds the bound.
        while (product > bound / value) {
            product /= values[left++];
        }
        product *= value;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    long long lower, upper;
    if (!(std::cin >> count >> lower >> upper)) {
        return 0;
    }
    std::vector<int> values(count);
    for (int &value : values) {
        std::cin >> value;
    }

    const int unreachable = count + 1;
    std::vector<int> best(count + 1, unreachable);
    best[0] = 0;
    ProductWindow upper_window(upper), lower_window(lower - 1);
    std::deque<int> candidates;
    int next_cut = 0;

    for (int index = 0; index < count; ++index) {
        upper_window.extend(values, index);
        lower_window.extend(values, index);

        // Valid previous cuts form [upper_window.left, lower_window.left).
        while (next_cut < lower_window.left) {
            if (best[next_cut] != unreachable) {
                while (!candidates.empty() && best[candidates.back()] >= best[next_cut]) {
                    candidates.pop_back();
                }
                candidates.push_back(next_cut);
            }
            ++next_cut;
        }
        while (!candidates.empty() && candidates.front() < upper_window.left) {
            candidates.pop_front();
        }
        if (!candidates.empty()) {
            best[index + 1] = best[candidates.front()] + 1;
        }
    }

    std::cout << (best[count] == unreachable ? -1 : best[count]) << '\n';
}
