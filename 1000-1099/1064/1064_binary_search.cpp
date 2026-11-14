#include <cstdio>
#include <utility>
#include <vector>

const int MAX_LENGTH = 10000;

class Search {
    int target, steps;
    std::vector<bool> path;
    std::vector<std::pair<int, int>> runs;

    int pivot(int length) const {
        int start = 0, gaps = length + 1;
        for (bool right : path) {
            int left = gaps / 2;
            if (right) {
                start += left;
                gaps -= left;
            } else {
                gaps = left;
            }
        }
        return start + gaps / 2 - 1;
    }

    int firstAtLeast(int lo, int hi, int value) const {
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (pivot(mid) < value)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }

    void visit(int lo, int hi, int depth) {
        if (lo >= hi)
            return;
        // The pivot is nondecreasing in the length for a fixed path.
        int first = firstAtLeast(lo, hi, target);
        int after = firstAtLeast(first, hi, target + 1);
        if (depth == steps) {
            if (first < after) {
                if (!runs.empty() && runs.back().second + 1 == first)
                    runs.back().second = after - 1;
                else
                    runs.emplace_back(first, after - 1);
            }
            return;
        }
        path.push_back(true);
        visit(lo, first, depth + 1);
        path.back() = false;
        visit(after, hi, depth + 1);
        path.pop_back();
    }

  public:
    Search(int index, int comparisons) : target(index), steps(comparisons) {}

    void print() {
        visit(target + 1, MAX_LENGTH + 1, 1);
        printf("%zu\n", runs.size());
        for (auto [first, last] : runs)
            printf("%d %d\n", first, last);
    }
};

int main() {
    int target, steps;
    if (scanf("%d %d", &target, &steps) == 2)
        Search(target, steps).print();
}
