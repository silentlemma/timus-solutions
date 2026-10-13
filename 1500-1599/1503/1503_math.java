import java.io.*;
import java.util.*;

public class Main {
    static final int STEPS = 200; // halvings of the search interval: far below the 1e-6 asked
    static final int QUARTIC = 4;

    static double value(double[] poly, double x) {
        double s = 0;
        for (double c : poly)
            s = s * x + c;
        return s;
    }

    // points where poly changes sign inside (lo, hi); between neighbouring
    // sign changes of the derivative the polynomial is monotone
    static List<Double> signRoots(double[] poly, double lo, double hi) {
        List<Double> found = new ArrayList<>();
        if (poly.length < 2)
            return found;
        int n = poly.length - 1;
        double[] deriv = new double[n];
        for (int i = 0; i < n; i++)
            deriv[i] = poly[i] * (n - i);
        List<Double> cuts = new ArrayList<>();
        cuts.add(lo);
        cuts.addAll(signRoots(deriv, lo, hi));
        cuts.add(hi);
        for (int k = 0; k + 1 < cuts.size(); k++) {
            double a = cuts.get(k), b = cuts.get(k + 1);
            int sa = (int)Math.signum(value(poly, a)), sb = (int)Math.signum(value(poly, b));
            if (sa == 0 || sb == 0 || sa == sb)
                continue;
            for (int it = 0; it < STEPS; it++) {
                double mid = (a + b) / 2;
                if ((int)Math.signum(value(poly, mid)) == sa)
                    a = mid;
                else
                    b = mid;
            }
            found.add((a + b) / 2);
        }
        return found;
    }

    // a root p/q of poly as {p, q}, or null
    static long[] rationalRoot(long[] poly) {
        long lead = Math.abs(poly[0]), last = Math.abs(poly[poly.length - 1]);
        for (long q = 1; q <= lead; q++) {
            if (lead % q != 0)
                continue;
            for (long pa = 1; pa <= last; pa++) {
                if (last % pa != 0)
                    continue;
                for (long p : new long[] {pa, -pa}) {
                    // q^n f(p/q), exact in integers
                    long s = 0, qp = 1;
                    for (long c : poly) {
                        s = s * p + c * qp;
                        qp *= q;
                    }
                    if (s == 0)
                        return new long[] {p, q};
                }
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] poly = new long[n + 1]; // the leading coefficient first
        for (int i = 0; i <= n; i++) {
            in.nextToken();
            poly[i] = (long)in.nval;
        }
        List<Double> roots = new ArrayList<>();
        // rational roots p/q, with p dividing the constant term and q the
        // leading one; dividing by (q x - p) keeps integer coefficients
        while (poly.length > 1 && poly[poly.length - 1] == 0) {
            roots.add(0.0);
            poly = Arrays.copyOf(poly, poly.length - 1);
        }
        long[] pq;
        while (poly.length > 1 && (pq = rationalRoot(poly)) != null) {
            long p = pq[0], q = pq[1];
            long[] out = new long[poly.length - 1];
            out[0] = poly[0] / q;
            for (int i = 1; i < out.length; i++)
                out[i] = (poly[i] + p * out[i - 1]) / q;
            poly = out;
            roots.add((double)p / q);
        }
        // what is left has no rational roots; a repeated irrational root would
        // need its quadratic twice, so only a0 (x^2 + b x + d)^2 can repeat
        if (poly.length == QUARTIC + 1) {
            long a0 = poly[0], c3 = poly[1], c2 = poly[2], c1 = poly[QUARTIC - 1],
                 c0 = poly[QUARTIC];
            long u = QUARTIC * a0, e = u * c2 - c3 * c3; // then b = 2 c3 / u, d = 2 e / u^2
            if (2 * c3 * e == c1 * u * u && e * e == c0 * u * u * u) {
                long w = c3 * c3 - 2 * e; // the roots are (-c3 +- sqrt(w)) / u
                if (w > 0)
                    for (double r :
                         new double[] {(-c3 - Math.sqrt(w)) / u, (-c3 + Math.sqrt(w)) / u}) {
                        roots.add(r);
                        roots.add(r);
                    }
                poly = new long[] {1};
            }
        }
        double[] rest = new double[poly.length];
        for (int i = 0; i < poly.length; i++)
            rest[i] = poly[i];
        double bound = 1;
        for (int i = 1; i < rest.length; i++)
            bound = Math.max(bound, 1 + Math.abs(rest[i] / rest[0]));
        roots.addAll(signRoots(rest, -bound, bound));
        Collections.sort(roots);
        StringBuilder sb = new StringBuilder();
        for (double r : roots)
            sb.append(String.format(Locale.US, "%.10f", r)).append('\n');
        System.out.print(sb);
    }
}
