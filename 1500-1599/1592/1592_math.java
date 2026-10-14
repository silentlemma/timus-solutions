import java.io.*;
import java.util.*;

public class Main {
    static final long MINUTE = 60;
    static final long HOUR = 60 * MINUTE;
    static final long CYCLE = 12 * HOUR; // the dial shows the same after 12 hours
    static final int TWELVE = 12;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String first = in.readLine();
        if (first == null)
            return;
        int n = Integer.parseInt(first.trim());
        long[] times = new long[n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            String[] parts = in.readLine().trim().split(":");
            int h = Integer.parseInt(parts[0]);
            times[i] = h % TWELVE * HOUR + Integer.parseInt(parts[1]) * MINUTE +
                       Integer.parseInt(parts[2]); // 12 o'clock is 0
            total += times[i];
        }
        Arrays.sort(times);
        // winding clock i forward to t costs t - time_i, plus a full cycle when
        // the clock shows a later time than t; moving t back to the nearest
        // clock time only helps, so only the clock times are tried
        long best = 0, bestCost = -1;
        int j = 0; // clocks showing at most t
        for (long t : times) {
            while (j < n && times[j] <= t)
                j++;
            long cost = n * t - total + CYCLE * (n - j);
            if (bestCost < 0 || cost < bestCost) {
                best = t;
                bestCost = cost;
            }
        }
        long h = best / HOUR, rest = best % HOUR;
        System.out.printf("%d:%02d:%02d%n", h == 0 ? TWELVE : h, rest / MINUTE, rest % MINUTE);
    }
}
