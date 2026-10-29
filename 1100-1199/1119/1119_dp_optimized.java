import java.util.Arrays;

public class Main {
    private static final int SIDE = 100;
    private static final int MAX_COORDINATE = 1000;
    private static final int COORDINATE_BASE = MAX_COORDINATE + 1;

    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the input is read in 1 KB blocks and parsed by hand, which needs much
    // less memory than Scanner
    private static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = read();
        } while (ch <= ' ' && ch >= 0);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int width = nextInt();
        int height = nextInt();
        int count = nextInt();
        int[] blocks = new int[count];
        for (int i = 0; i < count; ++i) {
            int x = nextInt();
            int y = nextInt();
            // a block is one int x * 1001 + y: sorting the ints sorts the pairs,
            // with no array of pairs and no comparator
            blocks[i] = x * COORDINATE_BASE + y;
        }
        Arrays.sort(blocks);
        // a route can use a chain of diagonal blocks increasing in both
        // coordinates; each one replaces two sides by one diagonal
        int[] chain = new int[count];
        int best = 0;
        for (int i = 0; i < count; ++i) {
            int x = blocks[i] / COORDINATE_BASE;
            int y = blocks[i] % COORDINATE_BASE;
            chain[i] = 1;
            for (int j = 0; j < i; ++j) {
                if (blocks[j] / COORDINATE_BASE < x && blocks[j] % COORDINATE_BASE < y) {
                    chain[i] = Math.max(chain[i], chain[j] + 1);
                }
            }
            best = Math.max(best, chain[i]);
        }
        double length = SIDE * (width + height - 2 * best) + SIDE * Math.sqrt(2) * best;
        System.out.println(Math.round(length));
    }
}
