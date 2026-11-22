public class Main {
    static final int COORDINATE_BYTES = 3;
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
    static int[] order, degree, remainingDegree;
    static long isolated;

    static void restore(int v, long remaining, long previousIsolated) {
        for (long scan = adjacency[v] & remaining; scan != 0; scan &= scan - 1)
            remainingDegree[Long.numberOfTrailingZeros(scan)]++;
        isolated = previousIsolated;
    }

    static boolean tour(int v, long remaining, int depth) {
        path[depth] = v;
        if (remaining == 0)
            return true;
        long previousIsolated = isolated;
        isolated &= ~(1L << v);
        long choices = adjacency[v] & remaining;
        for (long scan = choices; scan != 0; scan &= scan - 1) {
            int w = Long.numberOfTrailingZeros(scan);
            if (--remainingDegree[w] == 0)
                isolated |= 1L << w;
        }
        if (isolated != 0 && (remaining & (remaining - 1)) != 0) {
            restore(v, remaining, previousIsolated);
            return false;
        }
        int count = 0, offset = depth * MOVES.length;
        while (choices != 0) {
            int w = Long.numberOfTrailingZeros(choices);
            choices &= choices - 1;
            int d = remainingDegree[w], j = count++;
            while (j > 0 && degree[offset + j - 1] > d) {
                degree[offset + j] = degree[offset + j - 1];
                order[offset + j] = order[offset + j - 1];
                j--;
            }
            degree[offset + j] = d;
            order[offset + j] = w;
        }
        for (int i = 0; i < count; i++) {
            int w = order[offset + i];
            if (tour(w, remaining ^ (1L << w), depth + 1))
                return true;
        }
        restore(v, remaining, previousIsolated);
        return false;
    }

    public static void main(String[] args) throws Exception {
        n = nextInt();
        total = n * n;
        adjacency = new long[total];
        path = new int[total];
        order = new int[total * MOVES.length];
        degree = new int[total * MOVES.length];
        for (int c = 0; c < n; c++)
            for (int r = 0; r < n; r++)
                for (int[] move : MOVES) {
                    int x = c + move[0], y = r + move[1];
                    if (0 <= x && x < n && 0 <= y && y < n)
                        adjacency[c * n + r] |= 1L << (x * n + y);
                }
        remainingDegree = new int[total];
        isolated = 0;
        for (int v = 0; v < total; v++) {
            remainingDegree[v] = Long.bitCount(adjacency[v]);
            if (remainingDegree[v] == 0)
                isolated |= 1L << v;
        }
        long whole = total == Long.SIZE ? -1L : (1L << total) - 1;
        // Reflect rows/columns and transpose to obtain a triangular orbit set.
        for (int c = 0; c < (n + 1) / 2; c++)
            for (int r = c; r < (n + 1) / 2; r++) {
                int v = c * n + r;
                if (tour(v, whole ^ (1L << v), 0)) {
                    // Each coordinate has one letter and one digit because n <= 8.
                    byte[] out = new byte[COORDINATE_BYTES * total];
                    int at = 0;
                    for (int w : path) {
                        out[at++] = (byte)('a' + w / n);
                        out[at++] = (byte)('1' + w % n);
                        out[at++] = '\n';
                    }
                    System.out.write(out);
                    return;
                }
            }
        byte[] impossible = {'I', 'M', 'P', 'O', 'S', 'S', 'I', 'B', 'L', 'E', '\n'};
        System.out.write(impossible);
    }
}
