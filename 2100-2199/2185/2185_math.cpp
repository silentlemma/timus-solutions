#include <cstdio>
#include <string>
#include <vector>

class FastInput {
    static constexpr int BUFFER_SIZE = 65536;
    char buffer[BUFFER_SIZE];
    int position = 0;
    int length = 0;

    char nextChar() {
        if (position == length) {
            length = static_cast<int>(std::fread(buffer, 1, BUFFER_SIZE, stdin));
            position = 0;
        }
        return position < length ? buffer[position++] : '\0';
    }

  public:
    int readInt() {
        char ch = nextChar();
        while (ch <= ' ' && ch != '\0') {
            ch = nextChar();
        }
        bool negative = ch == '-';
        if (negative) {
            ch = nextChar();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = nextChar();
        }
        return negative ? -value : value;
    }
};

struct RemovedRange {
    int left;
    int right;
    int center;
};

int main() {
    constexpr int OUTPUT_RESERVE_PER_QUERY = 16;
    FastInput input;
    int n = input.readInt();
    int q = input.readInt();
    std::vector<int> steps(n);
    for (int &step : steps) {
        step = input.readInt();
    }
    std::vector<int> queries(q);
    int maximum = 0;
    for (int &query : queries) {
        query = input.readInt();
        int index = query < 0 ? -query - 1 : query;
        if (index > maximum) {
            maximum = index;
        }
    }

    int left = 0;
    int right = maximum + 1;
    long long offset = 0;
    std::vector<RemovedRange> removed;
    for (int step : steps) {
        offset += left + offset < 0 ? step : -step;
        long long cut = -offset;
        if (left < cut && cut < right) {
            int middle = static_cast<int>(cut);
            int center = 2 * middle - 1;
            // Opposite values stay related by x -> -x - 1 after every later step.
            if (middle - left <= right - middle) {
                removed.push_back({left, middle, center});
                left = middle;
            } else {
                removed.push_back({middle, right, center});
                right = middle;
            }
        }
    }

    std::vector<long long> answer(maximum + 1);
    for (int index = left; index < right; ++index) {
        answer[index] = index + offset;
    }
    for (auto range = removed.rbegin(); range != removed.rend(); ++range) {
        for (int index = range->left; index < range->right; ++index) {
            answer[index] = -answer[range->center - index] - 1;
        }
    }

    std::string output;
    output.reserve(static_cast<std::size_t>(q) * OUTPUT_RESERVE_PER_QUERY);
    for (int query : queries) {
        long long value = query < 0 ? -answer[-query - 1] - 1 : answer[query];
        output += std::to_string(value);
        output += '\n';
    }
    std::fwrite(output.data(), 1, output.size(), stdout);
}
