import java.util.Scanner;

public class Main {
    static final long CENTS = 100, PEAK = 2 * CENTS;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = Math.round(Double.parseDouble(in.next()) * CENTS);
        long b = Math.round(Double.parseDouble(in.next()) * CENTS);
        long k = in.nextLong();
        // everything is in kopecks: x horns earn a * x - 100 * x^2
        long best = -1, bestX = 0, bestY = 0, yPeak = Math.max(b, 0) / PEAK;
        for (long x = 0; x <= k; x++) {
            long room = k - x, gainX = a * x - CENTS * x * x;
            // the hoof profit is concave in y, so the best y is next to its peak
            for (long y : new long[] {Math.min(yPeak, room), Math.min(yPeak + 1, room)}) {
                long total = gainX + b * y - CENTS * y * y;
                if (total > best) {
                    best = total;
                    bestX = x;
                    bestY = y;
                }
            }
        }
        System.out.printf("%d.%02d\n%d %d\n", best / CENTS, best % CENTS, bestX, bestY);
    }
}
