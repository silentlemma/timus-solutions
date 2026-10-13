import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[][] routes = new int[n][];
        List<List<Integer>> onStop = new ArrayList<>();
        for (int i = 0; i <= m; i++)
            onStop.add(new ArrayList<>());
        for (int r = 0; r < n; r++) {
            in.nextToken();
            routes[r] = new int[(int)in.nval];
            for (int i = 0; i < routes[r].length; i++) {
                in.nextToken();
                routes[r][i] = (int)in.nval;
                onStop.get(routes[r][i]).add(r);
            }
        }
        in.nextToken();
        int a = (int)in.nval;
        in.nextToken();
        int b = (int)in.nval;
        // one ride along a route reaches any of its stops, both ways; layers of rides
        int[] rides = new int[m + 1], cameBy = new int[m + 1], boarded = new int[n],
              queue = new int[m + 1];
        Arrays.fill(rides, -1);
        Arrays.fill(boarded, -1);
        rides[a] = 0;
        int tail = 0;
        queue[tail++] = a;
        for (int head = 0; head < tail && rides[b] < 0; head++) {
            int st = queue[head];
            for (int r : onStop.get(st)) {
                if (boarded[r] >= 0)
                    continue;
                boarded[r] = st; // the stop where the route was first taken
                for (int next : routes[r])
                    if (rides[next] < 0) {
                        rides[next] = rides[st] + 1;
                        cameBy[next] = r;
                        queue[tail++] = next;
                    }
            }
        }
        if (rides[b] < 0) {
            System.out.println(-1);
            return;
        }
        List<Integer> path = new ArrayList<>();
        path.add(b);
        while (path.get(path.size() - 1) != a)
            path.add(boarded[cameBy[path.get(path.size() - 1)]]);
        StringBuilder out = new StringBuilder();
        out.append(rides[b]).append('\n');
        for (int i = path.size() - 1; i >= 0; i--)
            out.append(path.get(i)).append(i > 0 ? ' ' : '\n');
        System.out.print(out);
    }
}
