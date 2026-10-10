import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final long SQUARE = 8;

    // Whether v is a perfect square, with the floating root corrected exactly.
    static boolean isSquare(long v) {
        long r = (long)Math.sqrt((double)v);
        while (r * r > v) {
            r--;
        }
        while ((r + 1) * (r + 1) <= v) {
            r++;
        }
        return r * r == v;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long k = (long)in.nval;
            // the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
            // perfect square
            out.append(isSquare(SQUARE * (k - 1) + 1) ? '1' : '0');
            out.append(i + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
