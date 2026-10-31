import java.io.IOException;

public class Main {

    // refilling this buffer bounds input storage independently of input size.
    static final int INPUT_BUFFER = 4096;
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int pos, len;

    static int read() throws IOException {
        if (pos == len) {
            len = System.in.read(buffer);
            pos = 0;
            if (len <= 0)
                return -1;
        }
        return buffer[pos++];
    }

    static int next() throws IOException {
        int c = read();
        while (c != -1 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        // n <= 100 keeps this matrix small and avoids boxed adjacency lists.
        boolean[][] children = new boolean[n + 1][n + 1];
        int[] parents = new int[n + 1], order = new int[n];
        for (int v = 1; v <= n; v++) {
            for (int c = next(); c != 0; c = next()) {
                if (!children[v][c]) {
                    children[v][c] = true;
                    parents[c]++;
                }
            }
        }
        int size = 0;
        for (int v = 1; v <= n; v++)
            if (parents[v] == 0)
                order[size++] = v;
        for (int i = 0; i < size; i++) {
            for (int c = 1; c <= n; c++)
                if (children[order[i]][c] && --parents[c] == 0)
                    order[size++] = c;
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < size; i++) {
            if (i > 0)
                out.append(' ');
            out.append(order[i]);
        }
        System.out.println(out);
    }
}
