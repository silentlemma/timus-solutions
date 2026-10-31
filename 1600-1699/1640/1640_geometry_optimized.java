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
        int n = (int)nextLong();
        // Sandro's own spot holds no demon: stay there and reach the farthest one
        double farthest = 0;
        for (int i = 0; i < n; i++) {
            farthest = Math.max(farthest, Math.hypot(nextLong(), nextLong()));
        }
        System.out.println(String.format(java.util.Locale.US, "0 0 %.10f", farthest));
    }
}
