import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int MODULUS = 40961;

    private static long power(long base, int exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * base % MODULUS;
            }
            base = base * base % MODULUS;
            exponent /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        StringBuilder text = new StringBuilder();
        int next = input.read();
        while (next >= 0 && next <= ' ') {
            next = input.read();
        }
        while (next > ' ') {
            text.append((char) next);
            next = input.read();
        }
        int n = text.length();
        int[] row = new int[n];
        long ones = 0;
        for (int i = 0; i < n; i++) {
            row[i] = text.charAt(i) - '0';
            ones += row[i];
        }

        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial = factorial * i % MODULUS;
        }
        long[] inverseFactorial = new long[n + 1];
        inverseFactorial[n] = power(factorial, MODULUS - 2);
        for (int i = n; i > 0; i--) {
            inverseFactorial[i - 1] = inverseFactorial[i] * i % MODULUS;
        }

        long[] answer = new long[n + 1];
        long total = 1;
        long onesTotal = ones;
        for (int k = n - 1; k > 0; k--) {
            long squares = 0;
            // Scaling each row by (n-k)! removes division from the recurrence.
            for (int i = 0; i < k; i++) {
                int value = ((k - i) * row[i] + (i + 1) * row[i + 1]) % MODULUS;
                row[i] = value;
                squares += (long) value * value;
            }
            total = total * (k + 1) % MODULUS;
            onesTotal = onesTotal * k % MODULUS;
            long difference = (total * onesTotal - squares % MODULUS + MODULUS) % MODULUS;
            long inverse = inverseFactorial[n - k];
            answer[k] = difference * inverse % MODULUS * inverse % MODULUS;
        }

        StringBuilder output = new StringBuilder();
        for (int k = 1; k <= n; k++) {
            if (k > 1) {
                output.append(' ');
            }
            output.append(answer[k]);
        }
        System.out.println(output);
    }
}
