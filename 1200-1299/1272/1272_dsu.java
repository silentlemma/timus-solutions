import java.io.*;

public class Main {
    static int[] parent;

    static int find(int x) {
        while (parent[x] != x)
            x = parent[x] = parent[parent[x]];
        return x;
    }

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next(in), k = next(in);
        next(in); // the bridges themselves do not matter
        parent = new int[n + 1];
        for (int i = 0; i <= n; i++)
            parent[i] = i;
        // tunnels are free; every bridge joins two of the remaining groups
        int groups = n;
        for (int i = 0; i < k; i++) {
            int a = find(next(in)), b = find(next(in));
            if (a != b) {
                parent[a] = b;
                groups--;
            }
        }
        System.out.println(groups - 1);
    }
}
