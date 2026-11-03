import java.util.Arrays;

public class Main {
    static final long[] PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
    static final int MOST = 64, INITIAL_CAPACITY = 32, BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available, size;
    static long limit;
    static long[] values = new long[INITIAL_CAPACITY];
    static int[] counts = new int[INITIAL_CAPACITY];

    static int read() throws Exception {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }
    static long nextLong() throws Exception {
        int c = read();
        while (c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }
    static int lower(long value) {
        int lo = 0, hi = size;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (values[mid] < value)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
    static void grow(int index, int cap, long value, int divisors) {
        int at = lower(value);
        if (at == 0 || counts[at - 1] < divisors) {
            int end = at;
            // Sorted values and strictly increasing counts form the Pareto frontier.
            while (end < size && counts[end] <= divisors)
                end++;
            int newSize = size - (end - at) + 1;
            if (newSize > values.length) {
                values = Arrays.copyOf(values, values.length * 2);
                counts = Arrays.copyOf(counts, counts.length * 2);
            }
            System.arraycopy(values, end, values, at + 1, size - end);
            System.arraycopy(counts, end, counts, at + 1, size - end);
            values[at] = value;
            counts[at] = divisors;
            size = newSize;
        }
        if (index == PRIMES.length)
            return;
        for (int exponent = 1; exponent <= cap; exponent++) {
            if (value > limit / PRIMES[index])
                break;
            value *= PRIMES[index];
            grow(index + 1, exponent, value, divisors * (exponent + 1));
        }
    }
    public static void main(String[] args) throws Exception {
        int tests = (int)nextLong();
        long[] queries = new long[tests];
        for (int i = 0; i < tests; i++) {
            queries[i] = nextLong();
            limit = Math.max(limit, queries[i]);
        }
        grow(0, MOST, 1, 1);
        StringBuilder out = new StringBuilder();
        for (long query : queries) {
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (values[mid] <= query)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            out.append(values[lo - 1]).append(' ').append(counts[lo - 1]).append('\n');
        }
        System.out.print(out);
    }
}
