import java.util.*;

public class Main {
    static final double EPS = 1e-9; // touching counts as fitting
    static final int SIDES = 3;

    // the third vertex of a triangle on the segment from (0, 0) to (base, 0)
    // whose other sides are left (from the origin) and right
    static double[] apex(double base, double left, double right) {
        double x = (base * base + left * left - right * right) / (2 * base);
        return new double[] {x, Math.sqrt(Math.max(0, left * left - x * x))};
    }

    // can the card lie with its side card[0] on the envelope's side env[0], in
    // either of its two mirror images?
    static boolean fitsOn(double[] env, double[] card) {
        double m = env[0], length = card[0];
        if (length > m + EPS)
            return false;
        double[] w = apex(m, env[1], env[2]);
        double wx = w[0], height = w[1];
        for (int mirror = 0; mirror < 2; mirror++) {
            double[] a = apex(length, card[1 + mirror], card[2 - mirror]);
            double u = a[0], h = a[1];
            if (h > height + EPS)
                continue;
            // the card slides along the side by t in [0, m - length]; its apex
            // (t + u, h) must stay between the envelope's two other sides
            double lo = Math.max(0, h * wx / height - u);
            double hi = Math.min(m - length, m - h * (m - wx) / height - u);
            if (lo <= hi + EPS)
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] e = new int[SIDES], c = new int[SIDES];
        for (int i = 0; i < SIDES; i++)
            e[i] = in.nextInt();
        for (int i = 0; i < SIDES; i++)
            c[i] = in.nextInt();
        Arrays.sort(e);
        Arrays.sort(c);
        boolean fits = false;
        if (e[0] + e[1] == e[2]) {
            // a flat envelope holds only a flat card that is no longer
            fits = c[0] + c[1] == c[2] && c[2] <= e[2];
        } else {
            // a triangle fits in another one exactly when it fits with one of its
            // sides lying on a side of the other
            for (int i = 0; i < SIDES; i++)
                for (int j = 0; j < SIDES; j++) {
                    double[] env = new double[SIDES], card = new double[SIDES];
                    for (int k = 0; k < SIDES; k++) {
                        env[k] = e[(i + k) % SIDES];
                        card[k] = c[(j + k) % SIDES];
                    }
                    fits = fits || fitsOn(env, card);
                }
        }
        System.out.println(fits ? "YES" : "NO");
    }
}
