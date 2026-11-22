import java.util.Arrays;

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

    public static void main(String[] args) throws Exception {
        int stones = (int)nextLong(), count = (int)nextLong();
        int[] moves = new int[count];
        for (int i = 0; i < count; i++)
            moves[i] = (int)nextLong();
        Arrays.sort(moves);
        boolean[] win = new boolean[stones + 1];
        // Taking the last stone loses. Larger moves cannot be made at all.
        for (int left = 1; left <= stones; left++)
            for (int take : moves) {
                if (take >= left)
                    break;
                if (!win[left - take]) {
                    win[left] = true;
                    break;
                }
            }
        System.out.println(win[stones] ? 1 : 2);
    }
}
