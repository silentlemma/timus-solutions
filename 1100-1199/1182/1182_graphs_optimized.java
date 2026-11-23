import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        int n = in.nextInt();
        boolean[][] knows = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = in.nextInt(); j != 0; j = in.nextInt()) {
                knows[i][j - 1] = true;
            }
        }
        // two people who do not both know each other must be in different
        // teams, so these pairs must form a bipartite graph; each component
        // gives two sides, and one side of each goes to the first team
        int[] side = new int[n];
        Arrays.fill(side, -1);
        List<List<List<Integer>>> parts = new ArrayList<>();
        for (int s = 0; s < n; s++) {
            if (side[s] >= 0) {
                continue;
            }
            side[s] = 0;
            List<List<Integer>> groups = new ArrayList<>();
            groups.add(new ArrayList<>());
            groups.add(new ArrayList<>());
            List<Integer> queue = new ArrayList<>();
            queue.add(s);
            for (int h = 0; h < queue.size(); h++) {
                int v = queue.get(h);
                groups.get(side[v]).add(v);
                for (int u = 0; u < n; u++) {
                    if (u != v && !(knows[v][u] && knows[u][v])) {
                        if (side[u] < 0) {
                            side[u] = 1 - side[v];
                            queue.add(u);
                        } else if (side[u] == side[v]) {
                            System.out.println("No solution");
                            return;
                        }
                    }
                }
            }
            parts.add(groups);
        }
        int count = parts.size();
        // reach[k][size]: which side of part k-1 gives the first team that
        // size, or -1 when it cannot be reached
        int[][] reach = new int[count + 1][n + 1];
        for (int[] row : reach) {
            Arrays.fill(row, -1);
        }
        reach[0][0] = 0;
        for (int k = 0; k < count; k++) {
            for (int size = 0; size <= n; size++) {
                if (reach[k][size] < 0) {
                    continue;
                }
                for (int pick = 0; pick < 2; pick++) {
                    int next = size + parts.get(k).get(pick).size();
                    if (reach[k + 1][next] < 0) {
                        reach[k + 1][next] = pick;
                    }
                }
            }
        }
        int size = -1;
        for (int s = 0; s <= n; s++) {
            boolean closer = size < 0 || Math.abs(2 * s - n) < Math.abs(2 * size - n);
            if (reach[count][s] >= 0 && closer) {
                size = s;
            }
        }
        List<List<Integer>> team = new ArrayList<>();
        team.add(new ArrayList<>());
        team.add(new ArrayList<>());
        for (int k = count - 1; k >= 0; k--) {
            int pick = reach[k + 1][size];
            team.get(0).addAll(parts.get(k).get(pick));
            team.get(1).addAll(parts.get(k).get(1 - pick));
            size -= parts.get(k).get(pick).size();
        }
        StringBuilder out = new StringBuilder();
        for (List<Integer> t : team) {
            out.append(t.size());
            for (int v : t) {
                out.append(' ').append(v + 1);
            }
            out.append('\n');
        }
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
