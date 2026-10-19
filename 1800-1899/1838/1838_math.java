import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        long length = (long) in.nval;
        in.nextToken();
        int n = (int) in.nval;
        long[] s = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            s[i] = (long) in.nval;
        }
        // a cut at x between supports s[i] and s[i + 1] leaves both parts
        // standing when the left centre x/2 lies in [s[0], s[i]] and the
        // right centre (x + length)/2 lies in [s[i + 1], s[n - 1]]
        long loAll = 2 * s[0], hiAll = 2 * s[n - 1] - length, safe = 0;
        for (int i = 0; i + 1 < n; i++) {
            long lo = Math.max(s[i], Math.max(loAll, 2 * s[i + 1] - length));
            long hi = Math.min(s[i + 1], Math.min(hiAll, 2 * s[i]));
            safe += Math.max(0, hi - lo);
        }
        System.out.println(length - safe);
    }
}
