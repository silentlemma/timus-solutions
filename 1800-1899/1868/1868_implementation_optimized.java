import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static final String[] MEDALS = {"gold", "silver", "bronze"};
    static final int PER_MEDAL = 4;
    static final int PRIZE = 5;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Map<String, String> medal = new HashMap<>();
        // each name and forecast occupies its own line; retain only medallists.
        for (String kind : MEDALS)
            for (int i = 0; i < PER_MEDAL; i++)
                medal.put(in.readLine().trim(), kind);
        int n = Integer.parseInt(in.readLine().trim()), best = -1, winners = 0;
        for (int p = 0; p < n; p++) {
            int k = Integer.parseInt(in.readLine().trim()), right = 0;
            for (int i = 0; i < k; i++) {
                StringTokenizer words = new StringTokenizer(in.readLine());
                String team = words.nextToken();
                words.nextToken();
                if (words.nextToken().equals(medal.get(team)))
                    right++;
            }
            if (right > best) {
                best = right;
                winners = 1;
            } else if (right == best)
                winners++;
        }
        System.out.println(PRIZE * winners);
    }
}
