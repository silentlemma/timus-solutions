import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final int DIM = 3;
    static final int STEPS = 60; // halvings in each bisection
    static final int SPHERE = 1500; // directions tried for the narrowest width

    static final int GRID = 80; // grid side of the fallback search
    static final int STARTS = 4; // best grid cells it zooms in around
    static final int ZOOMS = 14; // rounds of zooming, each one ZOOM times finer
    static final int ZOOM = 5;

    static final double TINY = 1e-13; // where the local search stops
    static final double NEAR = 1e-10; // equal widths, relative to the diameter
    static final int ROUNDS = 400; // passes of a local search, which may creep on forever

    // a helper axis closer than this to n gives a poor cross product
    static final double HELPER = 0.9;
    // the golden angle, spreading directions over the sphere
    static final double GOLDEN = 2.399963229728653;
    static final double FIRST_TURN = Math.PI / 2 / 2; // the first turn of the polish

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

    static double cost(double[][] f) {
        double w0 = width(f[0]);
        double w1 = width(f[1]);
        double w2 = width(f[2]);
        return (w0 - w1) * (w0 - w1) + (w1 - w2) * (w1 - w2) + (w2 - w0) * (w2 - w0);
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
                    for (int sign = -1; sign <= 1; sign += 2) {
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
        // at nMin the third width is the smallest, at nMax the largest
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
        if (spread(result) > NEAR * scale) {
            // the chosen balance jumped. A solution still lies in the (t, phi)
            // square, as the third width is the smallest along t = 0 and the
            // largest along t = 1: scan it, then zoom in around the best cells
            double quarter = Math.PI / 2;
            List<double[]> cells = new ArrayList<>();
            for (int i = 0; i < GRID; i++) {
                for (int j = 0; j < GRID; j++) {
                    double ti = (double) i / (GRID - 1);
                    double pj = quarter * j / (GRID - 1);
                    cells.add(new double[] {cost(frame(ti, pj)), ti, pj});
                }
            }
            cells.sort((x, y) -> Double.compare(x[0], y[0]));
            for (int k = 0; k < STARTS; k++) {
                double[] here = cells.get(k).clone();
                double dt = 1.0 / (GRID - 1);
                double dp = quarter / (GRID - 1);
                for (int z = 0; z < ZOOMS; z++) {
                    double tc = here[1];
                    double pc = here[2];
                    for (int a = -ZOOM; a <= ZOOM; a++) {
                        double ta = Math.min(1, Math.max(0, tc + a * dt / ZOOM));
                        for (int b = -ZOOM; b <= ZOOM; b++) {
                            double pb = pc + b * dp / ZOOM;
                            double c = cost(frame(ta, pb));
                            if (c < here[0]) {
                                here = new double[] {c, ta, pb};
                            }
                        }
                    }
                    dt /= ZOOM;
                    dp /= ZOOM;
                }
                result = frame(here[1], here[2]);
                if (spread(result) <= NEAR * scale) {
                    break;
                }
            }
        }
        // polish by small turns of the frame about its own axes
        double best = cost(result);
        double step = spread(result) > NEAR * scale ? FIRST_TURN : TINY * 2;
        for (int round = 0; round < ROUNDS && step > TINY; round++) {
            boolean moved = false;
            for (int k = 0; k < DIM; k++) {
                for (int sign = -1; sign <= 1; sign += 2) {
                    double[][] cand = result.clone();
                    for (int i = 0; i < DIM; i++) {
                        if (i != k) {
                            cand[i] = turn(result[i], result[k], sign * step);
                        }
                    }
                    double c = cost(cand);
                    if (c < best) {
                        best = c;
                        result = cand;
                        moved = true;
                    }
                }
            }
            if (!moved) {
                step /= 2;
            }
        }
        show(result);
    }
}
