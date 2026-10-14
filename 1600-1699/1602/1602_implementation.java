import java.util.*;

public class Main {
    static final long HUNDRED = 100;        // times are kept in hundredths of a second, exactly
    static final long STAND = 15 * HUNDRED; // the lift stands this long on the first floor
    static final long BOARD = 5 * HUNDRED;  // getting into the lift
    static final int DIGITS = 2;

    // a number with at most two decimals, as an exact integer of hundredths
    static long hundredths(String word) {
        int dot = word.indexOf('.');
        String whole = dot < 0 ? word : word.substring(0, dot);
        String frac = dot < 0 ? "" : word.substring(dot + 1);
        frac = (frac + "00").substring(0, DIGITS);
        return Long.parseLong(whole) * HUNDRED + Long.parseLong(frac);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long n = in.nextLong(), k = in.nextLong();
        long u = hundredths(in.next()), v = hundredths(in.next());
        // walking all the way down needs no lift
        long bestFloor = 1, bestTime = (n - 1) * u;
        long ready = (k - 1) * v + STAND; // the lift may leave the first floor from then on
        for (long f = 2; f <= n; f++) {
            // Petya calls the lift on reaching floor f; it comes up, waits for
            // the boarding and goes down again
            long start = Math.max(ready, (n - f) * u);
            long total = start + (f - 1) * v + BOARD + (f - 1) * v;
            // a later floor means less walking, so ties go to it
            if (total <= bestTime) {
                bestFloor = f;
                bestTime = total;
            }
        }
        System.out.println(bestFloor);
    }
}
