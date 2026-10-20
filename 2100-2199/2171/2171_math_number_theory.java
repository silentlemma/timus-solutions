import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SHIFT = 16;

    private final long limit;
    private final long[] starts;
    private final long[] steps;

    private Main(long limit, long[] starts, long[] steps) {
        this.limit = limit;
        this.starts = starts;
        this.steps = steps;
    }

    private long count(int index, long first, long period, long sign) {
        long answer = 0;
        for (int i = index; i < starts.length; ++i) {
            long start = starts[i];
            long step = steps[i];
            long nextFirst = first;
            long nextPeriod = period;
            if (period == 0) {
                // A zero period represents a single remaining number.
                if (first < start || (first - start) % step != 0) {
                    continue;
                }
            } else {
                long gcd = period;
                long remainder = step;
                long coefficient = 1;
                long nextCoefficient = 0;
                while (remainder != 0) {
                    long quotient = gcd / remainder;
                    long oldGcd = gcd;
                    gcd = remainder;
                    remainder = oldGcd - quotient * remainder;
                    long oldCoefficient = coefficient;
                    coefficient = nextCoefficient;
                    nextCoefficient = oldCoefficient - quotient * nextCoefficient;
                }
                long difference = start - first;
                if (difference % gcd != 0) {
                    continue;
                }
                long modulus = step / gcd;
                long offset = (difference / gcd * coefficient) % modulus;
                if (offset < 0) {
                    offset += modulus;
                }
                nextPeriod = period * modulus;
                nextFirst = first + period * offset;
                if (nextFirst < start) {
                    nextFirst += (start - nextFirst + nextPeriod - 1) / nextPeriod
                        * nextPeriod;
                }
                if (nextFirst > limit) {
                    continue;
                }
                if (nextPeriod > limit - nextFirst) {
                    nextPeriod = 0;
                }
            }
            long size = nextPeriod == 0 ? 1 : (limit - nextFirst) / nextPeriod + 1;
            answer += sign * size;
            answer += count(i + 1, nextFirst, nextPeriod, -sign);
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner(System.in);
        long limit = input.nextLong();
        int size = (int) input.nextLong();
        long[] starts = new long[size];
        long[] steps = new long[size];
        for (int i = 0; i < size; ++i) {
            starts[i] = input.nextLong();
            steps[i] = input.nextLong();
        }
        Main solution = new Main(limit, starts, steps);
        System.out.println(solution.count(0, 1, 1, 1));
    }

    private static final class FastScanner {
        private final InputStream input;
        private final byte[] buffer = new byte[1 << BUFFER_SHIFT];
        private int position;
        private int length;

        private FastScanner(InputStream input) {
            this.input = input;
        }

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

        private long nextLong() throws IOException {
            int character;
            do {
                character = read();
            } while (character <= ' ' && character != -1);
            long value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }
}
