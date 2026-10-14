import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        // coordinates up to 10^9 are exact in the tokenizer's doubles
        int n = (int)in.nval;
        long[] xs = new long[n], ys = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = (long)in.nval;
            in.nextToken();
            ys[i] = (long)in.nval;
        }
        in.nextToken();
        int m = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int j = 0; j < m; j++) {
            in.nextToken();
            long px = (long)in.nval;
            in.nextToken();
            long py = (long)in.nval;
            int turns = 0;
            boolean onEdge = false;
            for (int i = 0; i < n && !onEdge; i++) {
                long ax = xs[i], ay = ys[i], bx = xs[(i + 1) % n], by = ys[(i + 1) % n];
                // each product is below 4 10^18, so the difference fits in 64 bits
                long cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax);
                if (cross == 0 && Math.min(ax, bx) <= px && px <= Math.max(ax, bx) &&
                    Math.min(ay, by) <= py && py <= Math.max(ay, by)) {
                    onEdge = true;
                } else if (ay <= py && py < by) {
                    // upwards past the point on its left: one more turn
                    if (cross > 0)
                        turns++;
                } else if (by <= py && py < ay) {
                    // downwards past the point on its right: one turn less
                    if (cross < 0)
                        turns--;
                }
            }
            out.append(onEdge ? "EDGE" : String.valueOf(turns)).append('\n');
        }
        System.out.print(out);
    }
}
