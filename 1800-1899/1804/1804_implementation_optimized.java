import java.io.*;

public class Main {
    static final int MOST = 30;
    static final int VENUE_FIELD = 3, SCORED_FIELD = 6, CONCEDED_FIELD = 10;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int tests = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int test = 0; test < tests; ++test) {
            String[] words = in.readLine().trim().split("\\s+");
            boolean home = words[VENUE_FIELD].equals("home");
            int x = Integer.parseInt(words[SCORED_FIELD]),
                y = Integer.parseInt(words[CONCEDED_FIELD]);
            int lowest = -1, highest = -1;
            for (int goals = 0; goals <= MOST; ++goals) {
                int total = x + goals, away = home ? goals : x;
                // Compare against zero and thirty goals by the opponents.
                int bestAway = home ? y : 0, worstAway = home ? y : MOST;
                if (lowest < 0 && (total > y || total == y && away >= bestAway))
                    lowest = goals;
                if (total < y + MOST || total == y + MOST && away <= worstAway)
                    highest = goals;
            }
            out.append(lowest).append(' ').append(highest).append('\n');
        }
        System.out.print(out);
    }
}
