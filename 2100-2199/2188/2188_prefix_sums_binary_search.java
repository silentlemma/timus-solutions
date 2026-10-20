import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;

    private static class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int digit;
            do {
                digit = read();
            } while (digit <= ' ');
            int value = 0;
            while (digit > ' ') {
                value = value * 10 + digit - '0';
                digit = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int q = input.nextInt();
        long[] prefix = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = input.nextInt();
        }
        for (int i = 1; i <= n; i++) {
            prefix[i] += prefix[i - 1] - input.nextInt();
        }

        long[] suffixMinimum = new long[n + 1];
        suffixMinimum[n] = prefix[n];
        for (int i = n - 1; i >= 1; i--) {
            suffixMinimum[i] = Math.min(prefix[i], suffixMinimum[i + 1]);
        }

        long[] thresholds = new long[n];
        int[] times = new int[n];
        int count = 0;
        long prefixMaximum = 0;
        for (int i = 1; i <= n; i++) {
            // Waiting before this second costs at most the earlier prefix maximum.
            if (suffixMinimum[i] > prefixMaximum) {
                thresholds[count] = suffixMinimum[i];
                times[count++] = i;
            }
            prefixMaximum = Math.max(prefixMaximum, prefix[i]);
        }

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int distance = input.nextInt();
            int left = 0;
            int right = count;
            while (left < right) {
                int middle = left + (right - left) / 2;
                if (thresholds[middle] <= distance) {
                    left = middle + 1;
                } else {
                    right = middle;
                }
            }
            output.append(left < count ? times[left] : -1).append('\n');
        }
        System.out.print(output);
    }
}
