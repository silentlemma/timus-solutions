import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int m = (int)in.nval;
        List<long[]> list = new ArrayList<>();
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int left = (int)in.nval;
            in.nextToken();
            int right = (int)in.nval;
            if (left == 0 && right == 0)
                break;
            list.add(new long[] {left, right});
        }
        long[][] segments = list.toArray(new long[0][]);
        Arrays.sort(segments,
                    (a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        List<long[]> chosen = new ArrayList<>();
        long covered = 0;
        int i = 0;
        while (covered < m) {
            // among the segments that start inside the covered part, take the
            // one that reaches furthest; it is never worse than any other
            long[] best = null;
            for (; i < segments.length && segments[i][0] <= covered; i++) {
                if (best == null || segments[i][1] > best[1])
                    best = segments[i];
            }
            if (best == null || best[1] <= covered) {
                System.out.println("No solution");
                return;
            }
            chosen.add(best);
            covered = best[1];
        }
        StringBuilder out = new StringBuilder();
        out.append(chosen.size()).append('\n');
        for (long[] s : chosen)
            out.append(s[0]).append(' ').append(s[1]).append('\n');
        System.out.print(out);
    }
}
