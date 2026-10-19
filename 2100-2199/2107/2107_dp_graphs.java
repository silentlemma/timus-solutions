import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    private static boolean complete(int n, int k, int[] next) {
        int[] indegree = new int[n + 1];
        for (int vertex = 1; vertex <= n; vertex++) {
            if (next[vertex] != 0 && ++indegree[next[vertex]] > 1) {
                return false;
            }
        }

        boolean[] visited = new boolean[n + 1];
        List<List<int[]>> buckets = new ArrayList<>();
        for (int length = 0; length <= n; length++) {
            buckets.add(new ArrayList<>());
        }
        for (int start = 1; start <= n; start++) {
            if (indegree[start] != 0) {
                continue;
            }
            int[] path = new int[n];
            int length = 0;
            for (int vertex = start; vertex != 0; vertex = next[vertex]) {
                visited[vertex] = true;
                path[length++] = vertex;
            }
            buckets.get(length).add(Arrays.copyOf(path, length));
        }
        for (int start = 1; start <= n; start++) {
            if (visited[start]) {
                continue;
            }
            int length = 0;
            for (int vertex = start; !visited[vertex]; vertex = next[vertex]) {
                visited[vertex] = true;
                length++;
            }
            if (k % length != 0) {
                return false;
            }
        }

        List<Integer> lengths = new ArrayList<>();
        List<Integer> radices = new ArrayList<>();
        int states = 1;
        for (int length = 1; length <= n; length++) {
            int count = buckets.get(length).size();
            if (count != 0) {
                lengths.add(length);
                radices.add(count + 1);
                states *= count + 1;
            }
        }

        // A mixed-radix state records how many paths of every length are used.
        int[][] digits = new int[states][lengths.size()];
        List<Integer> groups = new ArrayList<>();
        for (int state = 0; state < states; state++) {
            int value = state;
            int weight = 0;
            for (int kind = 0; kind < lengths.size(); kind++) {
                digits[state][kind] = value % radices.get(kind);
                value /= radices.get(kind);
                weight += digits[state][kind] * lengths.get(kind);
            }
            if (weight != 0 && k % weight == 0) {
                groups.add(state);
            }
        }

        boolean[] possible = new boolean[states];
        int[] choice = new int[states];
        possible[0] = true;
        for (int state = 1; state < states; state++) {
            int anchor = lengths.size() - 1;
            while (digits[state][anchor] == 0) {
                anchor--;
            }
            for (int group : groups) {
                if (group > state) {
                    break;
                }
                if (digits[group][anchor] == 0 || !possible[state - group]) {
                    continue;
                }
                boolean fits = true;
                for (int kind = 0; kind < lengths.size(); kind++) {
                    if (digits[group][kind] > digits[state][kind]) {
                        fits = false;
                        break;
                    }
                }
                if (fits) {
                    possible[state] = true;
                    choice[state] = group;
                    break;
                }
            }
        }
        if (!possible[states - 1]) {
            return false;
        }

        for (int state = states - 1; state != 0;) {
            int group = choice[state];
            List<int[]> paths = new ArrayList<>();
            for (int kind = 0; kind < lengths.size(); kind++) {
                List<int[]> bucket = buckets.get(lengths.get(kind));
                for (int count = 0; count < digits[group][kind]; count++) {
                    paths.add(bucket.remove(bucket.size() - 1));
                }
            }
            for (int index = 0; index < paths.size(); index++) {
                int[] path = paths.get(index);
                next[path[path.length - 1]] = paths.get((index + 1) % paths.size())[0];
            }
            state -= group;
        }
        return true;
    }

    private static int readInt(BufferedInputStream input) throws IOException {
        int value = 0;
        int symbol;
        do {
            symbol = input.read();
        } while (symbol != -1 && Character.isWhitespace(symbol));
        while (symbol >= '0' && symbol <= '9') {
            value = value * 10 + symbol - '0';
            symbol = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = readInt(input);
        int k = readInt(input);
        int[] next = new int[n + 1];
        for (int vertex = 1; vertex <= n; vertex++) {
            next[vertex] = readInt(input);
        }
        if (!complete(n, k, next)) {
            System.out.println("No");
            return;
        }
        StringBuilder output = new StringBuilder("Yes\n");
        for (int vertex = 1; vertex <= n; vertex++) {
            if (vertex != 1) {
                output.append(' ');
            }
            output.append(next[vertex]);
        }
        output.append('\n');
        System.out.print(output);
    }
}
