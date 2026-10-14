import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        long r = Long.parseLong(st.nextToken());
        long[] sizes = new long[n];
        st = new StringTokenizer(in.readLine());
        for (int i = 0; i < n; i++) {
            while (!st.hasMoreTokens())
                st = new StringTokenizer(in.readLine());
            sizes[i] = Long.parseLong(st.nextToken());
        }
        // coats whose sizes lie within r of each other need different trips, so
        // the largest number of sizes in a window [x, x + r] is a lower bound
        int trips = 0;
        for (int lo = 0, hi = 0; hi < n; hi++) {
            while (sizes[hi] - sizes[lo] > r)
                lo++;
            trips = Math.max(trips, hi - lo + 1);
        }
        // and it is enough: dealing the sorted coats round, the coat after coat i
        // in a trip is coat i + trips, which lies beyond that window
        StringBuilder out = new StringBuilder();
        out.append(trips).append('\n');
        for (int t = 0; t < trips; t++) {
            out.append((n - t + trips - 1) / trips);
            for (int coat = t + 1; coat <= n; coat += trips)
                out.append(' ').append(coat);
            out.append('\n');
        }
        System.out.print(out);
    }
}
