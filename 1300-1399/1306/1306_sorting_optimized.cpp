#include <algorithm>
#include <cstdio>

// refills allow arbitrarily long input with only four kibibytes of storage.
const int INPUT_BUFFER = 4096;
char input_buffer[INPUT_BUFFER];
int input_pos = 0, input_len = 0;

int read_byte() {
    if (input_pos == input_len) {
        input_len = static_cast<int>(fread(input_buffer, 1, INPUT_BUFFER, stdin));
        input_pos = 0;
        if (input_len == 0)
            return EOF;
    }
    return input_buffer[input_pos++];
}

int next_int() {
    int c = read_byte();
    while (c != EOF && c <= ' ')
        c = read_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + (c - '0');
        c = read_byte();
    }
    return value;
}

const int MAX_COUNT = 250000, MAX_KEEP = MAX_COUNT / 2 + 1;
int heap[MAX_KEEP];

void replace_top(int value, int size) {
    // one downward sift replaces pop_heap followed by push_heap.
    int at = 0;
    while (at * 2 + 1 < size) {
        int child = at * 2 + 1;
        if (child + 1 < size && heap[child + 1] > heap[child])
            child++;
        if (heap[child] <= value)
            break;
        heap[at] = heap[child];
        at = child;
    }
    heap[at] = value;
}
int main() {
    int n = next_int(), keep = n / 2 + 1;
    // n <= 250000 needs at most 125001 ordinary 32-bit elements, within one mib.
    for (int i = 0; i < keep; i++)
        heap[i] = next_int();
    std::make_heap(heap, heap + keep);
    for (int i = keep; i < n; i++) {
        int value = next_int();
        if (value < heap[0])
            replace_top(value, keep);
    }
    long long total = heap[0];
    if (n % 2)
        printf("%lld.0\n", total);
    else {
        // each value <= 2^31 - 1; widening before addition preserves the mean.
        replace_top(heap[keep - 1], keep - 1);
        total += heap[0];
        printf("%lld.%c\n", total / 2, total % 2 ? '5' : '0');
    }
}
