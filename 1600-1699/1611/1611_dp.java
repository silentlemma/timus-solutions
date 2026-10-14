import java.io.*;
import java.util.*;

public class Main {
    static final int STEP = 10; // every tenth person is fined
    static final int INF = 1 << 30;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        String good = in.readLine().trim();
        // cost[i][j] holds the least fines once i conductors and j friends stand
        // in line, and the next person then stands at place i + j + 1
        int[][] cost = new int[n + 1][k + 1];
        for (int[] row : cost)
            Arrays.fill(row, INF);
        cost[0][0] = 0;
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= k; j++) {
                int here = cost[i][j];
                if (here == INF)
                    continue;
                int fined = (i + j + 1) % STEP == 0 ? 1 : 0;
                if (j < k)
                    cost[i][j + 1] = Math.min(cost[i][j + 1], here + fined); // a friend steps in
                if (i < n) {
                    int add = fined == 1 && good.charAt(i) == '1' ? 1 : 0;
                    cost[i + 1][j] = Math.min(cost[i + 1][j], here + add);
                }
            }
        int j = 0;
        for (int t = 1; t <= k; t++)
            if (cost[n][t] < cost[n][j])
                j = t;
        int best = cost[n][j];
        // walk back: a friend was added wherever the cost came from the left
        ArrayList<Integer> places = new ArrayList<>();
        for (int i = n; i > 0 || j > 0;) {
            boolean fined = (i + j) % STEP == 0;
            int add = fined && i > 0 && good.charAt(i - 1) == '1' ? 1 : 0;
            if (i > 0 && cost[i - 1][j] + add == cost[i][j])
                i--;
            else {
                places.add(i + j);
                j--;
            }
        }
        Collections.reverse(places);
        StringBuilder out = new StringBuilder().append(best).append('\n').append(places.size());
        for (int p : places)
            out.append(' ').append(p);
        System.out.println(out);
    }
}
