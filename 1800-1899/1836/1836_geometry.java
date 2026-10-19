import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int CORNERS = 4;
    static final double TETRAHEDRON = 6; // a corner with legs a, b, c cuts off abc/6

    static String volume(long side, long[] h) {
        // the surface is a plane, so the levels at opposite corners add up
        // to the same sum; a sensor reads max(0, level), and 0 hides it
        int dry = 0, at = -1;
        long[] diagonal = new long[2];
        boolean[] hidden = new boolean[2];
        long total = 0;
        for (int i = 0; i < CORNERS; i++) {
            diagonal[i % 2] += h[i];
            total += h[i];
            if (h[i] == 0) {
                dry++;
                at = i;
                hidden[i % 2] = true;
            }
        }
        double area = (double) side * side;
        if (dry == CORNERS) {
            return "0.000000";
        }
        if (dry == 0) {
            if (diagonal[0] != diagonal[1]) {
                return "error";
            }
            return String.format("%.6f", area * total / CORNERS);
        }
        if (dry == 1) {
            long left = h[(at + 1) % CORNERS], far = h[(at + 2) % CORNERS];
            long right = h[(at + CORNERS - 1) % CORNERS], x = left + right - far;
            if (x > 0) {
                return "error";
            }
            // the plane dips below the bottom at the dry corner in a
            // tetrahedron with legs -x up and -x/(left - x), -x/(right - x)
            // along the edges, so that much negative water is added back
            double dip = -(double) x;
            double level = (double) (total + x) / CORNERS
                    + dip * dip * dip / (TETRAHEDRON * (left - x) * (double) (right - x));
            return String.format("%.6f", area * level);
        }
        // two or more hidden levels: they only have to be at most 0 and keep
        // the two diagonal sums equal, and when that is possible they can move
        if (hidden[0] && hidden[1]) {
            return "ambiguous";
        }
        int low = hidden[0] ? 0 : 1;
        return diagonal[1 - low] > diagonal[low] ? "error" : "ambiguous";
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int t = (int) in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            long side = (long) in.nval;
            long[] h = new long[CORNERS];
            for (int j = 0; j < CORNERS; j++) {
                in.nextToken();
                h[j] = (long) in.nval;
            }
            out.append(volume(side, h)).append('\n');
        }
        System.out.print(out);
    }
}
