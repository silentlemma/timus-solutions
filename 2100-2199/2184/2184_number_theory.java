import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput(System.in);
        int n = (int) input.nextLong();
        long[] values = new long[n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            values[i] = input.nextLong();
            total += values[i];
        }

        // Only strict changes of a prefix or suffix gcd can be exceptions.
        boolean[] marked = new boolean[n];
        long current = total;
        for (int i = 0; i < n; i++) {
            long next = gcd(current, values[i]);
            if (next != current) {
                marked[i] = true;
                current = next;
            }
        }
        current = total;
        for (int i = n - 1; i >= 0; i--) {
            long next = gcd(current, values[i]);
            if (next != current) {
                marked[i] = true;
                current = next;
            }
        }

        int count = 0;
        long fixed = total;
        for (int i = 0; i < n; i++) {
            if (marked[i]) {
                count++;
            } else {
                fixed = gcd(fixed, values[i]);
            }
        }
        long[] critical = new long[count];
        int at = 0;
        for (int i = 0; i < n; i++) {
            if (marked[i]) {
                critical[at++] = values[i];
            }
        }

        long[] suffix = new long[count + 1];
        suffix[count] = fixed;
        for (int i = count - 1; i >= 0; i--) {
            suffix[i] = gcd(critical[i], suffix[i + 1]);
        }
        long answer = suffix[0];
        long before = fixed;
        for (int i = 0; i < count; i++) {
            long middle = before;
            for (int j = i + 1; j < count; j++) {
                answer = Math.max(answer, gcd(middle, suffix[j + 1]));
                middle = gcd(middle, critical[j]);
            }
            before = gcd(before, critical[i]);
        }
        System.out.println(answer);
    }

    private static class FastInput {
        private final InputStream stream;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        FastInput(InputStream stream) {
            this.stream = stream;
        }

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

        long nextLong() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return value;
        }
    }
}
