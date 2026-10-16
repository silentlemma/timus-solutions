import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static DataInputStream in = new DataInputStream(new java.io.BufferedInputStream(System.in));

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int value = 0;
        while (c >= '0') {
            value = value * 10 + c - '0';
            c = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // each range packed as low * 2^21 + (2^21 - 1 - high), so that the
        // natural order is low up, then high down
        long[] pieces = new long[n];
        for (int i = 0; i < n; i++) {
            int a = readInt(), b = readInt();
            pieces[i] = pack(Math.min(a, b), Math.max(a, b));
        }
        Arrays.sort(pieces);
        // a domino is a range [low, high]; standing upright as (low, high)
        // or flipped as (high, low), two of a kind fit together when nested,
        // and one of each when they overlap; the kinds are nested chains
        long[] upright = new long[n], flipped = new long[n];
        int ups = 0, flips = 0;
        for (long p : pieces) {
            if (ups == 0 || high(p) <= high(upright[ups - 1])) {
                upright[ups++] = p;
            } else if (flips == 0 || high(p) <= high(flipped[flips - 1])) {
                flipped[flips++] = p;
            } else {
                System.out.println("NO");
                return;
            }
        }
        // the innermost ranges of the two chains meet in the middle
        if (ups > 0 && flips > 0) {
            long a = upright[ups - 1], b = flipped[flips - 1];
            if (high(a) < low(b) || high(b) < low(a)) {
                System.out.println("NO");
                return;
            }
        }
        StringBuilder out = new StringBuilder("YES\n");
        for (int i = 0; i < ups; i++) {
            out.append(low(upright[i])).append(' ').append(high(upright[i])).append('\n');
        }
        for (int i = flips - 1; i >= 0; i--) {
            out.append(high(flipped[i])).append(' ').append(low(flipped[i])).append('\n');
        }
        System.out.print(out);
    }

    static final int SHIFT = 21;
    static final long MASK = (1L << SHIFT) - 1;

    static long pack(int low, int high) {
        return ((long) low << SHIFT) | (MASK - high);
    }

    static int low(long p) {
        return (int) (p >> SHIFT);
    }

    static int high(long p) {
        return (int) (MASK - (p & MASK));
    }
}
