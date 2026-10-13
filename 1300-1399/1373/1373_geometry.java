import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Locale;

public class Main {
    static final int STROKE = 4; // numbers per stroke

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long lowX = Long.MAX_VALUE, highX = Long.MIN_VALUE;
        long lowY = Long.MAX_VALUE, highY = Long.MIN_VALUE;
        long[] s = new long[STROKE];
        boolean any = false;
        while (true) {
            int got = 0;
            while (got < STROKE && in.nextToken() != StreamTokenizer.TT_EOF)
                s[got++] = (long)in.nval;
            if (got < STROKE)
                break;
            long ax = s[0], ay = s[1], bx = s[2], by = s[STROKE - 1];
            long dx = bx - ax, dy = by - ay;
            // go (p, q), then turn clockwise and go (q, -p): p + q = dx and
            // q - p = dy give the corner a + ((dx - dy) / 2, (dx + dy) / 2), and
            // doubled coordinates keep the halves whole
            long[] xs = {2 * ax, 2 * bx, 2 * ax + dx - dy};
            long[] ys = {2 * ay, 2 * by, 2 * ay + dx + dy};
            for (long x : xs) {
                lowX = Math.min(lowX, x);
                highX = Math.max(highX, x);
            }
            for (long y : ys) {
                lowY = Math.min(lowY, y);
                highY = Math.max(highY, y);
            }
            any = true;
        }
        if (!any)
            lowX = highX = lowY = highY = 0;
        System.out.println(
            String.format(Locale.US, "%.4f %.4f", (highX - lowX) / 2.0, (highY - lowY) / 2.0));
    }
}
