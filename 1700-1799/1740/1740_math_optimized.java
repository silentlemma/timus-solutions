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

    public static void main(String[] args) throws java.io.IOException {

        int l = (int)nextLong();
        int k = (int)nextLong();
        int h = (int)nextLong();
        // the time to reach x is x h / k plus a part that repeats every k km
        // and lies between 0 and h, so the last l mod k km take 0 to h hours
        int whole = l / k, slowest = whole + (l % k > 0 ? 1 : 0);
        // both bounds are integers <= 1000000; literal zeroes avoid floating formatting.
        System.out.println(whole * h + ".00000000 " + slowest * h + ".00000000");
    }
}
