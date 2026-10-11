import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
        String s = line == null ? "" : line.trim();
        int n = s.length(), bestStart = 0, bestLen = 0;
        // every letter and every gap between two letters is a centre, 2n - 1 in all, and
        // each is expanded as far as it goes; ties keep the leftmost start
        for (int centre = 0; centre < 2 * n - 1; centre++) {
            int lo = centre / 2, hi = (centre + 1) / 2;
            while (lo >= 0 && hi < n && s.charAt(lo) == s.charAt(hi)) {
                lo--;
                hi++;
            }
            int length = hi - lo - 1, start = lo + 1;
            if (length > bestLen || (length == bestLen && start < bestStart)) {
                bestStart = start;
                bestLen = length;
            }
        }
        System.out.println(s.substring(bestStart, bestStart + bestLen));
    }
}
