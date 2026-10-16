import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int CORNERS = 3;

    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    static long[] vec(long[] a, long[] b) {
        return new long[] {b[0] - a[0], b[1] - a[1]};
    }

    static long turn(long[] u, long[] w) {
        return u[0] * w[1] - u[1] * w[0];
    }

    static long dot(long[] u, long[] w) {
        return u[0] * w[0] + u[1] * w[1];
    }

    // whether the ray w lies in the closed sector turning left from u to v
    static boolean within(long[] u, long[] v, long[] w) {
        long c = turn(u, v);
        if (c > 0) {
            return turn(u, w) >= 0 && turn(w, v) >= 0;
        }
        if (c < 0) {
            return !(turn(v, w) > 0 && turn(w, u) > 0);
        }
        return turn(u, w) >= 0;
    }

    // rays from the bend b towards x and y stay on one side of the ravine
    static boolean sameSideAtBend(long[] a, long[] b, long[] c, long[] x, long[] y) {
        long[] u = vec(b, a), v = vec(b, c), p = vec(b, x), q = vec(b, y);
        if (turn(u, v) == 0 && dot(u, v) > 0) {
            return true; // b is a free tip
        }
        return (within(u, v, p) && within(u, v, q)) || (within(v, u, p) && within(v, u, q));
    }

    static boolean strictlyInside(long[] p, long[] a, long[] b) {
        return cross(a, b, p) == 0 && dot(vec(p, a), vec(p, b)) < 0;
    }

    static boolean crosses(long[] p, long[] q, long[] a, long[] b) {
        return cross(p, q, a) * cross(p, q, b) < 0 && cross(a, b, p) * cross(a, b, q) < 0;
    }

    static boolean allowed(List<long[]> path, long[] a, long[] b, long[] c) {
        for (int i = 0; i + 1 < path.size(); i++) {
            long[] p = path.get(i), q = path.get(i + 1);
            if (crosses(p, q, a, b) || crosses(p, q, b, c)) {
                return false;
            }
            // going straight through the bend must not change sides there
            if (strictlyInside(b, p, q) && !sameSideAtBend(a, b, c, p, q)) {
                return false;
            }
        }
        for (int i = 1; i + 1 < path.size(); i++) {
            long[] x = path.get(i - 1), v = path.get(i), y = path.get(i + 1);
            if (v == b && !sameSideAtBend(a, b, c, x, y)) {
                return false;
            }
            // an end of the ravine lying inside the other piece is no corner
            if (v == a && strictlyInside(a, b, c) && cross(b, c, x) * cross(b, c, y) < 0) {
                return false;
            }
            if (v == c && strictlyInside(c, a, b) && cross(a, b, x) * cross(a, b, y) < 0) {
                return false;
            }
        }
        return true;
    }

    // every order of every subset of the corners
    static void orders(List<Integer> left, List<Integer> chosen, List<List<Integer>> out) {
        out.add(new ArrayList<>(chosen));
        for (int i = 0; i < left.size(); i++) {
            List<Integer> rest = new ArrayList<>(left);
            int k = rest.remove(i);
            chosen.add(k);
            orders(rest, chosen, out);
            chosen.remove(chosen.size() - 1);
        }
    }

    static DataInputStream in = new DataInputStream(new java.io.BufferedInputStream(System.in));

    static long readLong() throws IOException {
        int c = in.read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = in.read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = in.read();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = in.read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        List<Integer> all = new ArrayList<>();
        for (int k = 0; k < CORNERS; k++) {
            all.add(k);
        }
        List<List<Integer>> routes = new ArrayList<>();
        orders(all, new ArrayList<>(), routes);
        int tests = (int) readLong();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < tests; t++) {
            long[] s = {readLong(), readLong()}, e = {readLong(), readLong()};
            long[] a = {readLong(), readLong()}, b = {readLong(), readLong()};
            long[] c = {readLong(), readLong()};
            long[][] corner = {a, b, c};
            // a shortest way bends only at points of the ravine, at most once
            // at each of A, B and C; the shortest allowed candidate wins
            double best = Double.POSITIVE_INFINITY;
            for (List<Integer> route : routes) {
                List<long[]> path = new ArrayList<>();
                path.add(s);
                for (int k : route) {
                    path.add(corner[k]);
                }
                path.add(e);
                double size = 0;
                for (int i = 0; i + 1 < path.size(); i++) {
                    size += Math.hypot(path.get(i + 1)[0] - path.get(i)[0],
                            path.get(i + 1)[1] - path.get(i)[1]);
                }
                if (size < best && allowed(path, a, b, c)) {
                    best = size;
                }
            }
            out.append(String.format("%.6f", best)).append('\n');
        }
        System.out.print(out);
    }
}
