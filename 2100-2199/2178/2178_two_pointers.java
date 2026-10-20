import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int MAX_VALUE = 100000;
    private static final int BASE_SIZE = 16;
    private static final int BUFFER_SIZE = 65536;
    private static int[] values;
    private static int[] limit;
    private static int[] minimum;
    private static int[] maximum;
    private static int[] frequency;

    private static long mixed(int left, int middle, int right, int sign) {
        int[] low = sign == 1 ? minimum : maximum;
        int[] high = sign == 1 ? maximum : minimum;
        int offset = sign == 1 ? 0 : MAX_VALUE;
        int lower = middle;
        int upper = middle - 1;
        int threshold = upper;
        int current = lower;
        long answer = 0;
        for (int i = middle - 1; i >= left; --i) {
            while (lower < right && sign * low[lower] >= sign * low[i]) {
                ++lower;
            }
            while (threshold + 1 < right && sign * high[threshold + 1] < sign * high[i]) {
                ++threshold;
            }
            int target = Math.min(threshold, limit[i]);
            while (upper < target) {
                ++upper;
                if (upper >= current) {
                    ++frequency[sign * low[upper] + upper + offset];
                }
            }
            while (upper > target) {
                if (upper >= current) {
                    --frequency[sign * low[upper] + upper + offset];
                }
                --upper;
            }
            while (current < lower) {
                if (current <= upper) {
                    --frequency[sign * low[current] + current + offset];
                }
                ++current;
            }
            answer += frequency[sign * high[i] + i + offset];
        }
        for (int j = middle; j < right; ++j) {
            frequency[sign * low[j] + j + offset] = 0;
        }
        return answer;
    }

    private static long count(int left, int right) {
        long answer = 0;
        if (right - left <= BASE_SIZE) {
            for (int i = left; i < right; ++i) {
                int low = values[i];
                int high = low;
                for (int j = i; j < right && j <= limit[i]; ++j) {
                    low = Math.min(low, values[j]);
                    high = Math.max(high, values[j]);
                    if (high - low == j - i) {
                        ++answer;
                    }
                }
            }
            return answer;
        }
        int middle = left + (right - left) / 2;
        answer = count(left, middle) + count(middle, right);
        while (left < middle && limit[left] < middle) {
            ++left;
        }
        right = Math.min(right, limit[middle - 1] + 1);
        if (left == middle || right == middle) {
            return answer;
        }
        minimum[middle - 1] = maximum[middle - 1] = values[middle - 1];
        for (int i = middle - 2; i >= left; --i) {
            minimum[i] = Math.min(minimum[i + 1], values[i]);
            maximum[i] = Math.max(maximum[i + 1], values[i]);
        }
        minimum[middle] = maximum[middle] = values[middle];
        for (int j = middle + 1; j < right; ++j) {
            minimum[j] = Math.min(minimum[j - 1], values[j]);
            maximum[j] = Math.max(maximum[j - 1], values[j]);
        }
        // Extrema in one half determine the opposite endpoint.
        for (int i = left; i < middle; ++i) {
            int j = i + maximum[i] - minimum[i];
            if (j >= middle && j < right && j <= limit[i] && maximum[j] < maximum[i] &&
                minimum[j] > minimum[i]) {
                ++answer;
            }
        }
        for (int j = middle; j < right; ++j) {
            int i = j - maximum[j] + minimum[j];
            if (i >= left && i < middle && j <= limit[i] && maximum[i] < maximum[j] &&
                minimum[i] > minimum[j]) {
                ++answer;
            }
        }
        return answer + mixed(left, middle, right, 1) + mixed(left, middle, right, -1);
    }

    private static class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int symbol = read();
            while (symbol < '0' || symbol > '9') {
                symbol = read();
            }
            int value = 0;
            while (symbol >= '0' && symbol <= '9') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        values = new int[n];
        limit = new int[n];
        minimum = new int[n];
        maximum = new int[n];
        frequency = new int[MAX_VALUE + n + 1];
        for (int i = 0; i < n; ++i) {
            values[i] = input.nextInt();
        }
        int[] next = new int[MAX_VALUE + 1];
        java.util.Arrays.fill(next, n);
        int end = n - 1;
        for (int i = n - 1; i >= 0; --i) {
            end = Math.min(end, next[values[i]] - 1);
            limit[i] = end;
            next[values[i]] = i;
        }
        System.out.println(count(0, n));
    }
}
