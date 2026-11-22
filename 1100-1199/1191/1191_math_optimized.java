public class Main {

    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available <= 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {

        int gap = (int)nextLong();
        int count = (int)nextLong();
        for (int i = 0; i < count; i++) {
            int interval = (int)nextLong();
            // The smallest achievable departure gap is gap-gap%interval.
            gap -= gap % interval;
            if (gap == 0) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}
