import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] head, to, next;
    static boolean[] victims, cleared;
    static final int PARENTS = 2;
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, available;
    // refillable storage bounds input memory independently of the record count.
    static int read() throws IOException {
        if (position >= available) {
            available = System.in.read(BUFFER);
            position = 0;
            if (available < 0)
                return -1;
        }
        return BUFFER[position++] & BYTE_MASK;
    }
    static String word() throws IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        if (c < 0)
            return null;
        StringBuilder value = new StringBuilder();
        while (c > ' ') {
            value.append((char)c);
            c = read();
        }
        return value.toString();
    }
    // marks everyone reachable from the victims along one kind of link
    static void clear(int direction, int n) {
        int[] stack = new int[n];
        boolean[] seen = new boolean[n + 1];
        int top = 0;
        // marking before pushing puts each person on the stack at most once.
        for (int i = 1; i <= n; ++i)
            if (victims[i]) {
                stack[top++] = i;
                seen[i] = true;
            }
        while (top > 0) {
            int v = stack[--top];
            for (int e = head[direction][v]; e != 0; e = next[direction][e]) {
                int u = to[direction][e];
                if (!seen[u]) {
                    seen[u] = cleared[u] = true;
                    stack[top++] = u;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(word());
        // two parents per person give room for 2n edges; the statement does not
        // forbid repeated lines, so the arrays double when they fill up.
        head = new int[2][n + 1];
        to = new int[2][PARENTS * n + 1];
        next = new int[2][PARENTS * n + 1];
        int edges = 0;
        for (String value; !(value = word()).equals("BLOOD");) {
            int child = Integer.parseInt(value), parent = Integer.parseInt(word());
            if (++edges == to[0].length)
                for (int d = 0; d < 2; ++d) {
                    to[d] = Arrays.copyOf(to[d], 2 * edges);
                    next[d] = Arrays.copyOf(next[d], 2 * edges);
                }
            to[0][edges] = parent;
            next[0][edges] = head[0][child];
            head[0][child] = edges;
            to[1][edges] = child;
            next[1][edges] = head[1][parent];
            head[1][parent] = edges;
        }
        victims = new boolean[n + 1];
        cleared = new boolean[n + 1];
        for (String value; (value = word()) != null;) {
            int v = Integer.parseInt(value);
            victims[v] = cleared[v] = true;
        }
        // the werewolf spares its ancestors and descendants, so no ancestor and
        // no descendant of a victim can be the werewolf
        clear(0, n);
        clear(1, n);
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; ++i)
            if (!cleared[i])
                out.append(out.length() > 0 ? " " : "").append(i);
        System.out.println(out.length() > 0 ? out : "0");
    }
}
