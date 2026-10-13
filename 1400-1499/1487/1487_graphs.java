import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int WORD_BITS = 64;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        List<List<Integer>> winners = new ArrayList<>();
        int[] indegree = new int[n];
        for (int i = 0; i < n; i++) {
            String row = in.readLine().trim();
            List<Integer> beaten = new ArrayList<>();
            for (int j = 0; j < n; j++)
                if (row.charAt(j) == '1') {
                    beaten.add(j);
                    indegree[j]++;
                }
            winners.add(beaten);
        }
        // stronger[v]: every team that is stronger than v, as a bit set; the
        // results are transitive, so the wins form an acyclic graph
        int words = (n + WORD_BITS - 1) / WORD_BITS;
        long[][] stronger = new long[n][words];
        int[] queue = new int[n];
        int tail = 0;
        for (int v = 0; v < n; v++)
            if (indegree[v] == 0)
                queue[tail++] = v;
        for (int h = 0; h < tail; h++) {
            int v = queue[h];
            for (int u : winners.get(v)) {
                for (int w = 0; w < words; w++)
                    stronger[u][w] |= stronger[v][w];
                stronger[u][v / WORD_BITS] |= 1L << (v % WORD_BITS);
                if (--indegree[u] == 0)
                    queue[tail++] = u;
            }
        }
        // A plays better than B when no team stronger than B is stronger than A
        int q = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < q; k++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            boolean common = false;
            for (int w = 0; w < words && !common; w++)
                common = (stronger[a][w] & stronger[b][w]) != 0;
            out.append(common ? "No" : "YES").append('\n');
        }
        System.out.print(out);
    }
}
