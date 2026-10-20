import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static class FastScanner {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int current;
            do {
                current = input.read();
            } while (current <= ' ' && current != -1);
            int value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = input.read();
            }
            return value;
        }
    }

    private static void fill(int[] required, int[] next, int parity, long limit, int count) {
        while (next[parity] < required.length && next[parity] <= limit) {
            required[next[parity]] = count;
            next[parity] += 2;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        int n = input.nextInt();
        int m = input.nextInt();
        int k = input.nextInt();
        int[] head = new int[n];
        Arrays.fill(head, -1);
        int[] to = new int[2 * m];
        int[] link = new int[2 * m];
        for (int edge = 0; edge < 2 * m; edge += 2) {
            int u = input.nextInt() - 1;
            int v = input.nextInt() - 1;
            to[edge] = v;
            link[edge] = head[u];
            head[u] = edge;
            to[edge + 1] = u;
            link[edge + 1] = head[v];
            head[v] = edge + 1;
        }

        int[] distance = new int[2 * n];
        Arrays.fill(distance, -1);
        distance[0] = 0;
        int[] queue = new int[2 * n];
        int back = 1;
        for (int front = 0; front < back; front++) {
            int state = queue[front];
            int vertex = state / 2;
            int parity = (state % 2) ^ 1;
            for (int edge = head[vertex]; edge != -1; edge = link[edge]) {
                int nextState = 2 * to[edge] + parity;
                if (distance[nextState] == -1) {
                    distance[nextState] = distance[state] + 1;
                    queue[back++] = nextState;
                }
            }
        }

        int[] cups = new int[k];
        for (int i = 0; i < k; i++) {
            cups[i] = input.nextInt();
        }
        Arrays.sort(cups);
        long[] prefixEven = new long[k + 1];
        long[] prefixOdd = new long[k + 1];
        prefixEven[0] = -1;
        prefixOdd[0] = -1;
        for (int i = 0; i < k; i++) {
            prefixEven[i + 1] = prefixEven[i];
            prefixOdd[i + 1] = prefixOdd[i];
            if (cups[i] % 2 == 0) {
                prefixEven[i + 1] = cups[i];
            } else {
                prefixOdd[i + 1] = cups[i];
            }
        }
        int[] required = new int[2 * n];
        Arrays.fill(required, -1);
        required[0] = 0;
        int[] next = {2, 1};
        long[] smallest = {-1, -1};
        long sum = 0;
        for (int count = 1; count <= k; count++) {
            int index = k - count;
            int cup = cups[index];
            sum += cup;
            smallest[cup % 2] = cup;
            int parity = (int) (sum % 2);
            fill(required, next, parity, sum, count);
            // An optimal sum of the other parity replaces one selected cup.
            long best = -1;
            if (smallest[0] != -1 && prefixOdd[index] != -1) {
                best = sum - smallest[0] + prefixOdd[index];
            }
            if (smallest[1] != -1 && prefixEven[index] != -1) {
                best = Math.max(best, sum - smallest[1] + prefixEven[index]);
            }
            fill(required, next, parity ^ 1, best, count);
        }

        StringBuilder output = new StringBuilder();
        for (int vertex = 0; vertex < n; vertex++) {
            int answer = -1;
            for (int parity = 0; parity < 2; parity++) {
                int d = distance[2 * vertex + parity];
                if (d != -1 && required[d] != -1 && (answer == -1 || required[d] < answer)) {
                    answer = required[d];
                }
            }
            if (vertex != 0) {
                output.append(' ');
            }
            output.append(answer);
        }
        output.append('\n');
        System.out.print(output);
    }
}
