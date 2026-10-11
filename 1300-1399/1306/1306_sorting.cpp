#include <algorithm>
#include <cstdio>

// stdio only: the memory limit is one megabyte
const int MAXN = 250000;
const int KEEP = MAXN / 2 + 1;

// the KEEP smallest numbers seen so far, as a max-heap: half the input is
// enough, because the median is the largest or second largest of them
unsigned heap[KEEP];

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    int keep = n / 2 + 1, size = 0;
    for (int i = 0; i < n; i++) {
        unsigned x = 0;
        if (scanf("%u", &x) != 1)
            break;
        if (size < keep) {
            heap[size++] = x;
            std::push_heap(heap, heap + size);
        } else if (x < heap[0]) {
            std::pop_heap(heap, heap + size);
            heap[size - 1] = x;
            std::push_heap(heap, heap + size);
        }
    }
    unsigned long long top = heap[0];
    if (n % 2 == 1) {
        printf("%llu.0\n", top);
        return 0;
    }
    std::pop_heap(heap, heap + size);
    unsigned long long sum = top + heap[0];
    printf("%llu.%s\n", sum / 2, sum % 2 ? "5" : "0");
    return 0;
}
