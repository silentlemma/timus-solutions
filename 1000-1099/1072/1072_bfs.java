import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int OCTET_BITS = 8;

    static int address(String s) {
        int v = 0;
        for (String part : s.split("\\.")) {
            v = v << OCTET_BITS | Integer.parseInt(part);
        }
        return v;
    }

    static boolean linked(int[] a, int[] b) {
        for (int p : a) {
            for (int q : b) {
                if (p == q) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(text.toString());
        int n = Integer.parseInt(tok.nextToken());
        // each interface is reduced to its subnet, IP AND mask; a signed int
        // holds the 32 bits, and only equality matters
        int[][] nets = new int[n][];
        for (int i = 0; i < n; i++) {
            int k = Integer.parseInt(tok.nextToken());
            nets[i] = new int[k];
            for (int j = 0; j < k; j++) {
                int ip = address(tok.nextToken());
                nets[i][j] = ip & address(tok.nextToken());
            }
        }
        int start = Integer.parseInt(tok.nextToken()) - 1;
        int end = Integer.parseInt(tok.nextToken()) - 1;
        int[] from = new int[n];
        Arrays.fill(from, -1);
        from[start] = start;
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v = 0; v < n; v++) {
                if (from[v] < 0 && linked(nets[u], nets[v])) {
                    from[v] = u;
                    queue.add(v);
                }
            }
        }
        if (from[end] < 0) {
            System.out.println("No");
            return;
        }
        List<Integer> path = new ArrayList<>();
        for (int v = end; v != start; v = from[v]) {
            path.add(v);
        }
        path.add(start);
        StringBuilder out = new StringBuilder("Yes\n");
        for (int i = path.size() - 1; i >= 0; i--) {
            out.append(path.get(i) + 1).append(i > 0 ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
