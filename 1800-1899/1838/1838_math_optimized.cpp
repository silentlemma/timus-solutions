#include <algorithm>
#include <array>
#include <cstdio>
#include <vector>

namespace {
constexpr int BUFFER_SIZE = 8192;
constexpr int DECIMAL = 10;

class Input {
    std::array<unsigned char, BUFFER_SIZE> buffer{};
    std::size_t offset = 0, length = 0;

    int next_byte() {
        if (offset == length) {
            length = std::fread(buffer.data(), 1, buffer.size(), stdin);
            offset = 0;
            if (length == 0) {
                return EOF;
            }
        }
        return buffer[offset++];
    }

  public:
    int number() {
        int ch = next_byte();
        while (ch != EOF && ch <= ' ') {
            ch = next_byte();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = next_byte();
        }
        return value;
    }
};
} // namespace

int main() {
    Input input;
    const int length = input.number();
    const int count = input.number();
    std::vector<int> supports(count);
    for (int &point : supports) {
        point = input.number();
    }
    const int min_cut = 2 * supports.front();
    const int max_cut = 2 * supports.back() - length;
    int safe = 0;
    if (min_cut < max_cut) {
        // Gaps entirely outside this range contribute nothing.
        for (auto right = std::upper_bound(supports.begin(), supports.end(), min_cut);
             right != supports.end() && *(right - 1) < max_cut; ++right) {
            const int left = *(right - 1);
            const int lo = std::max({left, min_cut, 2 * *right - length});
            const int hi = std::min({*right, max_cut, 2 * left});
            safe += std::max(0, hi - lo);
        }
    }
    std::printf("%d\n", length - safe);
}
