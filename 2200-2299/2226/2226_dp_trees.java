import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_LENGTH = 1000000000;
    private static final int INF = MAX_LENGTH + 1;

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c != -1);
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.nextInt();
        int[] head = new int[n + 1];
        int[] to = new int[2 * (n - 1)];
        int[] next = new int[to.length];
        Arrays.fill(head, -1);
        int[] first = new int[n + 1];
        int[] second = new int[n + 1];
        int[] shortest = new int[n + 1];
        int[] nextShortest = new int[n + 1];
        Arrays.fill(shortest, INF);
        Arrays.fill(nextShortest, INF);
        int edge = 0;
        for (int i = 1; i < n; ++i) {
            int u = input.nextInt();
            int v = input.nextInt();
            int length = input.nextInt();
            for (int direction = 0; direction < 2; ++direction) {
                to[edge] = v;
                next[edge] = head[u];
                head[u] = edge++;
                if (length < shortest[u]) {
                    nextShortest[u] = shortest[u];
                    second[u] = first[u];
                    shortest[u] = length;
                    first[u] = v;
                } else if (length < nextShortest[u]) {
                    nextShortest[u] = length;
                    second[u] = v;
                }
                int swap = u;
                u = v;
                v = swap;
            }
        }
        int[] parent = new int[n + 1];
        int[] order = new int[n];
        order[0] = 1;
        int size = 1;
        for (int i = 0; i < n; ++i) {
            int v = order[i];
            for (int e = head[v]; e != -1; e = next[e]) {
                int u = to[e];
                if (u != parent[v]) {
                    parent[u] = v;
                    order[size++] = u;
                }
            }
        }

        // down[v] is the endpoint after arriving at v from its parent.
        int[] down = new int[n + 1];
        int[] up = new int[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            int v = order[i];
            int u = first[v] == parent[v] ? second[v] : first[v];
            down[v] = u == 0 ? v : down[u];
        }
        // up[v] is the endpoint after leaving v for its parent.
        for (int i = 1; i < n; ++i) {
            int v = order[i];
            int p = parent[v];
            int u = first[p] == v ? second[p] : first[p];
            up[v] = u == 0 ? p : (u == parent[p] ? up[p] : down[u]);
        }
        StringBuilder output = new StringBuilder();
        for (int v = 1; v <= n; ++v) {
            if (v != 1) {
                output.append(' ');
            }
            output.append(first[v] == parent[v] ? up[v] : down[v]);
        }
        System.out.println(output);
    }
}
