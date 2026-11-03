public class Main {
    static final int WORD_BITS = 64;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int m = nextInt(), n = nextInt(), edges = nextInt();
        int left = Math.min(m, n), right = Math.max(m, n);
        int words = (right + WORD_BITS - 1) / WORD_BITS;
        long[] adjacent = new long[left * words], free = new long[words];
        java.util.Arrays.fill(free, -1L);
        for (int i = 0; i < edges; i++) {
            int a = nextInt() - 1, b = nextInt() - 1;
            if (m > n) {
                int temporary = a;
                a = b;
                b = temporary;
            }
            adjacent[a * words + b / WORD_BITS] |= 1L << (b % WORD_BITS);
        }
        int[] matchL = new int[left], matchR = new int[right];
        int[] parent = new int[right], queue = new int[left];
        java.util.Arrays.fill(matchL, -1);
        java.util.Arrays.fill(matchR, -1);
        int size = 0;
        for (int root = 0; root < left; root++) {
            long[] seen = new long[words];
            int head = 0, tail = 1, target = -1;
            queue[0] = root;
            while (head < tail && target < 0) {
                int v = queue[head++];
                for (int b = 0; b < words; b++) {
                    long available = adjacent[v * words + b] & free[b];
                    if (available != 0) {
                        target = b * WORD_BITS + Long.numberOfTrailingZeros(available);
                        parent[target] = v;
                        break;
                    }
                }
                if (target >= 0)
                    break;
                // Unseen neighbors are all matched. Their partners enter
                // the BFS queue once, so at most left slots are needed.
                for (int b = 0; b < words; b++) {
                    long options = adjacent[v * words + b] & ~seen[b];
                    seen[b] |= options;
                    while (options != 0) {
                        int u = b * WORD_BITS + Long.numberOfTrailingZeros(options);
                        parent[u] = v;
                        queue[tail++] = matchR[u];
                        options &= options - 1;
                    }
                }
            }
            if (target >= 0) {
                free[target / WORD_BITS] &= ~(1L << (target % WORD_BITS));
                // Flip the discovered path back to its free left root.
                while (target >= 0) {
                    int v = parent[target], old = matchL[v];
                    matchL[v] = target;
                    matchR[target] = v;
                    target = old;
                }
                size++;
            }
        }
        System.out.println(m + n - size);
    }
}
