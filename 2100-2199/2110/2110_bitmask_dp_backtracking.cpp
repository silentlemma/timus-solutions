#include <algorithm>
#include <iostream>
#include <vector>

constexpr int SMALL_REMOVALS = 7;

class Search {
    const std::vector<int> &values;
    std::vector<int> suffix;
    int best = 0;

    void visit(int index, int needed, int current) {
        if (needed == 0) {
            best = std::max(best, current);
            return;
        }
        int upper = current | suffix[index];
        if (upper <= best) {
            return;
        }
        int remaining = static_cast<int>(values.size()) - index;
        // One witness per uncovered bit suffices; extra elements can fill the selection.
        if (needed == remaining || needed >= __builtin_popcount(suffix[index] & ~current)) {
            best = upper;
            return;
        }
        visit(index + 1, needed - 1, current | values[index]);
        visit(index + 1, needed, current);
    }

  public:
    Search(const std::vector<int> &input, int kept) : values(input), suffix(input.size() + 1) {
        for (int i = static_cast<int>(values.size()) - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] | values[i];
        }
        for (int i = 0; i < kept; ++i) {
            best |= values[i];
        }
    }

    int solve(int kept) {
        visit(0, kept, 0);
        return best;
    }
};

int solve_dp(const std::vector<int> &values, int kept, int full) {
    std::vector<int> count(full + 1, kept + 1);
    count[0] = 0;
    int upper = 0;
    int best = 0;
    for (int value : values) {
        // OR never decreases a mask, so descending updates use each element at most once.
        for (int mask = upper; mask >= 0; --mask) {
            if (count[mask] < kept) {
                int merged = mask | value;
                count[merged] = std::min(count[merged], count[mask] + 1);
                best = std::max(best, merged);
            }
        }
        upper |= value;
        if (best == full) {
            break;
        }
    }
    return best;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, removed;
    std::cin >> n >> removed;
    std::vector<int> values(n);
    int full = 0;
    for (int &value : values) {
        std::cin >> value;
        full |= value;
    }
    int kept = n - removed;
    int answer = full;
    if (kept < __builtin_popcount(static_cast<unsigned int>(full))) {
        std::sort(values.rbegin(), values.rend());
        if (removed <= SMALL_REMOVALS) {
            answer = Search(values, kept).solve(kept);
        } else {
            values.erase(std::unique(values.begin(), values.end()), values.end());
            answer = solve_dp(values, kept, full);
        }
    }
    std::cout << answer << '\n';
}
