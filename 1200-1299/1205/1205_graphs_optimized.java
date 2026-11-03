public class Main {
    static final int BUFFER_SIZE = 4096, BASE = 10, WORD_BITS = Long.SIZE;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * BASE + c - '0';
            c = read();
        }
        return value;
    }

    static double nextDouble() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        StringBuilder token = new StringBuilder();
        while (c > ' ') {
            token.append((char)c);
            c = read();
        }
        // Preserve signs, arbitrary decimal lengths and scientific notation.
        return Double.parseDouble(token.toString());
    }

    public static void main(String[] args) throws java.io.IOException {
        double walk = nextDouble(), metro = nextDouble();
        int n = nextInt(), total = n + 2, start = n, goal = n + 1;
        int words = (total + WORD_BITS - 1) / WORD_BITS;
        double[] x = new double[total], y = new double[total];
        for (int i = 0; i < n; i++) {
            x[i] = nextDouble();
            y[i] = nextDouble();
        }
        long[] linked = new long[total * words];
        boolean[] active = new boolean[total];
        int edges = 0;
        while (true) {
            int a = nextInt(), b = nextInt();
            if (a == 0 && b == 0)
                break;
            a--;
            b--;
            linked[a * words + b / WORD_BITS] |= 1L << (b % WORD_BITS);
            linked[b * words + a / WORD_BITS] |= 1L << (a % WORD_BITS);
            active[a] = active[b] = true;
            edges++;
        }
        for (int v = start; v <= goal; v++) {
            x[v] = nextDouble();
            y[v] = nextDouble();
        }
        if (edges == 0 || walk == metro || (x[start] == x[goal] && y[start] == y[goal])) {
            System.out.println(Math.hypot(x[start] - x[goal], y[start] - y[goal]) / walk);
            System.out.println(0);
            return;
        }
        active[start] = active[goal] = true;
        double[] distance = new double[total];
        int[] previous = new int[total], vertices = new int[total];
        boolean[] done = new boolean[total];
        int count = 0;
        for (int v = 0; v < total; v++) {
            distance[v] = Double.POSITIVE_INFINITY;
            if (active[v])
                vertices[count++] = v;
        }
        distance[start] = 0;
        while (true) {
            int u = -1;
            for (int i = 0; i < count; i++) {
                int v = vertices[i];
                if (!done[v] && (u < 0 || distance[v] < distance[u]))
                    u = v;
            }
            if (u == goal)
                break;
            done[u] = true;
            for (int i = 0; i < count; i++) {
                int v = vertices[i];
                if (!done[v]) {
                    boolean train =
                        (linked[u * words + v / WORD_BITS] & (1L << (v % WORD_BITS))) != 0;
                    double candidate =
                        distance[u] + Math.hypot(x[v] - x[u], y[v] - y[u]) / (train ? metro : walk);
                    if (candidate < distance[v]) {
                        distance[v] = candidate;
                        previous[v] = u;
                    }
                }
            }
        }
        int[] path = new int[total];
        int length = 0;
        for (int v = previous[goal]; v != start; v = previous[v])
            path[length++] = v + 1;
        StringBuilder out = new StringBuilder(Double.toString(distance[goal]));
        out.append('\n').append(length);
        for (int i = length - 1; i >= 0; i--)
            out.append(' ').append(path[i]);
        System.out.println(out);
    }
}
