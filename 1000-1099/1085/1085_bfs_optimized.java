import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int TICKET = 4;
    private static final int WORD_BITS = Long.SIZE;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static void charge(long layer, long possible, int offset, int fare, int[] total) {
        for (long mask = layer & possible; mask != 0; mask &= mask - 1) {
            total[offset + Long.numberOfTrailingZeros(mask)] += fare;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int stops = number(input), routes = number(input);
        long[] low = new long[stops], high = new long[stops];
        for (int i = 0; i < routes; i++) {
            long a = 0, b = 0;
            for (int size = number(input); size > 0; size--) {
                int stop = number(input) - 1;
                if (stop < WORD_BITS) {
                    a |= 1L << stop;
                } else {
                    b |= 1L << (stop - WORD_BITS);
                }
            }
            for (long mask = a; mask != 0; mask &= mask - 1) {
                int stop = Long.numberOfTrailingZeros(mask);
                low[stop] |= a;
                high[stop] |= b;
            }
            for (long mask = b; mask != 0; mask &= mask - 1) {
                int stop = WORD_BITS + Long.numberOfTrailingZeros(mask);
                low[stop] |= a;
                high[stop] |= b;
            }
        }

        boolean[] occupied = new boolean[stops];
        int[] paying = new int[stops], budget = new int[stops], total = new int[stops];
        Arrays.fill(budget, stops);
        for (int friends = number(input); friends > 0; friends--) {
            int money = number(input), start = number(input) - 1;
            occupied[start] = true;
            if (number(input) == 0) {
                paying[start]++;
                budget[start] = Math.min(budget[start], money / TICKET);
            }
        }

        long possibleLow = stops >= WORD_BITS ? -1L : (1L << stops) - 1;
        long possibleHigh = stops > WORD_BITS ? (1L << (stops - WORD_BITS)) - 1 : 0;
        for (int start = 0; start < stops; start++) {
            if (!occupied[start]) {
                continue;
            }
            long a = start < WORD_BITS ? 1L << start : 0;
            long b = start >= WORD_BITS ? 1L << (start - WORD_BITS) : 0;
            long reachedLow = a, reachedHigh = b;
            // One breadth-first search serves everyone starting at this stop.
            for (int rides = 0; (a | b) != 0; rides++) {
                int fare = rides * TICKET * paying[start];
                if (fare != 0) {
                    charge(a, possibleLow, 0, fare, total);
                    charge(b, possibleHigh, WORD_BITS, fare, total);
                }
                long missing = (possibleLow & ~reachedLow) | (possibleHigh & ~reachedHigh);
                if (rides == budget[start] || missing == 0) {
                    break;
                }
                long nextLow = 0, nextHigh = 0;
                for (; a != 0; a &= a - 1) {
                    int stop = Long.numberOfTrailingZeros(a);
                    nextLow |= low[stop];
                    nextHigh |= high[stop];
                }
                for (; b != 0; b &= b - 1) {
                    int stop = WORD_BITS + Long.numberOfTrailingZeros(b);
                    nextLow |= low[stop];
                    nextHigh |= high[stop];
                }
                a = nextLow & ~reachedLow;
                b = nextHigh & ~reachedHigh;
                reachedLow |= a;
                reachedHigh |= b;
            }
            possibleLow &= reachedLow;
            possibleHigh &= reachedHigh;
            if ((possibleLow | possibleHigh) == 0) {
                System.out.println(0);
                return;
            }
        }
        int best = -1;
        for (int i = 0; i < stops; i++) {
            boolean possible = i < WORD_BITS ? (possibleLow & (1L << i)) != 0
                                             : (possibleHigh & (1L << (i - WORD_BITS))) != 0;
            if (possible && (best < 0 || total[i] < total[best])) {
                best = i;
            }
        }
        System.out.println(best < 0 ? "0" : (best + 1) + " " + total[best]);
    }
}
