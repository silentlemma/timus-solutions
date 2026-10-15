import java.util.*;

public class Main {
    static final int CORNERS = 3;
    static final int GLIDE = 3; // a glide reflection takes three reflections
    static final int NONE = -1;
    static final int[][] ORDERS = {
        {0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}
    };

    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    static long dist2(long[] p, long[] q) {
        long dx = p[0] - q[0], dy = p[1] - q[1];
        return dx * dx + dy * dy;
    }

    // the line a x + b y = c of points as far from p as from q
    static long[] bisector(long[] p, long[] q) {
        long[] origin = {0, 0};
        long c = dist2(q, origin) - dist2(p, origin);
        return new long[] {2 * (q[0] - p[0]), 2 * (q[1] - p[1]), c};
    }

    static boolean sameLine(long[] u, long[] v) {
        return u[0] * v[1] == u[1] * v[0] && u[0] * v[2] == u[2] * v[0]
            && u[1] * v[2] == u[2] * v[1];
    }

    // reflections taking cur[i] to to[i], or NONE when no isometry does
    static int moves(long[][] cur, long[][] to) {
        for (int i = 0; i < CORNERS; i++)
            for (int j = i + 1; j < CORNERS; j++)
                if (dist2(cur[i], cur[j]) != dist2(to[i], to[j]))
                    return NONE;
        boolean same = true;
        for (int i = 0; i < CORNERS; i++)
            same &= Arrays.equals(cur[i], to[i]);
        if (same)
            return 0;
        if ((cross(cur[0], cur[1], cur[2]) > 0) == (cross(to[0], to[1], to[2]) > 0))
            return 2; // a rotation or a translation: two reflections
        // orientation reversed: one reflection if a single mirror fits all three
        long[] mirror = null;
        for (int i = 0; i < CORNERS; i++) {
            if (Arrays.equals(cur[i], to[i]))
                continue;
            long[] line = bisector(cur[i], to[i]);
            if (mirror == null)
                mirror = line;
            else if (!sameLine(mirror, line))
                return GLIDE;
        }
        for (int i = 0; i < CORNERS; i++)
            if (Arrays.equals(cur[i], to[i])
                && mirror[0] * cur[i][0] + mirror[1] * cur[i][1] != mirror[2])
                return GLIDE;
        return 1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long[][] target = new long[CORNERS][], cur = new long[CORNERS][];
        for (int i = 0; i < CORNERS; i++)
            target[i] = new long[] {in.nextLong(), in.nextLong()};
        for (int i = 0; i < CORNERS; i++)
            cur[i] = new long[] {in.nextLong(), in.nextLong()};
        int best = NONE;
        for (int[] order : ORDERS) {
            long[][] to = new long[CORNERS][];
            for (int i = 0; i < CORNERS; i++)
                to[i] = target[order[i]];
            int m = moves(cur, to);
            if (m != NONE && (best == NONE || m < best))
                best = m;
        }
        System.out.println(best == NONE ? "IMPOSSIBLE" : String.valueOf(best));
    }
}
