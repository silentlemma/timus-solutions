import java.util.Arrays;
import java.util.Scanner;

public class Main {
    // a cost is pegs * PEG + inches cut: fewer pegs first, then less cutting
    static final long PEG = 1000000, NONE = -1;

    // a shelf is its height, left end, length and the two peg positions
    static final int Y = 0, LEFT = 1, LENGTH = 2, A = 3, B = 4, FIELDS = 5;

    // cheapest way to get a shelf out of the open strip (lo, hi) of the
    // tome, keeping its plank inside the niche [0, width]
    static long clear(long[] s, long lo, long hi, long width) {
        if (s[LEFT] + s[LENGTH] <= lo || s[LEFT] >= hi) {
            return 0;
        }
        long best = 2 * PEG + s[LENGTH];
        for (long[] side : new long[][] {{0, lo}, {hi, width}}) {
            long start = side[0], end = side[1];
            // pegs stay: a plank of length t in [start, end] over both pegs
            // with its middle between them exists for b - a <= t <= this bound
            if (start <= s[A] && s[B] <= end) {
                long longest = Math.min(Math.min(s[LENGTH], 2 * (s[B] - start)),
                                        Math.min(end - start, 2 * (end - s[A])));
                if (longest >= s[B] - s[A]) {
                    best = Math.min(best, s[LENGTH] - longest);
                }
            }
            // one peg moves anywhere, so only the kept peg and the room matter
            boolean kept = (start <= s[A] && s[A] <= end) || (start <= s[B] && s[B] <= end);
            if (end > start && kept) {
                best = Math.min(best, PEG + Math.max(0, s[LENGTH] - (end - start)));
            }
        }
        return best;
    }

    // cost of making a shelf hold the tome over [x, x + tome], or NONE
    static long carry(long[] s, long x, long tome, long width) {
        if (s[LENGTH] < tome) {
            return NONE;
        }
        // pegs stay: limits on the new left end, doubled to stay in integers
        long low = Math.max(Math.max(0, 2 * (s[B] - s[LENGTH])),
                            Math.max(2 * s[A] - s[LENGTH], 2 * (x + tome - s[LENGTH])));
        long high = Math.min(Math.min(2 * s[A], 2 * x),
                             Math.min(2 * s[B] - s[LENGTH], 2 * (width - s[LENGTH])));
        if (low <= high) {
            return 0;
        }
        // one peg moves: the plank only has to reach over the tome and the
        // peg that stays
        for (long p : new long[] {s[A], s[B]}) {
            if (Math.max(x + tome, p) - Math.min(x, p) <= s[LENGTH]) {
                return PEG;
            }
        }
        return NONE;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long width = in.nextLong(), height = in.nextLong();
        long tomeW = in.nextLong(), tomeH = in.nextLong();
        int n = in.nextInt();
        long[][] shelves = new long[n][FIELDS];
        for (long[] s : shelves) {
            s[Y] = in.nextLong();
            s[LEFT] = in.nextLong();
            s[LENGTH] = in.nextLong();
            s[A] = s[LEFT] + in.nextLong();
            s[B] = s[LEFT] + in.nextLong();
        }
        Arrays.sort(shelves, (p, q) -> Long.compare(p[Y], q[Y]));
        int spots = (int)(width - tomeW + 1);
        // prefix[k][x]: total cost of clearing the strip at x from the k
        // lowest shelves
        long[][] prefix = new long[n + 1][spots];
        for (int k = 0; k < n; k++) {
            for (int x = 0; x < spots; x++) {
                prefix[k + 1][x] = prefix[k][x] + clear(shelves[k], x, x + tomeW, width);
            }
        }
        long best = NONE;
        for (int i = 0; i < n; i++) {
            long y = shelves[i][Y];
            if (y + tomeH > height) {
                continue;
            }
            // the shelves strictly between the tome bottom and top are in
            // the way
            int top = i + 1;
            while (top < n && shelves[top][Y] < y + tomeH) {
                top++;
            }
            for (int x = 0; x < spots; x++) {
                long base = carry(shelves[i], x, tomeW, width);
                if (base != NONE) {
                    long total = base + prefix[top][x] - prefix[i + 1][x];
                    if (best == NONE || total < best) {
                        best = total;
                    }
                }
            }
        }
        System.out.println(best / PEG + " " + best % PEG);
    }
}
