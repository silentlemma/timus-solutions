import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int GOALS = 3;
    private static final long MODULUS = 1000000007L;

    static int countForecasts(int size) {
        int total = GOALS * size * (size - 1) / 2;
        int maximum = GOALS * (size - 1), stride = maximum + 1;
        int maxRows = 1;
        for (int used = 0; used <= size; ++used) {
            maxRows = Math.max(maxRows, total * used / size - GOALS * used * (used - 1) / 2 + 1);
        }
        int[] current = new int[maxRows * stride], following = new int[maxRows * stride];
        current[0] = 1;
        int lower = 0, upper = 0;
        for (int used = 0; used < size; ++used) {
            int nextUsed = used + 1;
            int nextLower = GOALS * nextUsed * used / 2, nextUpper = total * nextUsed / size;
            Arrays.fill(following, 0);
            for (int partial = lower; partial <= upper; ++partial) {
                int minimumLast = used > 0 ? (partial + used - 1) / used : 0;
                int first = Math.max(0, Math.max(nextLower - partial, minimumLast));
                int last = Math.min(
                    maximum, Math.min(nextUpper - partial, (total - partial) / (size - used)));
                if (first > last)
                    continue;
                int row = (partial - lower) * stride;
                long prefix = 0;
                for (int value = 0; value < first; ++value)
                    prefix += current[row + value];
                for (int value = first; value <= last; ++value) {
                    prefix += current[row + value];
                    if (prefix != 0) {
                        following[(partial + value - nextLower) * stride + value] =
                            (int)(prefix % MODULUS);
                    }
                }
            }
            int[] swap = current;
            current = following;
            following = swap;
            lower = nextLower;
            upper = nextUpper;
        }
        long answer = 0;
        for (int value = 0; value < stride; ++value)
            answer += current[value];
        return (int)(answer % MODULUS);
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        if (symbol == '+')
            symbol = in.read();
        int size = 0;
        while (symbol > ' ') {
            size = size * 10 + symbol - '0';
            symbol = in.read();
        }
        System.out.println(countForecasts(size));
    }
}
