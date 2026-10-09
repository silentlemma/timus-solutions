import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int MAX_BASE = 36;

    public static void main(String[] args) throws IOException {
        String s = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        int total = 0, top = 1;
        for (int i = 0; i < s.length(); i++) {
            int d = Character.digit(s.charAt(i), MAX_BASE);
            total += d;
            top = Math.max(top, d);
        }
        // base k is 1 modulo k - 1, so the number is congruent to its digit sum
        for (int k = top + 1; k <= MAX_BASE; k++) {
            if (total % (k - 1) == 0) {
                System.out.println(k);
                return;
            }
        }
        System.out.println("No solution.");
    }
}
