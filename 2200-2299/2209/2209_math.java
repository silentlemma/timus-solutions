import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long nextLong() throws IOException {
        int symbol = INPUT.read();
        while (symbol != -1 && symbol <= ' ') {
            symbol = INPUT.read();
        }
        long value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = INPUT.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        long depth = nextLong();
        long index = nextLong() - 1;
        int pathBits = 0;
        for (long remaining = index; remaining > 0; remaining >>= 1) {
            pathBits++;
        }

        long leftNumerator = 0;
        long leftDenominator = 1;
        long rightNumerator = 1;
        // Leading left moves only increase the right denominator.
        long rightDenominator = depth - 1 - pathBits;
        for (int bit = pathBits - 1; bit >= 0; bit--) {
            if (((index >> bit) & 1) == 0) {
                rightNumerator += leftNumerator;
                rightDenominator += leftDenominator;
            } else {
                leftNumerator += rightNumerator;
                leftDenominator += rightDenominator;
            }
        }

        System.out.println((leftNumerator + rightNumerator) + " "
                + (leftDenominator + rightDenominator));
    }
}
