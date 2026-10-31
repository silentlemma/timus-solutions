import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    private static long solve(long[][] cost, int[] plants) {
        int n = cost.length;
        long[] best = new long[n];
        Arrays.fill(best, Long.MAX_VALUE);
        boolean[] used = new boolean[n];
        for (int v : plants)
            best[v] = 0;
        long answer = 0;
        for (int step = 0; step < n; step++) {
            int vertex = -1;
            for (int v = 0; v < n; v++)
                if (!used[v] && (vertex < 0 || best[v] < best[vertex]))
                    vertex = v;
            answer += best[vertex];
            used[vertex] = true;
            for (int v = 0; v < n; v++)
                if (!used[v] && cost[vertex][v] < best[v])
                    best[v] = cost[vertex][v];
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        int[] plants = new int[k];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            plants[i] = (int)in.nval - 1;
        }
        long[][] cost = new long[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                in.nextToken();
                cost[i][j] = (long)in.nval;
            }
        System.out.println(solve(cost, plants));
    }
}
