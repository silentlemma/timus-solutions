import java.io.*;
import java.util.*;

public class Main {
    static final int ENOUGH = 9; // any 9 points, no three on a line, hold a convex pentagon
    static final int SIDES = 5;

    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    // the convex hull of points {x, y, id}, counterclockwise
    static List<long[]> hull(List<long[]> points) {
        points.sort((p, q) -> p[0] != q[0] ? Long.compare(p[0], q[0]) : Long.compare(p[1], q[1]));
        List<long[]> h = new ArrayList<>();
        for (int pass = 0; pass < 2; pass++) {
            int start = h.size();
            for (long[] p : points) {
                while (h.size() >= start + 2 &&
                       cross(h.get(h.size() - 2), h.get(h.size() - 1), p) <= 0)
                    h.remove(h.size() - 1);
                h.add(p);
            }
            h.remove(h.size() - 1);
            Collections.reverse(points);
        }
        return h;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int)st.nval;
        // by the Erdos-Szekeres theorem the first nine points are enough
        int m = Math.min(n, ENOUGH);
        long[][] points = new long[m][];
        for (int i = 0; i < m; i++) {
            st.nextToken();
            long x = (long)st.nval;
            st.nextToken();
            points[i] = new long[] {x, (long)st.nval, i + 1};
        }
        for (int mask = 0; mask < 1 << m; mask++) {
            if (Integer.bitCount(mask) != SIDES)
                continue;
            List<long[]> five = new ArrayList<>();
            for (int i = 0; i < m; i++)
                if ((mask >> i & 1) == 1)
                    five.add(points[i]);
            List<long[]> h = hull(five);
            if (h.size() == SIDES) {
                StringBuilder out = new StringBuilder("Yes\n");
                for (int i = 0; i < SIDES; i++)
                    out.append(i > 0 ? " " : "").append(h.get(i)[2]);
                System.out.println(out);
                return;
            }
        }
        System.out.println("No");
    }
}
