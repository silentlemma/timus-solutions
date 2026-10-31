#include <algorithm>
#include <cstdio>
#include <vector>

const int INPUT_BUFFER = 4096;
// refilling this small buffer keeps memory independent of the input size.
int nextInt() {
    static char buffer[INPUT_BUFFER];
    static int position = 0, size = 0;
    auto read = [&]() -> int {
        if (position == size) {
            size = static_cast<int>(std::fread(buffer, 1, INPUT_BUFFER, stdin));
            position = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[position++];
    };
    int c = read();
    while (c != EOF && c != '-' && (c < '0' || c > '9'))
        c = read();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value * sign;
}

int main() {
    int m = nextInt(), n = nextInt(), k = nextInt();
    int stride = n + 2, columnStride = m + 2;
    // coordinates <= 30000 make both row-major and column-major keys fit int.
    std::vector<int> rows(k), columns(k);
    for (int i = 0; i < k; ++i) {
        int x = nextInt(), y = nextInt();
        rows[i] = x * stride + y;
        columns[i] = y * columnStride + x;
    }
    std::sort(rows.begin(), rows.end());
    std::sort(columns.begin(), columns.end());
    int answer = 0, at = 0;
    for (int x = 1; x <= m; ++x) {
        int previous = 0;
        while (true) {
            int next = at < k && rows[at] / stride == x ? rows[at++] % stride : n + 1;
            int length = next - previous - 1, cell = x * stride + previous + 1;
            if (length >= 2 ||
                (length == 1 &&
                 (x == 1 || std::binary_search(rows.begin(), rows.end(), cell - stride)) &&
                 (x == m || std::binary_search(rows.begin(), rows.end(), cell + stride))))
                ++answer;
            if (next == n + 1)
                break;
            previous = next;
        }
    }
    at = 0;
    for (int y = 1; y <= n; ++y) {
        int previous = 0;
        while (true) {
            int next =
                at < k && columns[at] / columnStride == y ? columns[at++] % columnStride : m + 1;
            if (next - previous - 1 >= 2)
                ++answer;
            if (next == m + 1)
                break;
            previous = next;
        }
    }
    std::printf("%d\n", answer);
}
