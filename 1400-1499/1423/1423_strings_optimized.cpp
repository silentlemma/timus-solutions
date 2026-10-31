#include <cstdint>
#include <cstdio>

const int MAX_LENGTH = 250000;
const int PREFIX_BITS = 18;
const int WORD_BITS = 32;
const int PREFIX_WORDS = (MAX_LENGTH * PREFIX_BITS + WORD_BITS - 1) / WORD_BITS + 1;
const std::uint64_t PREFIX_MASK = (std::uint64_t{1} << PREFIX_BITS) - 1;
// each string has at most 250000 bytes, plus its terminating zero.
char source[MAX_LENGTH + 1], target[MAX_LENGTH + 1];
// prefix lengths are below 250000 and fit in eighteen bits.
// one extra word makes a two-word read safe even at the end of the array.
std::uint32_t prefix[PREFIX_WORDS];

int getPrefix(int index) {
    int bit = index * PREFIX_BITS, word = bit / WORD_BITS, shift = bit % WORD_BITS;
    std::uint64_t pair = prefix[word] | (std::uint64_t{prefix[word + 1]} << WORD_BITS);
    return static_cast<int>((pair >> shift) & PREFIX_MASK);
}

void setPrefix(int index, int value) {
    int bit = index * PREFIX_BITS, word = bit / WORD_BITS, shift = bit % WORD_BITS;
    std::uint64_t pair = std::uint64_t(value) << shift;
    // each disjoint field is written once into the initially zero array.
    prefix[word] |= static_cast<std::uint32_t>(pair);
    prefix[word + 1] |= static_cast<std::uint32_t>(pair >> WORD_BITS);
}

int main() {
    int n;
    std::scanf("%d%250000s%250000s", &n, source, target);
    // t is s turned left by k, that is right by n - k: find it in s + s with KMP
    for (int i = 1, k = 0; i < n; ++i) {
        while (k > 0 && target[i] != target[k])
            k = getPrefix(k - 1);
        if (target[i] == target[k])
            ++k;
        setPrefix(i, k);
    }
    // two passes over the source avoid allocating its doubled copy.
    for (int i = 0, k = 0; i < 2 * n - 1; ++i) {
        char c = source[i < n ? i : i - n];
        while (k > 0 && c != target[k])
            k = getPrefix(k - 1);
        if (c == target[k])
            ++k;
        if (k == n) {
            int start = i - n + 1;
            std::printf("%d\n", (n - start) % n);
            return 0;
        }
    }
    std::puts("-1");
}
