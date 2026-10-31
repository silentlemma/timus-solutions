import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // times in tenths of a second; starts are 30 seconds apart
    static final int TENTHS_PER_MINUTE = 600, GAP = 300;
    // comparable records avoid the runtime machinery of a lambda comparator.
    static class Finish implements Comparable<Finish> {
        String name;
        int at, run;
        public int compareTo(Finish other) { return Integer.compare(at, other.at); }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        Finish[] racers = new Finish[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer words = new StringTokenizer(in.readLine());
            Finish f = new Finish();
            f.name = words.nextToken();
            StringTokenizer time = new StringTokenizer(words.nextToken(), ":.");
            f.run = Integer.parseInt(time.nextToken()) * TENTHS_PER_MINUTE +
                    Integer.parseInt(time.nextToken()) * 10 + Integer.parseInt(time.nextToken());
            f.at = f.run + i * GAP;
            racers[i] = f;
        }
        Arrays.sort(racers);
        // replay the finishes in order; the board changes on every new best run
        String[] leaders = new String[n];
        int count = 0, best = -1;
        for (Finish f : racers) {
            if (best < 0 || f.run < best) {
                best = f.run;
                leaders[count++] = f.name;
            }
        }
        Arrays.sort(leaders, 0, count);
        StringBuilder out = new StringBuilder().append(count).append('\n');
        for (int i = 0; i < count; i++)
            out.append(leaders[i]).append('\n');
        System.out.print(out);
    }
}
