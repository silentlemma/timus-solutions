public class Main {

    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
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
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = (int)nextLong(), events = (int)nextLong();
        long limit = nextLong();
        // At most 100000 weights of at most 10000: every prefix is at most 10^9.
        int[] prefix = new int[count + 1];
        for (int i = 1; i <= count; i++)
            prefix[i] = prefix[i - 1] + (int)nextLong();
        int[] retreat = new int[count + 1];
        int left = 0;
        for (int height = 1; height <= count; height++) {
            while (left + 1 < height && prefix[height] - prefix[left + 1] > limit)
                left++;
            retreat[height] = left;
        }
        long time = 0;
        int height = 0;
        for (int i = 0; i < events; i++) {
            long event = nextLong(), ordinary = event - time - 1;
            if (ordinary >= count - height) {
                System.out.println(time + count - height);
                return;
            }
            height += (int)ordinary;
            height = retreat[height];
            time = event;
        }
        System.out.println(time + count - height);
    }
}
