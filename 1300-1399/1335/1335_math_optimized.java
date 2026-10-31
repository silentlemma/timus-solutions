public class Main {

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int at, size;
    static int read() throws java.io.IOException {
        if (at == size) {
            size = System.in.read(buffer);
            at = 0;
            if (size < 0)
                return -1;
        }
        return buffer[at++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws java.io.IOException {
        long n = nextLong();
        // modulo n^2 + 1 the first number is -1 and the second is n, so the sum
        // of their squares is 1 + n^2, a multiple of n^2 + 1
        System.out.println(n * n + " " + (n * n + n + 1) + " " + (n * n + 1));
    }
}
