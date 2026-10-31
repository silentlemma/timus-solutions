#include <algorithm>
#include <cstdio>

constexpr int MAX_SIGNS = 10000;
constexpr int KIND_BITS = 14;
constexpr int COUNT_UNIT = 1 << KIND_BITS;
constexpr int KIND_MASK = COUNT_UNIT - 1;
// count and kind are <= 10000: two 14-bit fields fit in a signed int.
// integer order equals the simple heap's (count, kind) lexicographic order.
int heap[MAX_SIGNS];

int main() {
    int k, size = 0;
    scanf("%d", &k);
    for (int kind = 1; kind <= k; kind++) {
        int count;
        scanf("%d", &count);
        heap[size++] = count * COUNT_UNIT + kind;
        std::push_heap(heap, heap + size);
    }
    int previous = 0;
    bool first = true;
    while (size > 0) {
        std::pop_heap(heap, heap + size);
        int value = heap[--size];
        if ((value & KIND_MASK) == previous && size > 0) {
            std::pop_heap(heap, heap + size);
            int other = heap[--size];
            heap[size++] = value;
            std::push_heap(heap, heap + size);
            value = other;
        }
        int kind = value & KIND_MASK;
        // stream the answer instead of retaining up to 10000 decimal strings.
        printf(first ? "%d" : " %d", kind);
        first = false;
        previous = kind;
        if (value / COUNT_UNIT > 1) {
            heap[size++] = value - COUNT_UNIT;
            std::push_heap(heap, heap + size);
        }
    }
    putchar('\n');
}
