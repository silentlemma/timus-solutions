import java.io.*;
import java.util.*;
import java.util.function.DoubleUnaryOperator;

public class Main {
    static final int STEPS = 70;   // golden-section steps: the bracket shrinks by 0.618 each
    static final int SAMPLES = 24; // first look along circle B, before refining
    static final double GOLD = (Math.sqrt(5) - 1) / 2;
    static double hx, hy, bx, r;

    // the least value of a function with one minimum on [lo, hi]
    static double golden(DoubleUnaryOperator f, double lo, double hi) {
        double a = hi - GOLD * (hi - lo), b = lo + GOLD * (hi - lo);
        double fa = f.applyAsDouble(a), fb = f.applyAsDouble(b);
        for (int i = 0; i < STEPS; i++) {
            if (fa < fb) {
                hi = b;
                b = a;
                fb = fa;
                a = hi - GOLD * (hi - lo);
                fa = f.applyAsDouble(a);
            } else {
                lo = a;
                a = b;
                fa = fb;
                b = lo + GOLD * (hi - lo);
                fb = f.applyAsDouble(b);
            }
        }
        return Math.min(fa, fb);
    }

    // the shortest way from P to the circle of dog B and on home
    static double toB(double px, double py) {
        double dx = hx - px, dy = hy - py, length = Math.hypot(dx, dy);
        double t = length > 0
                       ? Math.min(Math.max(((bx - px) * dx - py * dy) / (length * length), 0), 1)
                       : 0;
        if (Math.hypot(px + t * dx - bx, py + t * dy) <= r)
            return length;
        DoubleUnaryOperator via = phi -> {
            double qx = bx + r * Math.cos(phi), qy = r * Math.sin(phi);
            return Math.hypot(qx - px, qy - py) + Math.hypot(hx - qx, hy - qy);
        };
        double step = 2 * Math.PI / SAMPLES;
        int best = 0;
        for (int k = 1; k < SAMPLES; k++)
            if (via.applyAsDouble(k * step) < via.applyAsDouble(best * step))
                best = k;
        return golden(via, (best - 1) * step, (best + 1) * step);
    }

    static double next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        double r1 = next(in), r2 = next(in), r3 = next(in);
        r = next(in);
        // a dog is fed from the house itself: then the tour goes to the other
        // dog's circle and back, and nothing shorter exists
        if (Math.min(r1, r2) <= r) {
            System.out.println(
                String.format(Locale.ROOT, "%.3f", 2 * Math.max(Math.max(r1, r2) - r, 0)));
            return;
        }
        // posts at (0, 0) and (r3, 0), the house above them
        hx = r3 > 0 ? (r1 * r1 - r2 * r2 + r3 * r3) / (2 * r3) : r1;
        hy = Math.sqrt(Math.max(r1 * r1 - hx * hx, 0));
        bx = r3;
        // the tour length is convex in P inside dog A's circle, so a golden
        // search over x of golden searches over y finds its least value
        DoubleUnaryOperator column = px -> {
            double half = Math.sqrt(Math.max(r * r - px * px, 0));
            return golden(py -> Math.hypot(hx - px, hy - py) + toB(px, py), -half, half);
        };
        System.out.println(String.format(Locale.ROOT, "%.3f", golden(column, -r, r)));
    }
}
