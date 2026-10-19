import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final long EDGE = 1000000000L;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int k = (int) in.nval;
        long[][] candles = new long[n][2];
        for (long[] c : candles) {
            in.nextToken();
            c[0] = (long) in.nval;
            in.nextToken();
            c[1] = (long) in.nval;
        }
        Arrays.sort(candles, (a, b) -> a[0] != b[0]
            ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        // take the first k candles from the left, ties broken from below: all
        // columns left of candle k, and its own column up to it; the cut from it
        // to (x - 1, EDGE) leaves the rest of its column outside
        long x = candles[k - 1][0];
        long y = candles[k - 1][1];
        List<long[]> polygon = new ArrayList<>();
        polygon.add(new long[] {-EDGE, -EDGE});
        polygon.add(new long[] {x, -EDGE});
        polygon.add(new long[] {x, y});
        if (x - 1 > -EDGE) {
            polygon.add(new long[] {x - 1, EDGE});
        }
        polygon.add(new long[] {-EDGE, EDGE});
        StringBuilder out = new StringBuilder();
        out.append(polygon.size()).append('\n');
        for (long[] p : polygon) {
            out.append(p[0]).append(' ').append(p[1]).append('\n');
        }
        System.out.print(out);
    }
}
