import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int STEP = 2;    // columns two apart keep every pair of points farther than 1
    static final int LIMIT = 999; // the leftmost column, so that 1000 columns fit in [-999, 999]

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        in.nextToken();
        int n = (int)in.nval;
        // adjacency as linked lists in arrays: head, next and target per wire end
        int[] head = new int[n + 1], next = new int[2 * n], to = new int[2 * n];
        Arrays.fill(head, -1);
        for (int i = 0; i < 2 * (n - 1); i += 2) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            to[i] = b;
            next[i] = head[a];
            head[a] = i;
            to[i + 1] = a;
            next[i + 1] = head[b];
            head[b] = i + 1;
        }
        // column = preorder index, row = depth: the subtrees of the vertices on
        // one row take disjoint ranges of columns, so no two wires cross
        int[] x = new int[n + 1], y = new int[n + 1], stack = new int[n];
        boolean[] seen = new boolean[n + 1];
        seen[1] = true;
        stack[0] = 1;
        int top = 1, order = 0;
        while (top > 0) {
            int v = stack[--top];
            x[v] = order++ * STEP - LIMIT;
            for (int e = head[v]; e >= 0; e = next[e])
                if (!seen[to[e]]) {
                    seen[to[e]] = true;
                    y[to[e]] = y[v] + 1;
                    stack[top++] = to[e];
                }
        }
        StringBuilder out = new StringBuilder();
        for (int v = 1; v <= n; v++)
            out.append(x[v]).append(' ').append(y[v]).append('\n');
        System.out.print(out);
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[4096];
        private int position, length;
        private String pending;
        double nval;
        String sval;

        int read() throws IOException {
            if (position >= length) {
                length = System.in.read(data);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return data[position++] & 255;
        }

        private int first() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        long nextLong() throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        int nextInt() throws IOException { return (int)nextLong(); }

        String next() throws IOException {
            if (pending != null) {
                String word = pending;
                pending = null;
                return word;
            }
            int c = first();
            if (c < 0)
                return null;
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }

        boolean hasNext() throws IOException {
            if (pending == null)
                pending = next();
            return pending != null;
        }

        void nextToken() throws IOException {
            int c = first();
            if ((c >= '0' && c <= '9') || c == '-' || c == '+') {
                boolean negative = c == '-';
                if (negative || c == '+')
                    c = read();
                long value = 0;
                while (c >= '0' && c <= '9') {
                    value = value * 10 + c - '0';
                    c = read();
                }
                nval = negative ? -value : value;
                sval = null;
            } else {
                StringBuilder word = new StringBuilder();
                while (c > ' ') {
                    word.append((char)c);
                    c = read();
                }
                sval = word.toString();
            }
        }

        long scaled(int scale) throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            boolean fraction = false;
            while (c > ' ') {
                if (c == '.')
                    fraction = true;
                else {
                    value = value * 10 + c - '0';
                    if (fraction)
                        scale /= 10;
                }
                c = read();
            }
            value *= scale;
            return negative ? -value : value;
        }
    }
}
