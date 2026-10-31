import java.util.Arrays;
public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return BUFFER[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), m = nextInt(), width = n + 1;
        // positive costs at most 10000 fit in short; zero means no edge.
        short[] cost = new short[width * width];
        int[] indegree = new int[width], best = new int[width], order = new int[n];
        for (int i = 0; i < m; i++) {
            int a = nextInt(), b = nextInt(), c = nextInt();
            cost[a * width + b] = (short)c;
            indegree[b]++;
        }
        int start = nextInt(), finish = nextInt();
        Arrays.fill(best, -1);
        // at most 499 edges of cost 10000 keep path sums within signed 32 bits.
        best[start] = 0;
        int size = 0;
        for (int v = 1; v <= n; v++)
            if (indegree[v] == 0)
                order[size++] = v;
        for (int at = 0; at < size; at++) {
            int v = order[at];
            for (int w = 1; w <= n; w++) {
                int c = cost[v * width + w];
                if (c == 0)
                    continue;
                if (best[v] >= 0 && best[v] + c > best[w])
                    best[w] = best[v] + c;
                if (--indegree[w] == 0)
                    order[size++] = w;
            }
        }
        System.out.println(best[finish] < 0 ? "No solution" : String.valueOf(best[finish]));
    }
}
