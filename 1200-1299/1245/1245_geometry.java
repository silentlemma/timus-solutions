import java.io.*;
import java.util.*;

public class Main {
    static final int SIDE = 100;
    static final int LO = 0, HI = 1, LO2 = 2, HI2 = 3;

    // a box is {lo, hi, lo2, hi2}: its span on the split axis, then the other
    static int[] grow(int[] a, int[] b) {
        return new int[] {Math.min(a[LO], b[LO]), Math.max(a[HI], b[HI]), Math.min(a[LO2], b[LO2]),
                          Math.max(a[HI2], b[HI2])};
    }

    // area of the smallest picture holding the box, at least 100 by 100
    static long area(int[] b) {
        return (long)Math.max(b[HI] - b[LO], SIDE) * Math.max(b[HI2] - b[LO2], SIDE);
    }

    // sorted by their low edge on the split axis, a prefix and the rest can
    // hang apart exactly when the prefix ends no later than the rest begins
    static long best(int[][] spots) {
        Arrays.sort(spots, (a, b) -> Integer.compare(a[LO], b[LO]));
        int n = spots.length;
        int[][] suffix = new int[n][];
        suffix[n - 1] = spots[n - 1];
        for (int i = n - 2; i >= 0; i--)
            suffix[i] = grow(spots[i], suffix[i + 1]);
        long result = area(suffix[0]);
        int[] prefix = spots[0];
        for (int k = 1; k < n; k++) {
            if (prefix[HI] <= spots[k][LO])
                result = Math.min(result, area(prefix) + area(suffix[k]));
            prefix = grow(prefix, spots[k]);
        }
        return result;
    }

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next(in);
        // a picture must hold each spot whole, so it must hold its bounding square
        int[][] across = new int[n][], down = new int[n][];
        for (int i = 0; i < n; i++) {
            int r = next(in), x = next(in), y = next(in);
            across[i] = new int[] {x - r, x + r, y - r, y + r};
            down[i] = new int[] {y - r, y + r, x - r, x + r};
        }
        // two pictures that do not overlap are split by a vertical or a
        // horizontal line, and each can grow to 100 mm away from that line
        System.out.println(Math.min(best(across), best(down)));
    }
}
