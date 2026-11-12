#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 8192;
const int NUMBER_RESERVE = 24;
const int AMOUNT_LIMIT = 50000;
const int FIELD_BITS = 17;
const uint64_t FIELD_MASK = (uint64_t(1) << FIELD_BITS) - 1;
const int DAY_SLOTS = 32;
const int HOURS = 24;
const int MINUTES = 60;

struct Reader {
    unsigned char data[BUFFER_SIZE];
    int position = 0, length = 0;
    int byte() {
        if (position == length) {
            length = int(fread(data, 1, sizeof(data), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return data[position++];
    }
    int number() {
        int c = byte();
        while (c && (c < '0' || c > '9') && c != '-' && c != '+')
            c = byte();
        bool negative = c == '-';
        if (c == '-' || c == '+')
            c = byte();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return negative ? -value : value;
    }
};

struct Writer {
    char data[BUFFER_SIZE];
    int used = 0;
    void flush() {
        fwrite(data, 1, used, stdout);
        used = 0;
    }
    void number(int64_t value) {
        if (used + NUMBER_RESERVE > BUFFER_SIZE)
            flush();
        if (value < 0) {
            data[used++] = '-';
            value = -value;
        }
        char digits[NUMBER_RESERVE];
        int length = 0;
        do {
            digits[length++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (length)
            data[used++] = digits[--length];
        data[used++] = '\n';
    }
};

int main() {
    Reader in;
    Writer out;
    int n = in.number(), size = 1;
    std::vector<uint64_t> events(n);
    for (int i = 0; i < n; ++i) {
        int amount = in.number(), day = in.number(), month = in.number();
        int hour = in.number(), minute = in.number();
        uint64_t key = ((month * DAY_SLOTS + day) * HOURS + hour) * MINUTES + minute;
        events[i] = (key << (2 * FIELD_BITS)) | (uint64_t(i) << FIELD_BITS) |
                    uint64_t(amount + AMOUNT_LIMIT);
    }
    std::sort(events.begin(), events.end());
    std::vector<uint32_t> ranks(n);
    for (int rank = 0; rank < n; ++rank)
        ranks[(events[rank] >> FIELD_BITS) & FIELD_MASK] = rank;
    while (size < n)
        size *= 2;
    std::vector<int32_t> leaves(size);
    // Only internal nodes need 64-bit sum/prefix pairs; leaves fit signed32.
    std::vector<int64_t> sums(size), prefixes(size);
    for (int i = 0; i < n; ++i) {
        int rank = int(ranks[i]);
        leaves[rank] = int32_t(events[rank] & FIELD_MASK) - AMOUNT_LIMIT;
        if (size == 1) {
            out.number(std::min(0, leaves[0]));
            continue;
        }
        int parent = (size + rank) / 2;
        int64_t left = leaves[rank & ~1], right = leaves[rank | 1];
        sums[parent] = left + right;
        prefixes[parent] = std::min({int64_t(0), left, left + right});
        for (parent /= 2; parent; parent /= 2) {
            sums[parent] = sums[2 * parent] + sums[2 * parent + 1];
            prefixes[parent] =
                std::min(prefixes[2 * parent], sums[2 * parent] + prefixes[2 * parent + 1]);
        }
        out.number(prefixes[1]);
    }
    out.flush();
}
