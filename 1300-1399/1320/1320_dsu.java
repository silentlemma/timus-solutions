import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int VERTICES = 1000;
    static int[] parent = new int[VERTICES + 1];

    static int find(int v) {
        while (parent[v] != v) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int[] edges = new int[VERTICES + 1]; // edges of each component, kept at its root
        for (int v = 0; v <= VERTICES; v++)
            parent[v] = v;
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int a = (int)in.nval;
            in.nextToken();
            int ra = find(a), rb = find((int)in.nval);
            if (ra != rb) {
                parent[ra] = rb;
                edges[rb] += edges[ra];
            }
            edges[rb]++;
        }
        int answer = 1;
        for (int v = 1; v <= VERTICES; v++) {
            if (parent[v] == v && edges[v] % 2 != 0)
                answer = 0;
        }
        System.out.println(answer);
    }
}
