import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0')
            c = in.read();
        int x = 0;
        for (; c >= '0'; c = in.read())
            x = x * 10 + c - '0';
        return x;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] degree = new int[n + 1];
        int[] ends = new int[2 * m + 2 * n];
        for (int i = 0; i < 2 * m; i++) {
            ends[i] = readInt();
            degree[ends[i]]++;
        }
        // vertex 0 is a helper joined to every room with an odd number of tunnels
        int size = 2 * m;
        for (int v = 1; v <= n; v++)
            if (degree[v] % 2 == 1) {
                ends[size++] = 0;
                ends[size++] = v;
            }
        int edges = size / 2;
        int[] count = new int[n + 1];
        for (int i = 0; i < size; i++)
            count[ends[i]]++;
        int[][] adj = new int[n + 1][];
        for (int v = 0; v <= n; v++)
            adj[v] = new int[count[v]];
        int[] fill = new int[n + 1];
        for (int e = 0; e < edges; e++) {
            int a = ends[2 * e], b = ends[2 * e + 1];
            adj[a][fill[a]++] = e;
            adj[b][fill[b]++] = e;
        }
        // an Euler circuit, found without recursion
        boolean[] used = new boolean[edges];
        int[] pos = new int[n + 1];
        int[] stack = new int[edges + 1];
        int top = 0;
        stack[top++] = adj[0].length > 0 ? 0 : 1;
        int[] circuit = new int[edges + 1];
        int length = 0;
        while (top > 0) {
            int v = stack[top - 1];
            while (pos[v] < adj[v].length && used[adj[v][pos[v]]])
                pos[v]++;
            if (pos[v] == adj[v].length) {
                circuit[length++] = v;
                top--;
                continue;
            }
            int e = adj[v][pos[v]];
            used[e] = true;
            stack[top++] = ends[2 * e] + ends[2 * e + 1] - v;
        }
        // the helper edges cut the circuit into trails of real tunnels
        List<String> trails = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int v = circuit[i];
            if (v == 0) {
                if (current.length() > 0)
                    trails.add(current.toString());
                current.setLength(0);
            } else {
                if (current.length() > 0)
                    current.append(' ');
                current.append(v);
            }
        }
        if (current.length() > 0)
            trails.add(current.toString());
        StringBuilder out = new StringBuilder();
        out.append(trails.size()).append('\n');
        for (String t : trails)
            out.append(t).append('\n');
        System.out.print(out);
    }
}
