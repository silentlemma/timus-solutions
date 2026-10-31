public class Main {
    static final int DIGITS = 10, WORD_BITS = 64;
    // 2^64 divided by the golden ratio, the usual multiplier of Fibonacci hashing
    static final long HASH_MULTIPLIER = 0x9E3779B97F4A7C15L;
    static long[] number;
    static int[] table, best, before, heap, position;
    static int bits, size;

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int inputAt, inputSize;
    static int read() throws java.io.IOException {
        if (inputAt == inputSize) {
            inputSize = System.in.read(buffer);
            inputAt = 0;
            if (inputSize < 0)
                return -1;
        }
        return buffer[inputAt++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    // high bits of a multiplicative hash select a slot; zero marks an empty index + 1.
    static int slot(long value) {
        int s = (int)((value * HASH_MULTIPLIER) >>> (WORD_BITS - bits));
        while (table[s] != 0 && number[table[s] - 1] != value)
            s = (s + 1) & (table.length - 1);
        return s;
    }
    // each vertex occupies at most one heap slot, avoiding boxed or duplicate queue entries.
    static void rise(int v) {
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
    }
    static void relax(long value, int time, int from) {
        int v = table[slot(value)] - 1;
        if (v >= 0 && (best[v] < 0 || time < best[v])) {
            best[v] = time;
            before[v] = from;
            rise(v);
        }
    }
    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        int[] cost = new int[DIGITS];
        long[] place = new long[DIGITS];
        for (int p = 0; p < DIGITS; p++)
            cost[p] = (int)nextLong();
        place[DIGITS - 1] = 1;
        for (int p = DIGITS - 2; p >= 0; p--)
            place[p] = place[p + 1] * 10;
        int capacity = 1;
        while (capacity < 2 * n) {
            capacity *= 2;
            bits++;
        }
        table = new int[capacity];
        number = new long[n];
        for (int i = 0; i < n; i++) {
            number[i] = nextLong();
            table[slot(number[i])] = i + 1;
        }
        // at most 49999 edges of cost <= 10000 keep shortest distances within int.
        best = new int[n];
        before = new int[n];
        heap = new int[n];
        position = new int[n];
        java.util.Arrays.fill(best, -1);
        java.util.Arrays.fill(before, -1);
        java.util.Arrays.fill(position, -1);
        best[0] = 0;
        rise(0);
        int[] digit = new int[DIGITS];
        while (size > 0) {
            int u = heap[0], last = heap[--size];
            position[u] = -1;
            if (size > 0) {
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
            long value = number[u];
            for (int p = 0; p < DIGITS; p++)
                digit[p] = (int)(value / place[p] % 10);
            // neighbours with the first change at digit p share a prefix of p
            for (int p = 0; p < DIGITS; p++) {
                long low = value - digit[p] * place[p];
                for (int other = 0; other < DIGITS; other++)
                    if (other != digit[p])
                        relax(low + other * place[p], best[u] + cost[p], u);
                for (int q = p + 1; q < DIGITS; q++)
                    if (digit[q] != digit[p])
                        relax(value + (digit[q] - digit[p]) * (place[p] - place[q]),
                              best[u] + cost[p], u);
            }
        }
        if (best[n - 1] < 0) {
            System.out.println(-1);
            return;
        }
        size = 0;
        for (int v = n - 1; v >= 0; v = before[v])
            heap[size++] = v;
        StringBuilder out =
            new StringBuilder().append(best[n - 1]).append('\n').append(size).append('\n');
        while (size > 0) {
            out.append(heap[--size] + 1).append(size > 0 ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
