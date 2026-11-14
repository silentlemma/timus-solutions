import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    private static final int MODULUS = 2007;
    private static final int RESIDUE_DIGITS = 4;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        boolean negative = c == '-';
        if (negative || c == '+') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = input.read();
        }
        return negative ? -value : value;
    }

    private static int inverse(int a) {
        int b = MODULUS;
        int u = 1;
        int v = 0;
        while (b != 0) {
            int quotient = a / b;
            int remainder = a - quotient * b;
            int coefficient = u - quotient * v;
            a = b;
            b = remainder;
            u = v;
            v = coefficient;
        }
        return Math.floorMod(u, MODULUS);
    }

    private static void writeNumber(BufferedOutputStream output, byte[] digits, int value)
        throws IOException {
        int start = digits.length;
        do {
            digits[--start] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        output.write(digits, start, digits.length - start);
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = number(input);
        short[] f = new short[n + 1];
        for (int i = 1; i <= n; i++) {
            f[i] = (short)Math.floorMod(number(input), MODULUS);
        }
        int first = inverse(f[1]);
        short[] sums = new short[n + 1];
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        byte[] digits = new byte[RESIDUE_DIGITS];
        for (int d = 1; d <= n; d++) {
            int coefficient = first;
            if (d > 1) {
                coefficient = Math.floorMod(-first * sums[d], MODULUS);
                output.write(' ');
            }
            writeNumber(output, digits, coefficient);
            // Zero coefficients never affect any multiple of d.
            if (coefficient != 0) {
                for (int k = 2, multiple = d + d; multiple <= n; k++, multiple += d) {
                    sums[multiple] = (short)((sums[multiple] + f[k] * coefficient) % MODULUS);
                }
            }
        }
        output.write('\n');
        output.flush();
    }
}
