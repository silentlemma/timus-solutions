#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

const int ENDS[] = {1, 2}; // the first and last rows of a best shape are this narrow
const long long SCALE = 8; // no k cells have fewer than sqrt(SCALE k - SHIFT) + 2 neighbours
const long long SHIFT = 4;

long long isqrt(long long n) {
    long long r = (long long)std::sqrt((double)n);
    while (r * r > n)
        r--;
    while ((r + 1) * (r + 1) <= n)
        r++;
    return r;
}

long long capped(const std::vector<int> &full, int cap) {
    long long total = 0;
    for (int w : full)
        total += std::min(w, cap);
    return total;
}

// row widths of a region of k cells with the smallest fence: with row ends
// moving by at most one cell per row the fence is two cells per row plus the
// first and the last row, and no fence is smaller than sqrt(8 k - 4) + 2
std::vector<int> widthsFor(long long k) {
    for (int fence = (int)isqrt(SCALE * k - SHIFT - 1) + 1 + 2;; fence++)
        for (int first : ENDS)
            for (int last : ENDS) {
                int twice = fence - first - last, rows = twice / 2;
                if (twice % 2 != 0 || rows < 1)
                    continue;
                std::vector<int> full;
                if (rows == 1) {
                    if (first == last)
                        full.push_back(first);
                } else {
                    for (int i = 0; i < rows; i++)
                        full.push_back(std::min(first + 2 * i, last + 2 * (rows - 1 - i)));
                }
                if (full.empty() || capped(full, *std::max_element(full.begin(), full.end())) < k)
                    continue;
                // cap the widest rows at the smallest level that holds k cells
                int low = std::max(full.front(), full.back());
                int lo = low, hi = *std::max_element(full.begin(), full.end());
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (capped(full, mid) < k)
                        lo = mid + 1;
                    else
                        hi = mid;
                }
                int cap = lo;
                std::vector<int> widths;
                for (int w : full)
                    widths.push_back(std::min(w, cap));
                long long extra = capped(full, cap) - k;
                std::vector<int> inner;
                for (int i = 1; i + 1 < rows; i++)
                    if (widths[i] == cap)
                        inner.push_back(i);
                if (cap > low && extra <= (long long)inner.size()) {
                    for (long long j = 0; j < extra; j++)
                        widths[inner[j]]--;
                    return widths;
                }
                if (extra == 0)
                    return widths;
            }
}

int main() {
    long long k = 0;
    if (scanf("%lld", &k) != 1)
        return 0;
    std::vector<int> widths = widthsFor(k);
    // place the rows from y = 0 up, the first one starting at x = 0; the ends
    // move by at most one cell, the left one first when the row narrows
    std::vector<int> left(1, 0), right(1, widths[0] - 1);
    for (size_t i = 1; i < widths.size(); i++) {
        int grow = widths[i] - (right.back() - left.back() + 1);
        int dl = grow == 2 ? -1 : (grow < 0 ? 1 : 0);
        left.push_back(left.back() + dl);
        right.push_back(left.back() + widths[i] - 1);
    }
    int top = (int)widths.size() - 1;
    std::vector<std::pair<int, int>> fence;
    for (int x = left[0]; x <= right[0]; x++)
        fence.push_back({x, -1});
    for (int y = 0; y <= top; y++)
        fence.push_back({right[y] + 1, y});
    for (int x = right[top]; x >= left[top]; x--)
        fence.push_back({x, top + 1});
    for (int y = top; y >= 0; y--)
        fence.push_back({left[y] - 1, y});
    std::string out = std::to_string(fence.size()) + "\n";
    for (const auto &c : fence)
        out += std::to_string(c.first) + " " + std::to_string(c.second) + "\n";
    fputs(out.c_str(), stdout);
    return 0;
}
