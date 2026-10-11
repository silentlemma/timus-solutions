import java.io.*;
import java.util.*;

public class Main {
    static final int FORGET = 1001; // a grave untouched for 1000 days can go on the next day
    static final int NOTICE = 101;  // and only when no neighbour was visited in the last 100

    static int cells;
    static int[] touched, nearVisit, release;
    static PriorityQueue<Integer> pending = new PriorityQueue<>();

    // a pending release is day * cells + grave
    static void schedule(int g) {
        release[g] = Math.max(touched[g] + FORGET, nearVisit[g] + NOTICE);
        pending.add(release[g] * cells + g);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        cells = n * m;
        // the client in each grave (0 if free), the last burial or visit of
        // that client, the last visit next door and the day it may be freed
        int[] owner = new int[cells];
        touched = new int[cells];
        nearVisit = new int[cells];
        release = new int[cells];
        Arrays.fill(nearVisit, -NOTICE);
        int[] graveOf = new int[1]; // grave of each client, -1 if none
        int clients = 0;
        PriorityQueue<Integer> free = new PriorityQueue<>();
        for (int g = 0; g < cells; g++)
            free.add(g);
        int cremated = 0;
        for (String line; (line = in.readLine()) != null;) {
            st = new StringTokenizer(line);
            if (!st.hasMoreTokens())
                continue;
            int day = Integer.parseInt(st.nextToken());
            String kind = st.nextToken();
            // graves free at the start of the day, before its events
            while (!pending.isEmpty() && pending.peek() / cells <= day) {
                int top = pending.poll(), g = top % cells;
                if (owner[g] != 0 && release[g] == top / cells) {
                    graveOf[owner[g] - 1] = -1;
                    owner[g] = 0;
                    free.add(g);
                }
            }
            if (kind.equals("d")) {
                if (clients == graveOf.length)
                    graveOf = Arrays.copyOf(graveOf, 2 * clients);
                graveOf[clients++] = -1;
                if (free.isEmpty()) {
                    cremated++;
                    continue;
                }
                int g = free.poll();
                owner[g] = clients;
                graveOf[clients - 1] = g;
                touched[g] = day;
                schedule(g);
                continue;
            }
            int g = graveOf[Integer.parseInt(st.nextToken()) - 1];
            if (g < 0)
                continue;
            touched[g] = day;
            schedule(g);
            int r = g / m, c = g % m;
            for (int nr = r - 1; nr <= r + 1; nr++)
                for (int nc = c - 1; nc <= c + 1; nc++)
                    if ((nr != r || nc != c) && nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        int k = nr * m + nc;
                        nearVisit[k] = day;
                        if (owner[k] != 0)
                            schedule(k);
                    }
        }
        System.out.println(cremated);
    }
}
