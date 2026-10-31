#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
const int DIGITS = 10, BUFFER_SIZE = 4096, WORD_BITS = 64;
const uint64_t HASH_MULTIPLIER = 11400714819323198485ULL;
// a refillable buffer avoids retaining the input and repeated formatted conversions.
long long readNumber() {
    static char buffer[BUFFER_SIZE];
    static int at = 0, size = 0;
    auto read = []() {
        if (at == size) {
            size = static_cast<int>(fread(buffer, 1, BUFFER_SIZE, stdin));
            at = 0;
        }
        return at < size ? buffer[at++] : '\0';
    };
    char c;
    do {
        c = read();
    } while (c && c <= ' ');
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}
int main() {
    int n = static_cast<int>(readNumber());
    int cost[DIGITS];
    long long place[DIGITS];
    for (int &c : cost)
        c = static_cast<int>(readNumber());
    place[DIGITS - 1] = 1;
    for (int p = DIGITS - 2; p >= 0; p--)
        place[p] = place[p + 1] * 10;
    int capacity = 1, bits = 0;
    while (capacity < 2 * n) {
        capacity *= 2;
        bits++;
    }
    std::vector<long long> number(n);
    std::vector<int> table(capacity);
    // multiplicative hashing uses high bits; slots store index + 1, with zero meaning empty.
    auto slot = [&](long long value) {
        int s = static_cast<int>((static_cast<uint64_t>(value) * HASH_MULTIPLIER) >>
                                 (WORD_BITS - bits));
        while (table[s] && number[table[s] - 1] != value)
            s = (s + 1) & (capacity - 1);
        return s;
    };
    for (int i = 0; i < n; i++) {
        number[i] = readNumber();
        table[slot(number[i])] = i + 1;
    }
    // a shortest simple path has at most 49999 edges of cost <= 10000, within int32.
    std::vector<int> best(n, -1), before(n, -1), heap(n), position(n, -1);
    int size = 0;
    // indexed decrease-key keeps one heap slot per vertex instead of duplicate entries.
    auto rise = [&](int v) {
        int at = position[v];
        if (at < 0)
            at = size++;
        while (at > 0) {
            int parent = (at - 1) / 2;
            if (best[heap[parent]] <= best[v])
                break;
            heap[at] = heap[parent];
            position[heap[at]] = at;
            at = parent;
        }
        heap[at] = v;
        position[v] = at;
    };
    best[0] = 0;
    rise(0);
    auto relax = [&](long long value, int time, int from) {
        int v = table[slot(value)] - 1;
        if (v >= 0 && (best[v] < 0 || time < best[v])) {
            best[v] = time;
            before[v] = from;
            rise(v);
        }
    };
    while (size) {
        int u = heap[0], last = heap[--size];
        position[u] = -1;
        if (size) {
            int at = 0;
            while (at * 2 + 1 < size) {
                int child = at * 2 + 1;
                if (child + 1 < size && best[heap[child + 1]] < best[heap[child]])
                    child++;
                if (best[last] <= best[heap[child]])
                    break;
                heap[at] = heap[child];
                position[heap[at]] = at;
                at = child;
            }
            heap[at] = last;
            position[last] = at;
        }
        if (u == n - 1)
            break;
        long long value = number[u];
        int digit[DIGITS];
        for (int p = 0; p < DIGITS; p++)
            digit[p] = static_cast<int>(value / place[p] % 10);
        // neighbours with the first change at digit p share a prefix of p
        for (int p = 0; p < DIGITS; p++) {
            long long low = value - digit[p] * place[p];
            for (int other = 0; other < DIGITS; other++)
                if (other != digit[p])
                    relax(low + other * place[p], best[u] + cost[p], u);
            for (int q = p + 1; q < DIGITS; q++)
                if (digit[q] != digit[p])
                    relax(value + (digit[q] - digit[p]) * (place[p] - place[q]), best[u] + cost[p],
                          u);
        }
    }
    if (best[n - 1] < 0) {
        puts("-1");
        return 0;
    }
    // the heap is no longer needed; reuse it for the reversed route.
    size = 0;
    for (int v = n - 1; v >= 0; v = before[v])
        heap[size++] = v;
    printf("%d\n%d\n", best[n - 1], size);
    while (size) {
        printf("%d", heap[--size] + 1);
        putchar(size ? ' ' : '\n');
    }
}
