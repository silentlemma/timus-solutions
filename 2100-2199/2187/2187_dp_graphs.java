import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final long NEGATIVE_INFINITY = Long.MIN_VALUE / 2;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int size;

        private int read() throws IOException {
            if (position == size) {
                size = input.read(buffer);
                position = 0;
                if (size < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character = read();
            while (character <= ' ') {
                character = read();
            }
            int value = 0;
            while (character > ' ') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int m = input.nextInt();
        long[] treasure = new long[n];
        long[] cost = new long[n];
        for (int vertex = 0; vertex < n; vertex++) {
            treasure[vertex] = input.nextInt();
        }
        for (int length = 1; length < n; length++) {
            cost[length] = input.nextInt();
        }

        int[] first = new int[m];
        int[] second = new int[m];
        int[] degree = new int[n];
        for (int edge = 0; edge < m; edge++) {
            first[edge] = input.nextInt() - 1;
            second[edge] = input.nextInt() - 1;
            degree[first[edge]]++;
            degree[second[edge]]++;
        }
        int[] offset = new int[n + 1];
        for (int edge = 0; edge < m; edge++) {
            int u = first[edge];
            int v = second[edge];
            if (degree[u] < degree[v]) {
                offset[u + 1]++;
            } else if (degree[v] < degree[u]) {
                offset[v + 1]++;
            }
        }
        for (int vertex = 0; vertex < n; vertex++) {
            offset[vertex + 1] += offset[vertex];
        }
        int[] next = offset.clone();
        int[] adjacent = new int[offset[n]];
        for (int edge = 0; edge < m; edge++) {
            int u = first[edge];
            int v = second[edge];
            if (degree[u] < degree[v]) {
                adjacent[next[u]++] = v;
            } else if (degree[v] < degree[u]) {
                adjacent[next[v]++] = u;
            }
        }

        int[] count = new int[n + 1];
        for (int value : degree) {
            count[value + 1]++;
        }
        for (int value = 0; value < n; value++) {
            count[value + 1] += count[value];
        }
        int[] order = new int[n];
        for (int vertex = 0; vertex < n; vertex++) {
            order[count[degree[vertex]]++] = vertex;
        }

        // A state stores the profit before paying for the unfinished journey.
        long[][] states = new long[n][];
        states[0] = new long[] {treasure[0]};
        long answer = treasure[0];
        for (int u : order) {
            long[] current = states[u];
            states[u] = null;
            if (current == null) {
                continue;
            }
            long best = current[0];
            for (int length = 1; length < current.length; length++) {
                if (current[length] != NEGATIVE_INFINITY) {
                    best = Math.max(best, current[length] - cost[length] + treasure[u]);
                }
            }
            current[0] = best;
            answer = Math.max(answer, best);
            for (int edge = offset[u]; edge < offset[u + 1]; edge++) {
                int v = adjacent[edge];
                long[] target = states[v];
                int oldLength = target == null ? 0 : target.length;
                if (oldLength <= current.length) {
                    target = target == null ? new long[current.length + 1]
                            : Arrays.copyOf(target, current.length + 1);
                    Arrays.fill(target, oldLength, target.length, NEGATIVE_INFINITY);
                }
                for (int length = 0; length < current.length; length++) {
                    target[length + 1] = Math.max(target[length + 1], current[length]);
                }
                states[v] = target;
            }
        }
        System.out.println(answer);
    }
}
