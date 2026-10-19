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
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        Map<String, String> medal = new HashMap<>();
        for (String kind : MEDALS) {
            for (int i = 0; i < PER_MEDAL; i++) {
                medal.put(words.nextToken(), kind);
            }
        }
        int n = Integer.parseInt(words.nextToken());
        int[] scores = new int[n];
        int best = 0;
        for (int p = 0; p < n; p++) {
            int k = Integer.parseInt(words.nextToken());
            for (int i = 0; i < k; i++) {
                String team = words.nextToken();
                words.nextToken();
                String kind = words.nextToken();
                if (kind.equals(medal.get(team))) {
                    scores[p]++;
                }
            }
            best = Math.max(best, scores[p]);
        }
        int winners = 0;
        for (int s : scores) {
            if (s == best) {
                winners++;
            }
        }
        System.out.println(PRIZE * winners);
    }
}
