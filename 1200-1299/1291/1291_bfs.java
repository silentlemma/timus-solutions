import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static StreamTokenizer in =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) throws IOException {
        int n = next();
        int[] teeth = new int[n + 1];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());
        for (int i = 1; i <= n; i++) {
            teeth[i] = next();
            for (int j = next(); j != 0; j = next()) {
                // a link may be listed at one end only, so store it both ways
                adj.get(i).add(j);
                adj.get(j).add(i);
            }
        }
        int root = next(), speed = next();
        // meshed gears share the speed of their rims, speed * teeth, and turn
        // opposite ways; so gear j turns at +-speed * teeth[root] / teeth[j]
        int rim = speed * teeth[root];
        int[] sign = new int[n + 1];
        int[] queue = new int[n];
        int tail = 0;
        sign[root] = 1;
        queue[tail++] = root;
        for (int head = 0; head < tail; head++) {
            int u = queue[head];
            for (int v : adj.get(u)) {
                if (sign[v] == 0) {
                    sign[v] = -sign[u];
                    queue[tail++] = v;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            if (sign[i] == 0) {
                out.append("0/1\n");
            } else {
                int g = gcd(rim, teeth[i]);
                out.append(sign[i] * rim / g).append('/').append(teeth[i] / g).append('\n');
            }
        }
        System.out.print(out);
    }
}
