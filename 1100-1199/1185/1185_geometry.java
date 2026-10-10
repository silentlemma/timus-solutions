import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        int gap = Integer.parseInt(in.nextToken());
        long[][] pts = new long[n][];
        for (int i = 0; i < n; i++) {
            pts[i] = new long[] {Long.parseLong(in.nextToken()), Long.parseLong(in.nextToken())};
        }
        Arrays.sort(pts,
                    (p, q) -> p[0] != q[0] ? Long.compare(p[0], q[0]) : Long.compare(p[1], q[1]));
        // the shortest wall is the convex hull pushed out by L: its straight
        // parts add up to the hull perimeter, and its arcs turn once around
        // a full circle of radius L in total
        List<long[]> hull = new ArrayList<>();
        for (int pass = 0; pass < 2; pass++) {
            List<long[]> part = new ArrayList<>();
            for (int k = 0; k < n; k++) {
                long[] p = pts[pass == 0 ? k : n - 1 - k];
                while (part.size() >= 2 &&
                       cross(part.get(part.size() - 2), part.get(part.size() - 1), p) <= 0) {
                    part.remove(part.size() - 1);
                }
                part.add(p);
            }
            hull.addAll(part.subList(0, part.size() - 1));
        }
        double length = 2 * Math.PI * gap;
        for (int k = 0; k < hull.size(); k++) {
            long[] a = hull.get(k), b = hull.get((k + 1) % hull.size());
            length += Math.hypot(a[0] - b[0], a[1] - b[1]);
        }
        System.out.println(Math.round(length));
    }
}
