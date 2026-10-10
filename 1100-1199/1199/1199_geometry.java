import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final double SAFE = 0.1;
    static final double INF = 1e300;
    static final double SAME = 1e-9;

    static class Polygon {
        double[][] v, d; // corners and the edge vectors leaving them
        double cx, cy, r;
    }

    // Looks for a point of the edges closer to (px, py) than best[0] says, and
    // then best holds the squared distance, the edge index and the position
    // along the edge.
    static boolean pointEdges(double px, double py, Polygon poly, double[] best) {
        boolean found = false;
        for (int i = 0; i < poly.v.length; i++) {
            double wx = px - poly.v[i][0], wy = py - poly.v[i][1];
            double dx = poly.d[i][0], dy = poly.d[i][1], d2 = dx * dx + dy * dy;
            double t = wx * dx + wy * dy, q;
            if (t <= 0) {
                q = wx * wx + wy * wy;
                t = 0;
            } else if (t >= d2) {
                q = (wx - dx) * (wx - dx) + (wy - dy) * (wy - dy);
                t = 1;
            } else {
                double c = wx * dy - wy * dx;
                q = c * c / d2;
                t /= d2;
            }
            if (q < best[0]) {
                best[0] = q;
                best[1] = i;
                best[2] = t;
                found = true;
            }
        }
        return found;
    }

    // Squared distance between two polygons; onA and onB receive where it
    // is reached on each, as {edge index, position along the edge}.
    static double polyPoly(Polygon a, Polygon b, double[] onA, double[] onB) {
        double[] best = {INF, 0, 0};
        for (int side = 0; side < 2; side++) {
            Polygon own = side == 1 ? b : a, other = side == 1 ? a : b;
            for (int k = 0; k < own.v.length; k++) {
                if (pointEdges(own.v[k][0], own.v[k][1], other, best)) {
                    double[] here = {k, 0}, there = {best[1], best[2]};
                    System.arraycopy(side == 1 ? there : here, 0, onA, 0, 2);
                    System.arraycopy(side == 1 ? here : there, 0, onB, 0, 2);
                }
            }
        }
        return best[0];
    }

    static double[] at(Polygon poly, double[] p) {
        int e = (int)p[0];
        return new double[] {poly.v[e][0] + poly.d[e][0] * p[1],
                             poly.v[e][1] + poly.d[e][1] * p[1]};
    }

    // Corners passed going along the boundary from src to dst, in the
    // direction with fewer of them.
    static void walk(Polygon poly, double[] src, double[] dst, List<double[]> path) {
        int k = poly.v.length, i = (int)src[0], j = (int)dst[0];
        int fwd = ((j - i) % k + k) % k, back = ((i - j) % k + k) % k;
        if (fwd == 0 && dst[1] < src[1]) {
            fwd = k;
        }
        if (back == 0 && dst[1] > src[1]) {
            back = k;
        }
        if (fwd <= back) {
            for (int s = 0; s < fwd; s++) {
                path.add(poly.v[(i + 1 + s) % k]);
            }
        } else {
            for (int s = 0; s < back; s++) {
                path.add(poly.v[((i - s) % k + k) % k]);
            }
        }
    }

    static double[] toward(double[] f, double[] p, double len) {
        double d = Math.hypot(p[0] - f[0], p[1] - f[1]);
        return new double[] {f[0] + (p[0] - f[0]) * len / d, f[1] + (p[1] - f[1]) * len / d};
    }

    static StringTokenizer tok;
    static BufferedReader in;

    static String next() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        double[] mouse = {Double.parseDouble(next()), Double.parseDouble(next())};
        double[] cheese = {Double.parseDouble(next()), Double.parseDouble(next())};
        int n = Integer.parseInt(next());
        Polygon[] polys = new Polygon[n];
        for (int i = 0; i < n; i++) {
            Polygon poly = polys[i] = new Polygon();
            int k = Integer.parseInt(next());
            poly.v = new double[k][];
            for (int j = 0; j < k; j++) {
                poly.v[j] = new double[] {Double.parseDouble(next()), Double.parseDouble(next())};
                poly.cx += poly.v[j][0] / k;
                poly.cy += poly.v[j][1] / k;
            }
            // the corners may come in any order, so sort them around the centre
            final double cx = poly.cx, cy = poly.cy;
            Arrays.sort(poly.v,
                        (p, q)
                            -> Double.compare(Math.atan2(p[1] - cy, p[0] - cx),
                                              Math.atan2(q[1] - cy, q[0] - cx)));
            poly.d = new double[k][];
            for (int j = 0; j < k; j++) {
                double[] nxt = poly.v[(j + 1) % k];
                poly.d[j] = new double[] {nxt[0] - poly.v[j][0], nxt[1] - poly.v[j][1]};
                poly.r = Math.max(poly.r, Math.hypot(poly.v[j][0] - cx, poly.v[j][1] - cy));
            }
        }

        // nodes 0..n-1 are the safe zones around the furniture, n the mouse
        // and n + 1 the cheese; an edge costs the dangerous length between them
        int start = n, goal = n + 1;
        double[] dist = new double[n + 2];
        int[] parent = new int[n + 2];
        boolean[] done = new boolean[n + 2];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        while (true) {
            int u = -1;
            for (int v = 0; v < n + 2; v++) {
                if (!done[v] && (u < 0 || dist[v] < dist[u])) {
                    u = v;
                }
            }
            if (u == goal) {
                break;
            }
            done[u] = true;
            for (int v = 0; v < n + 2; v++) {
                if (done[v]) {
                    continue;
                }
                double w;
                if (v == goal && u == start) {
                    w = Math.hypot(mouse[0] - cheese[0], mouse[1] - cheese[1]);
                } else if (v == goal || u == start) {
                    double[] p = v == goal ? cheese : mouse, best = {INF, 0, 0};
                    pointEdges(p[0], p[1], polys[v == goal ? u : v], best);
                    w = Math.max(0, Math.sqrt(best[0]) - SAFE);
                } else {
                    Polygon a = polys[u], b = polys[v];
                    double gap = Math.hypot(a.cx - b.cx, a.cy - b.cy) - a.r - b.r - 2 * SAFE;
                    if (dist[u] + gap >= dist[v]) {
                        continue;
                    }
                    w = Math.sqrt(polyPoly(a, b, new double[2], new double[2])) - 2 * SAFE;
                }
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    parent[v] = u;
                }
            }
        }
        List<Integer> route = new ArrayList<>();
        route.add(goal);
        while (route.get(route.size() - 1) != start) {
            route.add(parent[route.get(route.size() - 1)]);
        }
        Collections.reverse(route);

        List<double[]> path = new ArrayList<>();
        path.add(mouse);
        if (route.size() == 2) {
            path.add(cheese);
        } else {
            // step from the mouse onto the nearest point of the first piece
            Polygon first = polys[route.get(1)];
            double[] best = {INF, 0, 0};
            pointEdges(mouse[0], mouse[1], first, best);
            double[] here = {best[1], best[2]};
            double[] foot = at(first, here);
            if (Math.sqrt(best[0]) > SAFE) {
                path.add(toward(foot, mouse, SAFE));
            }
            path.add(foot);
            for (int i = 1; i + 2 < route.size(); i++) {
                Polygon a = polys[route.get(i)], b = polys[route.get(i + 1)];
                double[] outPos = new double[2], inPos = new double[2];
                polyPoly(a, b, outPos, inPos);
                double[] fa = at(a, outPos), fb = at(b, inPos);
                walk(a, here, outPos, path);
                path.add(fa);
                path.add(toward(fa, fb, SAFE));
                path.add(toward(fb, fa, SAFE));
                path.add(fb);
                here = inPos;
            }
            Polygon last = polys[route.get(route.size() - 2)];
            best = new double[] {INF, 0, 0};
            pointEdges(cheese[0], cheese[1], last, best);
            double[] end = {best[1], best[2]};
            foot = at(last, end);
            walk(last, here, end, path);
            path.add(foot);
            if (Math.sqrt(best[0]) > SAFE) {
                path.add(toward(foot, cheese, SAFE));
            }
            path.add(cheese);
        }

        List<double[]> out = new ArrayList<>();
        out.add(path.get(0));
        for (double[] p : path) {
            double[] prev = out.get(out.size() - 1);
            if (Math.hypot(p[0] - prev[0], p[1] - prev[1]) > SAME) {
                out.add(p);
            }
        }
        if (out.size() == 1) {
            out.add(path.get(path.size() - 1));
        }
        StringBuilder sb = new StringBuilder();
        sb.append(out.size()).append('\n');
        for (double[] p : out) {
            sb.append(String.format(Locale.US, "%.9f %.9f\n", p[0], p[1]));
        }
        System.out.print(sb);
    }
}
