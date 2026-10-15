import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Locale;

public class Main {
    static final int DIM = 3;
    static final int STEPS = 60; // halvings in each bisection
    static final int SPHERE = 1500; // directions tried for the narrowest width

    static final double TINY = 1e-13; // where the local search stops
    static final double NEAR = 1e-10; // equal widths, relative to the diameter
    static final int ROUNDS = 400; // passes of a local search, which may creep on forever

    // a helper axis closer than this to n gives a poor cross product
    static final double HELPER = 0.9;
    // the golden angle, spreading directions over the sphere
    static final double GOLDEN = 2.399963229728653;

    static double[][] pts;
    static double[] nMin;
    static double[] hinge;
    static double[] a0;
    static double[] b0;
    static double angle;

    static double dot(double[] a, double[] b) {
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    }

    static double[] cross(double[] a, double[] b) {
        return new double[] {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]};
    }

    // s * a + t * b
    static double[] comb(double[] a, double s, double[] b, double t) {
        return new double[] {s * a[0] + t * b[0], s * a[1] + t * b[1], s * a[2] + t * b[2]};
    }

    static double[] unit(double[] a) {
        double norm = Math.sqrt(dot(a, a));
        return new double[] {a[0] / norm, a[1] / norm, a[2] / norm};
    }

    // v turned by angle around the unit vector axis (Rodrigues)
    static double[] turn(double[] v, double[] axis, double angle) {
        double c = Math.cos(angle);
        double s = Math.sin(angle);
        double k = dot(axis, v) * (1 - c);
        double[] w = cross(axis, v);
        return new double[] {v[0] * c + w[0] * s + axis[0] * k, v[1] * c + w[1] * s + axis[1] * k,
            v[2] * c + w[2] * s + axis[2] * k};
    }

    // two unit vectors completing n to a right-handed frame
    static double[][] across(double[] n) {
        double[] helper = Math.abs(n[0]) > HELPER ? new double[] {0, 1, 0} : new double[] {1, 0, 0};
        double[] a = unit(cross(n, helper));
        return new double[][] {a, cross(n, a)};
    }

    static double width(double[] u) {
        double lo = Double.MAX_VALUE;
        double hi = -Double.MAX_VALUE;
        for (double[] p : pts) {
            double s = dot(p, u);
            lo = Math.min(lo, s);
            hi = Math.max(hi, s);
        }
        return hi - lo;
    }

    static double spread(double[][] f) {
        double w0 = width(f[0]);
        double w1 = width(f[1]);
        double w2 = width(f[2]);
        return Math.max(w0, Math.max(w1, w2)) - Math.min(w0, Math.min(w1, w2));
    }

    static void show(double[][] f) {
        StringBuilder out = new StringBuilder();
        for (double[] u : f) {
            out.append(String.format(Locale.US, "%.15f %.15f %.15f\n", u[0], u[1], u[2]));
        }
        System.out.print(out);
    }

    // the frame at (t, phi): the third axis is the turned nMin, the first two
    // the turned a0, b0 rotated by phi
    static double[][] frame(double t, double phi) {
        double[] n = turn(nMin, hinge, angle * t);
        double[] a = turn(a0, hinge, angle * t);
        double[] b = turn(b0, hinge, angle * t);
        double c = Math.cos(phi);
        double s = Math.sin(phi);
        return new double[][] {comb(a, c, b, s), comb(a, -s, b, c), n};
    }

    // phi in [0, pi/2] with equal first two widths: the difference changes
    // sign over a quarter turn, as the axes swap places
    static double balance(double t) {
        double lo = 0;
        double hi = Math.PI / 2;
        double[][] f = frame(t, lo);
        if (width(f[0]) - width(f[1]) > 0) {
            lo = hi;
            hi = 0;
        }
        for (int i = 0; i < STEPS; i++) {
            double mid = (lo + hi) / 2;
            f = frame(t, mid);
            if (width(f[0]) - width(f[1]) > 0) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return (lo + hi) / 2;
    }

    static long[] icross(long[] a, long[] b) {
        return new long[] {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]};
    }

    static boolean zero(long[] a) {
        return a[0] == 0 && a[1] == 0 && a[2] == 0;
    }

    // A nonzero winding encloses equal widths and survives subdivision.
    static class Enclosure {
        double scale;
        double[][] answer;

        Enclosure(double scale) { this.scale = scale; }

        double[][] vertex(double[] q) {
            double w = q[0], x = q[1], y = q[2], z = q[3];
            double[][] f = {{1 - 2 * (y * y + z * z), 2 * (x * y + w * z), 2 * (x * z - w * y)},
                {2 * (x * y - w * z), 1 - 2 * (x * x + z * z), 2 * (y * z + w * x)},
                {2 * (x * z + w * y), 2 * (y * z - w * x), 1 - 2 * (x * x + y * y)}};
            double[] ws = {width(f[0]), width(f[1]), width(f[2])};
            double gap = Math.max(ws[0], Math.max(ws[1], ws[2]))
                         - Math.min(ws[0], Math.min(ws[1], ws[2]));
            if (gap <= NEAR * scale) {
                answer = f;
            }
            return new double[][] {q, {ws[0] - ws[2], ws[1] - ws[2]}};
        }

        double[][] middle(double[][] a, double[][] b) {
            double[] q = new double[4];
            double norm = 0;
            for (int i = 0; i < 4; i++) {
                q[i] = a[0][i] + b[0][i];
                norm += q[i] * q[i];
            }
            norm = Math.sqrt(norm);
            for (int i = 0; i < 4; i++) q[i] /= norm;
            return vertex(q);
        }

        double edge(double[][] a, double[][] b) {
            if (answer != null) return 0;
            double distance = 0;
            for (int i = 0; i < 4; i++) distance += (a[0][i] - b[0][i]) * (a[0][i] - b[0][i]);
            distance = Math.sqrt(distance);
            double[] u = a[1], v = b[1];
            // Each residual changes by at most 4 * diameter * chord length.
            if (Math.max(Math.abs(u[0]), Math.abs(u[1])) > 4 * scale * distance) {
                return Math.atan2(u[0] * v[1] - u[1] * v[0], u[0] * v[0] + u[1] * v[1]);
            }
            double[][] m = middle(a, b);
            return edge(a, m) + edge(m, b);
        }

        double winding(double[][] a, double[][] b, double[][] c) {
            return edge(a, b) + edge(b, c) + edge(c, a);
        }

        double[][] solve() {
            // The boundary cycles the axes, so its winding cannot be zero.
            double[][][] rim = {vertex(new double[] {1, 0, 0, 0}),
                vertex(new double[] {-0.5, 0.5, 0.5, 0.5}),
                vertex(new double[] {-0.5, -0.5, -0.5, -0.5})};
            double r2 = 1 / Math.sqrt(2);
            double[][] center = vertex(new double[] {0, r2, -r2, 0});
            double[][][] triangle = null;
            for (int i = 0; i < DIM; i++) {
                if (Math.abs(winding(center, rim[i], rim[(i + 1) % DIM])) > Math.PI) {
                    triangle = new double[][][] {center, rim[i], rim[(i + 1) % DIM]};
                    break;
                }
            }
            while (answer == null) {
                double[][] a = triangle[0], b = triangle[1], c = triangle[2];
                double[][] ab = middle(a, b), bc = middle(b, c), ca = middle(c, a);
                double[][][][] children = {{a, ab, ca}, {ab, b, bc}, {ca, bc, c}, {ab, bc, ca}};
                for (double[][][] tri : children) {
                    if (Math.abs(winding(tri[0], tri[1], tri[2])) > Math.PI) {
                        triangle = tri;
                        break;
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int count = (int) in.nval;
        long[][] ints = new long[count][DIM];
        pts = new double[count][DIM];
        for (int i = 0; i < count; i++) {
            for (int k = 0; k < DIM; k++) {
                in.nextToken();
                ints[i][k] = (long) in.nval;
                pts[i][k] = in.nval;
            }
        }
        // Accept the initial coordinate frame when its box is already a cube.
        double[][] aligned = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        double[] ws = {width(aligned[0]), width(aligned[1]), width(aligned[2])};
        if (ws[0] == ws[1] && ws[1] == ws[2]) {
            show(aligned);
            return;
        }
        // the shape of the swarm, decided exactly on the integers
        long[][] diffs = new long[count][DIM];
        for (int i = 0; i < count; i++) {
            for (int k = 0; k < DIM; k++) {
                diffs[i][k] = ints[i][k] - ints[0][k];
            }
        }
        long[] first = new long[DIM];
        long[] normal = new long[DIM];
        for (int i = 1; i < count && zero(first); i++) {
            first = diffs[i];
        }
        for (int i = 1; i < count && zero(normal); i++) {
            normal = icross(first, diffs[i]);
        }
        if (zero(normal)) {
            // all on a line of direction d: an axis at angle acos(1/sqrt 3) to
            // the line each, so the three widths are the length over sqrt 3
            double[] d = unit(new double[] {first[0], first[1], first[2]});
            double[][] uv = across(d);
            double r3 = 1 / Math.sqrt(DIM);
            double r2 = 1 / Math.sqrt(2);
            double r6 = 1 / Math.sqrt(2 * DIM);
            show(new double[][] {comb(comb(d, r3, uv[0], r2), 1, uv[1], r6),
                comb(comb(d, r3, uv[0], -r2), 1, uv[1], r6), comb(d, r3, uv[1], -2 * r6)});
            return;
        }
        boolean flat = true;
        for (long[] d : diffs) {
            flat = flat && normal[0] * d[0] + normal[1] * d[1] + normal[2] * d[2] == 0;
        }
        // widest direction: the diameter, where no other width can be larger
        long bestLength = -1;
        double[] nMax = null;
        for (long[] p : ints) {
            for (long[] q : ints) {
                long dx = p[0] - q[0];
                long dy = p[1] - q[1];
                long dz = p[2] - q[2];
                if (dx * dx + dy * dy + dz * dz > bestLength) {
                    bestLength = dx * dx + dy * dy + dz * dz;
                    nMax = new double[] {dx, dy, dz};
                }
            }
        }
        nMax = unit(nMax);
        // narrowest direction: the normal of a flat swarm, else a search
        if (flat) {
            nMin = unit(new double[] {normal[0], normal[1], normal[2]});
        } else {
            double wMin = Double.MAX_VALUE;
            for (int i = 0; i < SPHERE; i++) {
                double z = 1 - (2.0 * i + 1) / (2 * SPHERE);
                double r = Math.sqrt(1 - z * z);
                double[] u = {r * Math.cos(GOLDEN * i), r * Math.sin(GOLDEN * i), z};
                double w = width(u);
                if (w < wMin) {
                    wMin = w;
                    nMin = u;
                }
            }
            double step = 2 * Math.PI / Math.sqrt(SPHERE);
            for (int round = 0; round < ROUNDS && step > TINY; round++) {
                double[][] ab = across(nMin);
                boolean moved = false;
                double[][] axes = {ab[0], ab[1], unit(comb(ab[0], 1, ab[1], 1)),
                    unit(comb(ab[0], 1, ab[1], -1))};
                for (double[] axis : axes) {
                    for (int sign : new int[] {1, -1}) {
                        double[] cand = unit(turn(nMin, axis, sign * step));
                        double w = width(cand);
                        if (w < wMin) {
                            wMin = w;
                            nMin = cand;
                            moved = true;
                        }
                    }
                }
                if (!moved) {
                    step /= 2;
                }
            }
        }
        // frames along the great circle from nMin to nMax
        hinge = cross(nMin, nMax);
        if (dot(hinge, hinge) < TINY) {
            hinge = across(nMin)[0];
        }
        hinge = unit(hinge);
        angle = Math.acos(Math.max(-1, Math.min(1, dot(nMin, nMax))));
        double[][] start = across(nMin);
        a0 = start[0];
        b0 = start[1];
        // Try equalizing the third width; the candidate is checked afterwards.
        double lo = 0;
        double hi = 1;
        for (int i = 0; i < STEPS; i++) {
            double mid = (lo + hi) / 2;
            double[][] f = frame(mid, balance(mid));
            if (width(f[2]) - width(f[0]) < 0) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        double t = (lo + hi) / 2;
        double[][] result = frame(t, balance(t));
        double scale = Math.max(1, width(nMax));
        if (spread(result) > NEAR * scale) result = new Enclosure(scale).solve();
        show(result);
    }
}
