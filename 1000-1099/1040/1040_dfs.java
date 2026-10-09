import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static List<List<int[]>> adj = new ArrayList<>();
    static int[] number;
    static boolean[] visited;
    static int counter = 0;

    // numbers the flights in the order the search meets them; the first flight
    // met at a new airport right after its entry flight k gets k + 1
    static void dfs(int v) {
        visited[v] = true;
        for (int[] f : adj.get(v)) {
            if (number[f[1]] == 0) {
                number[f[1]] = ++counter;
                if (!visited[f[0]]) {
                    dfs(f[0]);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        for (int v = 0; v <= n; v++) {
            adj.add(new ArrayList<>());
        }
        number = new int[m];
        visited = new boolean[n + 1];
        for (int e = 0; e < m; e++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            adj.get(a).add(new int[] {b, e});
            adj.get(b).add(new int[] {a, e});
        }
        dfs(1);
        StringBuilder out = new StringBuilder("YES\n");
        for (int e = 0; e < m; e++) {
            out.append(number[e]).append(e + 1 < m ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
