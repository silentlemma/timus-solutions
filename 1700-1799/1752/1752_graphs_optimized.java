public class Main {
    static final char UNVISITED = Character.MAX_VALUE;
    static int n, q;
    static char[] head, to, following, askHead, askNext, distance, answer, depth, path, stack;
    static final int BUFFER_SIZE = 4096, BASE = 10, MAX_DIGITS = 5;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available, used;
    static final byte[] output = new byte[BUFFER_SIZE];

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

    static void flush() throws java.io.IOException {
        if (used != 0) {
            System.out.write(output, 0, used);
            used = 0;
        }
    }

    static void writeAnswer(int value) throws java.io.IOException {
        // Vertex IDs need at most MAX_DIGITS decimal digits and one newline.
        if (used + MAX_DIGITS + 1 > output.length)
            flush();
        int first = used;
        do {
            output[used++] = (byte)('0' + value % BASE);
            value /= BASE;
        } while (value != 0);
        for (int left = first, right = used - 1; left < right; left++, right--) {
            byte digit = output[left];
            output[left] = output[right];
            output[right] = digit;
        }
        output[used++] = '\n';
    }

    static int walk(int root) {
        for (int v = 1; v <= n; v++)
            depth[v] = UNVISITED;
        depth[root] = 0;
        stack[0] = (char)root;
        int top = 1, deepest = root;
        while (top > 0) {
            int vertex = stack[--top], dv = depth[vertex];
            path[dv] = (char)vertex;
            if (dv > depth[deepest])
                deepest = vertex;
            for (int query = askHead[vertex]; query != 0; query = askNext[query])
                if (answer[query] == 0 && distance[query] <= dv)
                    answer[query] = path[dv - distance[query]];
            for (int edge = head[vertex]; edge != 0; edge = following[edge]) {
                int child = to[edge];
                if (depth[child] == UNVISITED) {
                    depth[child] = (char)(dv + 1);
                    stack[top++] = (char)child;
                }
            }
        }
        return deepest;
    }

    public static void main(String[] args) throws Exception {
        n = nextInt();
        q = nextInt();
        // Vertex<=20000, edge<=39998, query<=50000 fit unsigned16-bit char.
        // Zero is reserved for missing links, and all valid IDs start at one.
        head = new char[n + 1];
        to = new char[2 * n];
        following = new char[2 * n];
        int edge = 0;
        for (int i = 0; i < n - 1; i++) {
            int a = nextInt(), b = nextInt();
            to[++edge] = (char)b;
            following[edge] = head[a];
            head[a] = (char)edge;
            to[++edge] = (char)a;
            following[edge] = head[b];
            head[b] = (char)edge;
        }
        askHead = new char[n + 1];
        askNext = new char[q + 1];
        distance = new char[q + 1];
        answer = new char[q + 1];
        for (int i = 1; i <= q; i++) {
            int vertex = nextInt();
            distance[i] = (char)nextInt();
            askNext[i] = askHead[vertex];
            askHead[vertex] = (char)i;
        }
        depth = new char[n + 1];
        path = new char[n + 1];
        stack = new char[n + 1];
        // A path to one of the diameter ends reaches every feasible distance.
        int a = walk(1), b = walk(a);
        walk(b);
        for (int i = 1; i <= q; i++)
            writeAnswer(answer[i]);
        flush();
    }
}
