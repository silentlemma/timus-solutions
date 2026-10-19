import java.io.BufferedInputStream;

public class Main {
    private static final int INF = 1000000000;
    private static int[][] cost;
    private static int[] previous;
    private static int[] current;
    private static int[] parent;

    private static void fill(int left, int right, int first, int last) {
        if (left > right) {
            return;
        }
        int middle = (left + right) / 2;
        int best = INF;
        int split = first;
        for (int cut = first; cut <= Math.min(last, middle - 1); cut++) {
            int value = previous[cut] + cost[cut + 1][middle];
            if (value < best) {
                best = value;
                split = cut;
            }
        }
        current[middle] = best;
        parent[middle] = split;
        fill(left, middle - 1, first, split);
        fill(middle + 1, right, split, last);
    }

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws Exception {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws Exception {
        Input input = new Input();
        int n = input.next();
        int k = input.next();
        int width = n + 1;
        int[][] weights = new int[width][width];
        cost = new int[width][width];
        for (int left = 1; left < n; left++) {
            for (int right = left + 1; right <= n; right++) {
                weights[left][right] = input.next();
            }
        }
        for (int left = n - 1; left >= 1; left--) {
            int prefix = 0;
            for (int right = left + 1; right <= n; right++) {
                prefix += weights[left][right];
                cost[left][right] = cost[left + 1][right] + prefix;
            }
        }
        int groups = k + 1;
        previous = new int[width];
        java.util.Arrays.fill(previous, INF);
        int[][] parents = new int[groups + 1][width];
        for (int end = 1; end <= n - groups + 1; end++) {
            previous[end] = cost[1][end];
        }
        for (int group = 2; group <= groups; group++) {
            current = new int[width];
            java.util.Arrays.fill(current, INF);
            parent = parents[group];
            int end = n - groups + group;
            fill(group, end, group - 1, end - 1);
            previous = current;
        }
        int[] cuts = new int[k];
        int end = n;
        for (int group = groups; group > 1; group--) {
            end = parents[group][end];
            cuts[group - 2] = end;
        }
        StringBuilder output = new StringBuilder();
        output.append(cost[1][n] - previous[n]).append('\n');
        for (int i = 0; i < k; i++) {
            if (i > 0) {
                output.append(' ');
            }
            output.append(cuts[i]);
        }
        System.out.println(output);
    }
}
