import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // the line has at most 10^5 pieces of each length, fewer than the 9 * 10^5
    // numbers of six digits, so the answer has at most six digits
    static final int DIGITS = 6, LIMIT = 1000000;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String s = in.readLine().trim();
        boolean[] seen = new boolean[LIMIT + 1];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') continue;
            int value = 0;
            for (int j = i; j < n && j < i + DIGITS; j++) {
                value = value * 10 + (s.charAt(j) - '0');
                seen[value] = true;
            }
        }
        int answer = 1;
        while (seen[answer]) answer++;
        System.out.println(answer);
    }
}
