import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int OPERAND_CAPACITY = 32;
    private static final int DECIMAL = 10;

    private static class Fraction {
        long numerator;
        long denominator = 1;

        Fraction(InputStream input, byte[] line) throws IOException {
            int length = readLine(input, line);
            int start = 0;
            while (line[start] == ' ' || line[start] == '\t') {
                start++;
            }
            boolean negative = line[start] == '-';
            if (negative) {
                start++;
            }
            while (length > start && (line[length - 1] == ' ' || line[length - 1] == '\t')) {
                length--;
            }
            long value = 0;
            long whole = 0;
            long fraction = 0;
            boolean hasSlash = false;
            for (int i = start; i < length; i++) {
                int ch = line[i];
                if (ch == '/') {
                    fraction = value;
                    value = 0;
                    hasSlash = true;
                } else if (ch == ' ' || ch == '\t') {
                    whole = value;
                    value = 0;
                    while (i + 1 < length && (line[i + 1] == ' ' || line[i + 1] == '\t')) {
                        i++;
                    }
                } else {
                    value = value * DECIMAL + ch - '0';
                }
            }
            if (hasSlash) {
                denominator = value;
                value = whole * denominator + fraction;
            }
            numerator = negative ? -value : value;
        }
    }

    private static int readLine(InputStream input, byte[] line) throws IOException {
        int length = 0;
        int ch;
        while ((ch = input.read()) != -1 && ch != '\n') {
            if (ch != '\r') {
                line[length++] = (byte)ch;
            }
        }
        return length;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        byte[] line = new byte[OPERAND_CAPACITY];
        Fraction left = new Fraction(System.in, line);
        readLine(System.in, line);
        int operatorIndex = 0;
        while (line[operatorIndex] == ' ' || line[operatorIndex] == '\t') {
            operatorIndex++;
        }
        int operation = line[operatorIndex];
        Fraction right = new Fraction(System.in, line);
        long an = left.numerator;
        long ad = left.denominator;
        long bn = right.numerator;
        long bd = right.denominator;
        long numerator;
        long denominator = ad * bd;
        switch (operation) {
        case '+':
            numerator = an * bd + bn * ad;
            break;
        case '-':
            numerator = an * bd - bn * ad;
            break;
        case '*':
            numerator = an * bn;
            break;
        default:
            numerator = an * bd;
            denominator = ad * bn;
        }
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
        StringBuilder answer = new StringBuilder(OPERAND_CAPACITY);
        if (numerator < 0) {
            answer.append('-');
            numerator = -numerator;
        }
        long divisor = gcd(numerator, denominator);
        numerator /= divisor;
        denominator /= divisor;
        long whole = numerator / denominator;
        long remainder = numerator % denominator;
        if (whole != 0 || remainder == 0) {
            answer.append(whole);
        }
        if (remainder != 0) {
            if (whole != 0) {
                answer.append(' ');
            }
            answer.append(remainder).append('/').append(denominator);
        }
        System.out.println(answer);
    }
}
