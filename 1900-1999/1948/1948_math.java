import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long SQUARE_FACTOR = 3, CONSTANT_FACTOR = 12;
    private static final long SEARCH_LIMIT = 2000000000L;
    private static final int DECIMAL_BASE = 10;

    static long nextLong(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        boolean negative = symbol == '-';
        if (negative)
            symbol = in.read();
        long value = 0;
        while (symbol >= '0' && symbol <= '9') {
            value = value * DECIMAL_BASE + symbol - '0';
            symbol = in.read();
        }
        return negative ? -value : value;
    }

    static long solve(long a, long b, long c) {
        long scaled = SQUARE_FACTOR * b * b / a - CONSTANT_FACTOR * c;
        if (scaled < 0)
            return 1;
        long threshold = scaled / a + 1;
        long low = 1, high = SEARCH_LIMIT;
        while (low < high) {
            long middle = low + (high - low) / 2;
            if (middle * middle > threshold)
                high = middle;
            else
                low = middle + 1;
        }
        return low;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        long cases = nextLong(in);
        StringBuilder output = new StringBuilder();
        for (long index = 0; index < cases; ++index) {
            long a = nextLong(in), b = nextLong(in), c = nextLong(in);
            output.append(solve(a, b, c)).append('\n');
        }
        System.out.print(output);
    }
}
