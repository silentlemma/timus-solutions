import java.util.*;

public class Main {
    static final double NODE = Math.sqrt(0.6); // outer three-point Gauss-Legendre nodes
    static final double OUTER = 5, MIDDLE = 8, TOTAL = 9; // its weights, as 5/9 and 8/9
    static final double TOLERANCE = 1e-13;
    static final int DEPTH = 50;
    static final double LIMIT = 20; // sinh(20) is about 2.4e8: the tails beyond are negligible
    static double a0, a1, a2, a3, a4;

    // x = sinh t, dx = cosh t dt: the infinite line becomes a finite range
    static double f(double t) {
        double x = Math.sinh(t);
        return Math.cosh(t) / ((((a4 * x + a3) * x + a2) * x + a1) * x + a0);
    }

    static double gauss(double lo, double hi) {
        double mid = (lo + hi) / 2, half = (hi - lo) / 2;
        double nodes = OUTER * f(mid - half * NODE) + MIDDLE * f(mid);
        nodes += OUTER * f(mid + half * NODE);
        return half * nodes / TOTAL;
    }

    // adaptive: split while the halves disagree with the whole
    static double integrate(double lo, double hi, double whole, int depth) {
        double mid = (lo + hi) / 2;
        double left = gauss(lo, mid), right = gauss(mid, hi), both = left + right;
        if (depth == 0 || Math.abs(both - whole) <= TOLERANCE * (1 + Math.abs(both)))
            return both;
        return integrate(lo, mid, left, depth - 1) + integrate(mid, hi, right, depth - 1);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        a0 = in.nextDouble();
        a1 = in.nextDouble();
        a2 = in.nextDouble();
        a3 = in.nextDouble();
        a4 = in.nextDouble();
        double result = integrate(-LIMIT, LIMIT, gauss(-LIMIT, LIMIT), DEPTH);
        System.out.println(String.format(Locale.ROOT, "%.10f", result));
    }
}
