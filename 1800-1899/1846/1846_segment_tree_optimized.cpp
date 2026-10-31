#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const int BUFFER_SIZE = 4096;
// refillable storage bounds memory, not input length.
unsigned char buffer[BUFFER_SIZE];
int position = 0, length = 0;
int read() {
    if (position == length) {
        length = static_cast<int>(fread(buffer, 1, BUFFER_SIZE, stdin));
        position = 0;
        if (length == 0)
            return EOF;
    }
    return buffer[position++];
}
int number() {
    int c = read();
    while (c < '0' || c > '9')
        c = read();
    int value = 0;
    do {
        value = value * 10 + c - '0';
        c = read();
    } while (c >= '0' && c <= '9');
    return value;
}

int main() {
    int q = number();
    std::vector<int> operations(q), values(q);
    // x <= 10^9: signed ints encode both the operation and its value.
    for (int i = 0; i < q; ++i) {
        int sign = read();
        while (sign != '+' && sign != '-')
            sign = read();
        int x = number();
        values[i] = x;
        operations[i] = sign == '+' ? x : -x;
    }
    std::sort(values.begin(), values.end());
    values.erase(std::unique(values.begin(), values.end()), values.end());
    int size = static_cast<int>(values.size());
    // one leaf per distinct value; duplicate copies only change a counter.
    std::vector<int> counts(size), tree(2 * size);
    for (int operation : operations) {
        int x = operation > 0 ? operation : -operation;
        int id =
            static_cast<int>(std::lower_bound(values.begin(), values.end(), x) - values.begin());
        counts[id] += operation > 0 ? 1 : -1;
        int v = size + id, value = counts[id] ? x : 0;
        if (tree[v] != value) {
            tree[v] = value;
            for (v /= 2; v; v /= 2) {
                int g = std::gcd(tree[2 * v], tree[2 * v + 1]);
                if (g == tree[v])
                    break;
                tree[v] = g;
            }
        }
        printf("%d\n", tree[1] ? tree[1] : 1);
    }
}
