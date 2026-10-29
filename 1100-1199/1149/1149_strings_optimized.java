import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 4096;
    private static final byte[] OUTPUT = new byte[BUFFER_SIZE];
    private static int used;

    // the expression goes straight into a 4 KB byte buffer instead of
    // building strings
    private static void write(int ch) {
        OUTPUT[used++] = (byte)ch;
        if (used == OUTPUT.length)
            flush();
    }

    private static void flush() {
        System.out.write(OUTPUT, 0, used);
        used = 0;
    }

    private static void writeNumber(int value) {
        if (value >= 10)
            writeNumber(value / 10);
        write('0' + value % 10);
    }

    // sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
    private static void sine(int n) {
        for (int k = 1; k <= n; k++) {
            write('s');
            write('i');
            write('n');
            write('(');
            writeNumber(k);
            if (k < n)
                write(k % 2 == 1 ? '-' : '+');
        }
        for (int k = 0; k < n; k++)
            write(')');
    }

    public static void main(String[] args) throws IOException {
        // the number is parsed byte by byte from System.in instead of Scanner
        int ch;
        do {
            ch = System.in.read();
        } while (ch <= ' ' && ch != -1);
        int n = 0;
        while (ch >= '0' && ch <= '9') {
            n = n * 10 + ch - '0';
            ch = System.in.read();
        }
        for (int k = 1; k < n; k++)
            write('(');
        for (int i = 1; i <= n; i++) {
            sine(i);
            write('+');
            writeNumber(n - i + 1);
            if (i < n)
                write(')');
        }
        write('\n');
        flush();
        System.out.flush();
    }
}
