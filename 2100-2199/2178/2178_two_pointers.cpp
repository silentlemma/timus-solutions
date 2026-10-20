#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

constexpr int MAX_VALUE = 100000;
constexpr int BASE_SIZE = 16;

class Solver {
    vector<int> values, limit, minimum, maximum, frequency;

    long long mixed(int left, int middle, int right, int sign) {
        const auto &low = sign == 1 ? minimum : maximum;
        const auto &high = sign == 1 ? maximum : minimum;
        const int offset = sign == 1 ? 0 : MAX_VALUE;
        int lower = middle, upper = middle - 1, threshold = upper, current = lower;
        long long answer = 0;
        for (int i = middle - 1; i >= left; --i) {
            while (lower < right && sign * low[lower] >= sign * low[i]) {
                ++lower;
            }
            while (threshold + 1 < right && sign * high[threshold + 1] < sign * high[i]) {
                ++threshold;
            }
            int target = min(threshold, limit[i]);
            while (upper < target) {
                ++upper;
                if (upper >= current) {
                    ++frequency[sign * low[upper] + upper + offset];
                }
            }
            while (upper > target) {
                if (upper >= current) {
                    --frequency[sign * low[upper] + upper + offset];
                }
                --upper;
            }
            while (current < lower) {
                if (current <= upper) {
                    --frequency[sign * low[current] + current + offset];
                }
                ++current;
            }
            answer += frequency[sign * high[i] + i + offset];
        }
        for (int j = middle; j < right; ++j) {
            frequency[sign * low[j] + j + offset] = 0;
        }
        return answer;
    }

    long long count(int left, int right) {
        long long answer = 0;
        if (right - left <= BASE_SIZE) {
            for (int i = left; i < right; ++i) {
                int low = values[i], high = values[i];
                for (int j = i; j < right && j <= limit[i]; ++j) {
                    low = min(low, values[j]);
                    high = max(high, values[j]);
                    answer += high - low == j - i;
                }
            }
            return answer;
        }
        const int middle = left + (right - left) / 2;
        answer = count(left, middle) + count(middle, right);
        while (left < middle && limit[left] < middle) {
            ++left;
        }
        right = min(right, limit[middle - 1] + 1);
        if (left == middle || right == middle) {
            return answer;
        }
        minimum[middle - 1] = maximum[middle - 1] = values[middle - 1];
        for (int i = middle - 2; i >= left; --i) {
            minimum[i] = min(minimum[i + 1], values[i]);
            maximum[i] = max(maximum[i + 1], values[i]);
        }
        minimum[middle] = maximum[middle] = values[middle];
        for (int j = middle + 1; j < right; ++j) {
            minimum[j] = min(minimum[j - 1], values[j]);
            maximum[j] = max(maximum[j - 1], values[j]);
        }
        // If both extrema lie in one half, the other endpoint is determined.
        for (int i = left; i < middle; ++i) {
            int j = i + maximum[i] - minimum[i];
            if (j >= middle && j < right && j <= limit[i] && maximum[j] < maximum[i] &&
                minimum[j] > minimum[i]) {
                ++answer;
            }
        }
        for (int j = middle; j < right; ++j) {
            int i = j - maximum[j] + minimum[j];
            if (i >= left && i < middle && j <= limit[i] && maximum[i] < maximum[j] &&
                minimum[i] > minimum[j]) {
                ++answer;
            }
        }
        // Negating values exchanges the two cases with extrema in opposite halves.
        return answer + mixed(left, middle, right, 1) + mixed(left, middle, right, -1);
    }

  public:
    explicit Solver(vector<int> input)
        : values(move(input)), limit(values.size()), minimum(values.size()), maximum(values.size()),
          frequency(MAX_VALUE + values.size() + 1) {
        const int n = static_cast<int>(values.size());
        vector<int> next(MAX_VALUE + 1, n);
        int end = n - 1;
        for (int i = n - 1; i >= 0; --i) {
            end = min(end, next[values[i]] - 1);
            limit[i] = end;
            next[values[i]] = i;
        }
    }

    long long solve() { return count(0, static_cast<int>(values.size())); }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> values(n);
    for (int &value : values) {
        cin >> value;
    }
    cout << Solver(move(values)).solve() << '\n';
}
