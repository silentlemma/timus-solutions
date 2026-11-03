public class Main {
    static final int[][] MOVES = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                                  {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
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

    static int n, total;
    static long[] adjacency;
    static int[] path;
    static int[][] order, degree;

    static boolean tour(int v, long remaining, int depth) {
        path[depth] = v;
        if (remaining == 0)
            return true;
        long choices = adjacency[v] & remaining;
        if (choices != 0 && (remaining & (remaining - 1)) != 0) {
            // A nontrivial remaining path cannot contain an isolated vertex.
            for (long scan = remaining; scan != 0; scan &= scan - 1)
                if ((adjacency[Long.numberOfTrailingZeros(scan)] & remaining) == 0)
                    return false;
        }
        int count = 0;
        while (choices != 0) {
            int w = Long.numberOfTrailingZeros(choices);
            choices &= choices - 1;
            int d = Long.bitCount(adjacency[w] & remaining), j = count++;
            while (j > 0 && degree[depth][j - 1] > d) {
                degree[depth][j] = degree[depth][j - 1];
                order[depth][j] = order[depth][j - 1];
                j--;
            }
            degree[depth][j] = d;
            order[depth][j] = w;
        }
        for (int i = 0; i < count; i++) {
            int w = order[depth][i];
            if (tour(w, remaining ^ (1L << w), depth + 1))
                return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        n = nextInt();
        total = n * n;
        adjacency = new long[total];
        path = new int[total];
        order = new int[total][MOVES.length];
        degree = new int[total][MOVES.length];
        for (int c = 0; c < n; c++)
            for (int r = 0; r < n; r++)
                for (int[] move : MOVES) {
                    int x = c + move[0], y = r + move[1];
                    if (0 <= x && x < n && 0 <= y && y < n)
                        adjacency[c * n + r] |= 1L << (x * n + y);
                }
        long whole = total == Long.SIZE ? -1L : (1L << total) - 1;
        // Reflect rows/columns and transpose to obtain a triangular orbit set.
        for (int c = 0; c < (n + 1) / 2; c++)
            for (int r = c; r < (n + 1) / 2; r++) {
                int v = c * n + r;
                if (tour(v, whole ^ (1L << v), 0)) {
                    StringBuilder out = new StringBuilder();
                    for (int w : path)
                        out.append((char)('a' + w / n)).append(w % n + 1).append('\n');
                    System.out.print(out);
                    return;
                }
            }
        System.out.println("IMPOSSIBLE");
    }
}
