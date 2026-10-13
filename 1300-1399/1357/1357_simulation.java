import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final long SPECIFIC_HEAT = 4190; // J/(kg K)
    static final long PORTION_GRAMS = 200;
    static final long COLD = 20, BOILING = 100; // degrees
    static final long POWER = 400;              // W

    // heating one portion takes C m dT / P seconds; with m in grams this is
    // exactly the number of milliseconds, 167 600
    static final long PORTION_MS = SPECIFIC_HEAT * PORTION_GRAMS * (BOILING - COLD) / POWER;
    static final int CAPACITY = 5; // portions in a full teakettle
    static final long MS = 1000;
    static final long MINUTE = 60, HOUR = MINUTE * MINUTE, DAY = 24 * HOUR;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine())
            all.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = in.hasMoreTokens() ? Integer.parseInt(in.nextToken()) : 0;
        long[] wake = new long[n];
        long[] ready = new long[n];
        for (int i = 0; i < n; i++) {
            String[] p = in.nextToken().split(":");
            wake[i] = (Long.parseLong(p[0]) * HOUR + Long.parseLong(p[1]) * MINUTE +
                       Long.parseLong(p[2])) *
                      MS;
        }
        List<Integer> kettle = new ArrayList<>();
        ArrayDeque<Integer> waiting = new ArrayDeque<>();
        long boil = 0; // the moment the water in the kettle boils, in milliseconds
        int i = 0;
        while (i < n || !kettle.isEmpty()) {
            // water that boils exactly when someone wakes up is poured out first
            if (!kettle.isEmpty() && (i == n || wake[i] >= boil)) {
                for (int j : kettle)
                    ready[j] = boil;
                kettle.clear();
                while (!waiting.isEmpty() && kettle.size() < CAPACITY)
                    kettle.add(waiting.poll());
                boil += PORTION_MS * kettle.size();
                continue;
            }
            if (kettle.isEmpty()) {
                kettle.add(i);
                boil = wake[i] + PORTION_MS;
            } else if (kettle.size() < CAPACITY) {
                // the heat still missing grows by one portion's worth
                kettle.add(i);
                boil += PORTION_MS;
            } else {
                waiting.add(i);
            }
            i++;
        }
        StringBuilder out = new StringBuilder();
        for (long t : ready) {
            long sec = (t + MS - 1) / MS % DAY; // rounded up, past midnight from 00:00:00
            out.append(
                   String.format("%02d:%02d:%02d", sec / HOUR, sec / MINUTE % MINUTE, sec % MINUTE))
                .append('\n');
        }
        System.out.print(out);
    }
}
