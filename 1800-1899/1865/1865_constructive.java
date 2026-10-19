import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // drop repeated points and points in the middle of a straight run
    static List<long[]> straighten(List<long[]> points) {
        List<long[]> out = new ArrayList<>();
        for (long[] p : points) {
            int size = out.size();
            if (size > 0 && out.get(size - 1)[0] == p[0] && out.get(size - 1)[1] == p[1]) {
                continue;
            }
            while (out.size() >= 2) {
                long[] a = out.get(out.size() - 2);
                long[] b = out.get(out.size() - 1);
                boolean sameX = a[0] == b[0] && b[0] == p[0];
                boolean sameY = a[1] == b[1] && b[1] == p[1];
                if (!sameX && !sameY) {
                    break;
                }
                out.remove(out.size() - 1);
            }
            out.add(p);
        }
        return out;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        long w = Long.parseLong(st.nextToken());
        long h = Long.parseLong(st.nextToken());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());
        long d = Long.parseLong(st.nextToken());
        long half = w * h / 2;
        // Finland always holds the column of cells along its coast, the
        // lighthouse, and a corridor of cells from the lighthouse to that column
        long right = w - 1 - x - d;
        if (h + d * d + right > half) {
            System.out.println("Impossible");
            return;
        }
        List<long[]> points = new ArrayList<>();
        if (h + d * (w - 1 - x) <= half) {
            // every row of Finland runs from some column to the coast; the area
            // still missing pushes rows west from the top down
            long extra = half - (h + d * (w - 1 - x));
            List<long[]> cuts = new ArrayList<>();
            long[][] bands = {{h, y + d, w - 1}, {y + d, y, x}, {y, 0, w - 1}};
            for (long[] band : bands) {
                long rows = band[0] - band[1];
                long column = band[2];
                if (rows == 0) {
                    continue;
                }
                long full = column > 1 ? Math.min(rows, extra / (column - 1)) : 0;
                extra -= full * (column - 1);
                if (full > 0) {
                    cuts.add(new long[] {full, 1});
                }
                if (full < rows) {
                    long part = Math.min(extra, column - 1);
                    extra -= part;
                    cuts.add(new long[] {1, column - part});
                    if (full + 1 < rows) {
                        cuts.add(new long[] {rows - full - 1, column});
                    }
                }
            }
            long level = h;
            points.add(new long[] {cuts.get(0)[1], h});
            for (long[] c : cuts) {
                points.add(new long[] {c[1], level});
                points.add(new long[] {c[1], level - c[0]});
                level -= c[0];
            }
        } else {
            // the border goes round the lighthouse: Finland takes full corridor
            // rows at the top of the lighthouse rows and part of one more row
            long rest = half - (h + d * d + right);
            long more = rest / right;
            long part = rest % right;
            long level = y + d - 1 - more;
            long[][] around = {{w - 1, h}, {w - 1, y + d}, {x, y + d}, {x, y}, {x + d, y},
                {x + d, level}, {w - 1 - part, level}, {w - 1 - part, level - 1},
                {w - 1, level - 1}, {w - 1, 0}};
            for (long[] p : around) {
                points.add(p);
            }
        }
        points = straighten(points);
        StringBuilder out = new StringBuilder();
        out.append(points.size()).append('\n');
        for (long[] p : points) {
            out.append(p[0]).append(' ').append(p[1]).append('\n');
        }
        System.out.print(out);
    }
}
