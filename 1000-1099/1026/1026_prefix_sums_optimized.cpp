#include <cstdio>

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

const int MAX_VALUE = 5000;
int counts[MAX_VALUE + 1];
int main() {
    int n = number();
    for (int i = 0; i < n; ++i)
        ++counts[number()];
    // values are in [1,5000]; counts can reach 100000 and need ordinary ints.
    for (int i = 1; i <= MAX_VALUE; ++i)
        counts[i] += counts[i - 1];
    int k = number();
    for (int i = 0; i < k; ++i) {
        int rank = number(), low = 1, high = MAX_VALUE;
        while (low < high) {
            int mid = (low + high) / 2;
            if (counts[mid] < rank)
                low = mid + 1;
            else
                high = mid;
        }
        printf("%d\n", low);
    }
}
