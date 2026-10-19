import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL_PLACES = 12;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long readLong() throws IOException {
        int character = INPUT.read();
        while (character <= ' ' && character != -1) {
            character = INPUT.read();
        }
        long value = 0;
        while (character >= '0' && character <= '9') {
            value = value * 10 + character - '0';
            character = INPUT.read();
        }
        return value;
    }

    private static String probability(long numerator, long denominator) {
        long fraction = 0;
        long remainder = numerator;
        long scale = 1;
        for (int digit = 0; digit < DECIMAL_PLACES; digit++) {
            remainder *= 10;
            fraction = fraction * 10 + remainder / denominator;
            remainder %= denominator;
            scale *= 10;
        }
        if (2 * remainder >= denominator) {
            fraction++;
        }
        String integer = Long.toString(fraction / scale);
        fraction %= scale;
        if (fraction == 0) {
            return integer;
        }
        String digits = Long.toString(fraction);
        StringBuilder result = new StringBuilder(integer).append('.');
        for (int digit = digits.length(); digit < DECIMAL_PLACES; digit++) {
            result.append('0');
        }
        result.append(digits);
        while (result.charAt(result.length() - 1) == '0') {
            result.setLength(result.length() - 1);
        }
        return result.toString();
    }

    public static void main(String[] args) throws IOException {
        long speed = readLong();
        readLong();
        readLong();
        long widthMarx = readLong();
        long greenEngels = readLong();
        long yellowEngels = readLong();
        long greenMarx = readLong();
        long yellowMarx = readLong();
        long period = greenEngels + yellowEngels + greenMarx + yellowMarx;
        long denominator = speed * period;
        // Only the phase lengths and the time to cross Marx affect the comparison.
        long crosswalk = speed * (greenEngels + yellowMarx) - widthMarx;
        System.out.println(probability(crosswalk, denominator) + " "
                + probability(widthMarx, denominator));
    }
}
