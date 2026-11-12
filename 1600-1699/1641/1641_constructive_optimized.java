import java.io.IOException;

public class Main {
    static final int OUTPUT_SIZE = 8192;
    static final int NUMBER_RESERVE = 16;
    static final int MAX_DIGITS = 3;

    static int number() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static class Output {
        byte[] bytes = new byte[OUTPUT_SIZE];
        byte[] digits = new byte[MAX_DIGITS];
        int used;
        boolean first = true;

        void flush() throws IOException {
            System.out.write(bytes, 0, used);
            used = 0;
        }

        void number(int value) throws IOException {
            if (used + NUMBER_RESERVE >= bytes.length)
                flush();
            if (!first)
                bytes[used++] = ' ';
            first = false;
            int count = 0;
            do {
                digits[count++] = (byte)('0' + value % 10);
                value /= 10;
            } while (value != 0);
            while (count > 0)
                bytes[used++] = digits[--count];
        }

        void line() {
            bytes[used++] = '\n';
            first = true;
        }
        void pair(int a, int b) throws IOException {
            number(a + 1);
            number(b + 1);
            line();
        }
    }

    public static void main(String[] args) throws IOException {
        int n = number(), k = number(), remaining = number();
        Output output = new Output();
        for (int i = 0; i < n; i++) {
            output.number(i % k + 1);
            output.line();
        }
        for (int i = 0; i + 1 < n; i += 2) {
            output.pair(i, i + 1);
            remaining--;
        }
        int anchor = (n - 1) % k == 0 ? 1 : 0;
        if (n % 2 != 0) {
            output.pair(anchor, n - 1);
            remaining--;
        }
        for (int a = 0; a < n && remaining > 0; a++) {
            for (int b = a + 1; b < n && remaining > 0; b++) {
                if (a % k == b % k)
                    continue;
                // Seed-pair arithmetic replaces the old boolean matrix and retained edge list.
                if ((a % 2 == 0 && b == a + 1) || (n % 2 != 0 && b == n - 1 && a == anchor))
                    continue;
                output.pair(a, b);
                remaining--;
            }
        }
        output.flush();
    }
}
