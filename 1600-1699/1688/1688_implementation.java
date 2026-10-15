import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long SHARES = 3; // a bill is split three ways

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(all.toString());
        long n = Long.parseLong(words.nextToken());
        int m = Integer.parseInt(words.nextToken());
        long total = 0;
        for (int i = 1; i <= m; i++) {
            total += Long.parseLong(words.nextToken());
            // Vanya's share total / 3 exceeds n exactly when total > 3n
            if (total > SHARES * n) {
                System.out.println("Free after " + i + " times.");
                return;
            }
        }
        System.out.println("Team.GOV!");
    }
}
