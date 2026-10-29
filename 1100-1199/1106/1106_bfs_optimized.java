public class Main {
    private static final int INPUT_BUFFER_SIZE = 4096;
    private static final byte[] input = new byte[INPUT_BUFFER_SIZE];
    private static int position;
    private static int length;

    // the numbers are parsed by hand from a small buffer, faster than StreamTokenizer
    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return input[position++];
    }

    private static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value * sign;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        // at most 100 vertices, so a vertex number fits in a byte
        byte[][] adj = new byte[n + 1][];
        byte[] neighbours = new byte[n];
        for (int v = 1; v <= n; v++) {
            int count = 0;
            for (int u = (int)nextLong(); u != 0; u = (int)nextLong()) {
                neighbours[count++] = (byte)u;
            }
            adj[v] = java.util.Arrays.copyOf(neighbours, count);
        }
        // colour a BFS tree of every component by depth parity: each member has a
        // tree neighbour, its parent or a child, in the other team (side 0: not
        // reached yet; 1 and 2: the teams, a child takes the other one)
        byte[] side = new byte[n + 1];
        // every vertex enters the queue once, so n cells are enough
        int[] queue = new int[n];
        for (int root = 1; root <= n; root++) {
            if (side[root] != 0) {
                continue;
            }
            side[root] = 1;
            queue[0] = root;
            int tail = 1;
            for (int head = 0; head < tail; head++) {
                int v = queue[head];
                for (int u : adj[v]) {
                    if (side[u] == 0) {
                        side[u] = (byte)(1 + side[v] % 2);
                        queue[tail++] = u;
                    }
                }
            }
        }
        int count = 0;
        StringBuilder team = new StringBuilder();
        for (int v = 1; v <= n; v++) {
            if (side[v] == 1) {
                if (count++ != 0) {
                    team.append(' ');
                }
                team.append(v);
            }
        }
        System.out.println(count);
        System.out.println(team);
    }
}
