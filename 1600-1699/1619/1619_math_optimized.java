import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static final int DECIMAL = 10;
    static final int PLACES = 8;
    static final long SCALE = 100000000L;

    static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int cases = number(input);
        StringBuilder output = new StringBuilder(cases * (PLACES + "0.\n".length()));
        char[] digits = new char[PLACES];
        for (int i = 0; i < cases; i++) {
            int k = number(input);
            int m = number(input);
            if (m > k) {
                output.append("0\n");
            } else if (m == 0) {
                output.append("1\n");
            } else {
                // Eight decimal places give error below 10^-8, even when truncated.
                long fraction = (k - m + 1) * SCALE / (k + 1);
                for (int pos = PLACES - 1; pos >= 0; pos--) {
                    digits[pos] = (char)('0' + fraction % DECIMAL);
                    fraction /= DECIMAL;
                }
                output.append("0.").append(digits).append('\n');
            }
        }
        System.out.print(output);
    }
}
