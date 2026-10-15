import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int ALPHABET = 26;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        int n = Integer.parseInt(words.nextToken());
        String word = words.nextToken();
        int size = word.length();
        // placing the remaining letter whose next occurrence is farthest moves at
        // least k places when k letters remain, so a universal word needs
        // n + (n - 1) + ... + 1 letters
        if (size < n * (n + 1) / 2) {
            System.out.println("NO");
            return;
        }
        short fail = (short) (size + 1);
        // after[c][p]: the place just after the first c at or after place p
        short[][] after = new short[ALPHABET][size + 2];
        for (int c = 0; c < ALPHABET; c++) {
            after[c][size] = fail;
            after[c][size + 1] = fail;
            for (int p = size - 1; p >= 0; p--) {
                after[c][p] = word.charAt(p) - 'a' == c ? (short) (p + 1) : after[c][p + 1];
            }
        }
        // reach[mask]: how far the greedy embedding gets for the worst order of
        // the letters in mask; submasks come first in increasing order, and one
        // failing mask makes the whole set fail, so the table stops there
        short[] reach = new short[1];
        int filled = 1;
        for (int mask = 1; mask < (1 << n); mask++) {
            short best = 0;
            for (int rest = mask; rest != 0; rest &= rest - 1) {
                int letter = Integer.numberOfTrailingZeros(rest);
                short pos = after[letter][reach[mask ^ (1 << letter)]];
                if (pos > best) {
                    best = pos;
                }
            }
            if (best == fail) {
                System.out.println("NO");
                return;
            }
            if (filled == reach.length) {
                reach = Arrays.copyOf(reach, 2 * filled);
            }
            reach[filled++] = best;
        }
        System.out.println("YES");
    }
}
