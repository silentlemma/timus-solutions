import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static List<List<Integer>> adj = new ArrayList<>();
    static int[] dist, prev;

    // distances from s and the predecessors on the shortest paths
    static void bfs(int s) {
        int n = adj.size();
        dist = new int[n];
        prev = new int[n];
        Arrays.fill(dist, -1);
        int[] queue = new int[n];
        int head = 0, tail = 0;
        queue[tail++] = s;
        dist[s] = 0;
        while (head < tail) {
            int v = queue[head++];
            for (int w : adj.get(v)) {
                if (dist[w] < 0) {
                    dist[w] = dist[v] + 1;
                    prev[w] = v;
                    queue[tail++] = w;
                }
            }
        }
    }

    static int farthest() {
        int best = 1;
        for (int v = 1; v < dist.length; v++) {
            if (dist[v] > dist[best]) {
                best = v;
            }
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        for (int v = 0; v <= n; v++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 2; i <= n; i++) {
            in.nextToken();
            int p = (int)in.nval;
            adj.get(i).add(p);
            adj.get(p).add(i);
        }
        // the farthest computer from any start is an end of a longest path; the
        // farthest one from it is the other end
        bfs(1);
        int u = farthest();
        bfs(u);
        int v = farthest();
        // the centers are the middle one or two computers of that path
        int length = dist[v];
        int first = 0, second = 0;
        for (int k = 0, x = v; k <= length; k++, x = prev[x]) {
            if (k == length / 2) {
                first = x;
            }
            if (k == (length + 1) / 2) {
                second = x;
            }
        }
        if (first == second) {
            System.out.println(first);
        } else {
            System.out.println(Math.min(first, second) + " " + Math.max(first, second));
        }
    }
}
