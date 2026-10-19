import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 65536;
    private static final int DIGIT_CAPACITY = 10;

    private static final class FastInput {
        private final BufferedInputStream input =
                new BufferedInputStream(System.in, BUFFER_SIZE);
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current = read();
            while (current <= ' ' && current >= 0) {
                current = read();
            }
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static int find(int[] representative, int vertex) {
        while (representative[vertex] != vertex) {
            representative[vertex] = representative[representative[vertex]];
            vertex = representative[vertex];
        }
        return vertex;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int[] head = new int[n + 1];
        Arrays.fill(head, -1);
        int[] to = new int[2 * (n - 1)];
        int[] next = new int[to.length];
        for (int edge = 0; edge < to.length; edge += 2) {
            int u = input.nextInt();
            int v = input.nextInt();
            to[edge] = v;
            next[edge] = head[u];
            head[u] = edge;
            to[edge + 1] = u;
            next[edge + 1] = head[v];
            head[v] = edge + 1;
        }

        int[] parent = new int[n + 1];
        int[] representative = new int[n + 1];
        int[] tin = new int[n + 1];
        Arrays.fill(tin, -1);
        for (int vertex = 1; vertex <= n; vertex++) {
            representative[vertex] = vertex;
        }
        parent[1] = 1;
        int[] order = new int[n];
        int orderLength = 0;
        int[] adjacent = new int[n - 1];
        int[] stack = new int[2 * n];
        int stackLength = 1;
        stack[0] = 1;
        while (stackLength > 0) {
            int u = stack[--stackLength];
            if (u < 0) {
                representative[-u] = parent[-u];
                continue;
            }
            tin[u] = orderLength;
            order[orderLength++] = u;
            // Finished subtrees point to their nearest active ancestor.
            if (u > 1 && tin[u - 1] >= 0) {
                adjacent[u - 2] = tin[find(representative, u - 1)];
            }
            if (u < n && tin[u + 1] >= 0) {
                adjacent[u - 1] = tin[find(representative, u + 1)];
            }
            stack[stackLength++] = -u;
            for (int edge = head[u]; edge != -1; edge = next[edge]) {
                int v = to[edge];
                if (v != parent[u]) {
                    parent[v] = u;
                    stack[stackLength++] = v;
                }
            }
        }

        int[] logarithm = new int[n + 1];
        for (int length = 2; length <= n; length++) {
            logarithm[length] = logarithm[length / 2] + 1;
        }
        int[][] table = new int[logarithm[n] + 1][];
        table[0] = adjacent;
        for (int level = 1, span = 1; 2 * span <= adjacent.length; level++, span *= 2) {
            int[] previous = table[level - 1];
            int[] row = new int[adjacent.length - 2 * span + 1];
            for (int index = 0; index < row.length; index++) {
                row[index] = Math.min(previous[index], previous[index + span]);
            }
            table[level] = row;
        }

        int queries = input.nextInt();
        BufferedOutputStream output = new BufferedOutputStream(System.out, BUFFER_SIZE);
        byte[] digits = new byte[DIGIT_CAPACITY];
        for (int query = 0; query < queries; query++) {
            int left = input.nextInt();
            int right = input.nextInt();
            int answer = left;
            if (left < right) {
                int level = logarithm[right - left];
                int[] row = table[level];
                int value = Math.min(row[left - 1], row[right - 1 - (1 << level)]);
                answer = order[value];
            }
            int start = digits.length;
            do {
                digits[--start] = (byte) ('0' + answer % 10);
                answer /= 10;
            } while (answer > 0);
            output.write(digits, start, digits.length - start);
            output.write('\n');
        }
        output.flush();
    }
}
