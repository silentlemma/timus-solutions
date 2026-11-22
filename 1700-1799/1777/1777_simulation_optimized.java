public class Main {
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
    static final byte[] output = new byte[OUTPUT_SIZE], digits = new byte[DIGITS];
    static int used;

    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void number(int value) {
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }

    static void finish() { System.out.write(output, 0, used); }

    static int asked(long a, long b, long c) {
        if (a > b) {
            long t = a;
            a = b;
            b = t;
        }
        if (b > c) {
            long t = b;
            b = c;
            c = t;
        }
        if (a > b) {
            long t = a;
            a = b;
            b = t;
        }
        long gap = Math.min(b - a, c - b);
        int people = 1;
        while (gap > 0) {
            people++;
            // gap <= b-a < b: the new pile can be adjacent only to a and b.
            long next;
            if (gap < a) {
                // b-gap is no smaller than a-gap in this branch.
                next = Math.min(gap, a - gap);
                b = a;
                a = gap;
            } else {
                // gap-a is no larger than gap in this branch.
                next = Math.min(gap - a, b - gap);
                b = gap;
            }
            gap = next;
        }
        return people;
    }

    public static void main(String[] args) throws java.io.IOException {
        number(asked(nextLong(), nextLong(), nextLong()));
        write('\n');
        finish();
    }
}
