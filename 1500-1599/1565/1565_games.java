import java.util.*;
import java.math.BigInteger;

public class Main {
    static final int SHOOTERS = 3;
    static final int INDEX_SUM = 0 + 1 + 2;
    static final int RATIO_DIGITS = 16;
    static final int OUTPUT_SCALE = 100000;
    // absorbs floating-point noise at output rounding midpoints
    static final double ROUND_EPS = 1e-8;

    static double[] acc = new double[SHOOTERS];
    static int[] order = new int[SHOOTERS];

    static String[] values = new String[SHOOTERS];
    static BigInteger[] exact = new BigInteger[SHOOTERS];
    static int stronger, weaker;
    static boolean[] attack = new boolean[2];

    static double ratio(int first, int second) {
        String a = values[first], b = values[second];
        String x = a.substring(0, Math.min(RATIO_DIGITS, a.length()));
        String y = b.substring(0, Math.min(RATIO_DIGITS, b.length()));
        int exponent = (a.length() - x.length()) - (b.length() - y.length());
        return (Double.parseDouble(x) / Double.parseDouble(y)) * Math.pow(10, exponent);
    }

    // two left, first to shoot: first wins p / (p + q - p q)
    static double[] duel(int first, int second) {
        double p = acc[first], q = acc[second];
        double[] c = new double[SHOOTERS];
        if (exact[first].compareTo(exact[second]) >= 0)
            c[first] = 1 / (1 + ratio(second, first) * (1 - p));
        else {
            double r = ratio(first, second);
            c[first] = r / (1 + r * (1 - q));
        }
        c[second] = 1 - c[first];
        return c;
    }

    // the duel left after a hit, with the next living shooter first
    static double[] afterHit(int turn, int killed) {
        int first = order[(turn + 1) % SHOOTERS];
        if (first == killed)
            first = order[(turn + 2) % SHOOTERS];
        return duel(first, INDEX_SUM - killed - first);
    }

    // chances when all three live and order[turn] shoots; A never misses, so
    // the shooting stops at A's turn at the latest
    static double[] three(int turn) {
        int shooter = order[turn];
        if (shooter == 0)
            return afterHit(turn, stronger);
        double p = acc[shooter];
        double[] miss = three((turn + 1) % SHOOTERS);
        // the weaker shooter attacks A iff (1-h)^k (1-l) >= h; ties attack
        int nextIsStronger = order[(turn + 1) % SHOOTERS] != 0 ? 1 : 0;
        if (shooter == weaker && !attack[nextIsStronger])
            return miss;
        double[] hit = afterHit(turn, 0), mixed = new double[SHOOTERS];
        for (int i = 0; i < SHOOTERS; i++)
            mixed[i] = p * hit[i] + (1 - p) * miss[i];
        return mixed;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        String[] tokens = new String[SHOOTERS];
        int precision = 0;
        for (int i = 0; i < SHOOTERS; i++) {
            tokens[i] = in.next();
            acc[i] = Double.parseDouble(tokens[i]);
            int point = tokens[i].indexOf('.');
            if (point >= 0)
                precision = Math.max(precision, tokens[i].length() - point - 1);
        }
        for (int i = 0; i < SHOOTERS; i++) {
            int point = tokens[i].indexOf('.');
            int fraction = point < 0 ? 0 : tokens[i].length() - point - 1;
            StringBuilder text = new StringBuilder(tokens[i].replace(".", ""));
            for (int j = fraction; j < precision; j++)
                text.append('0');
            exact[i] = new BigInteger(text.toString());
            values[i] = exact[i].toString();
        }
        stronger = exact[1].compareTo(exact[2]) > 0 ? 1 : 2;
        weaker = INDEX_SUM - stronger;
        BigInteger scale = BigInteger.TEN.pow(precision);
        BigInteger high = exact[stronger], low = exact[weaker];
        BigInteger complement = scale.subtract(high);
        BigInteger product = complement.multiply(scale.subtract(low));
        BigInteger bound = high.multiply(scale);
        attack[0] = low.signum() == 0 || product.compareTo(bound) >= 0;
        attack[1] = low.signum() == 0
                    || product.multiply(complement).compareTo(bound.multiply(scale)) >= 0;
        double[] total = new double[SHOOTERS];
        int orders = 0;
        for (int a = 0; a < SHOOTERS; a++)
            for (int b = 0; b < SHOOTERS; b++) {
                if (b == a)
                    continue;
                order = new int[] {a, b, INDEX_SUM - a - b};
                double[] c = three(0);
                for (int i = 0; i < SHOOTERS; i++)
                    total[i] += c[i];
                orders++;
            }
        double share = 1.0 / orders;
        int[] rounded = new int[SHOOTERS];
        for (int i = 0; i < SHOOTERS; i++)
            rounded[i] = (int)(total[i] * share * OUTPUT_SCALE + 0.5 + ROUND_EPS);
        System.out.printf(Locale.US, "%d.%05d %d.%05d %d.%05d\n",
                          rounded[0] / OUTPUT_SCALE, rounded[0] % OUTPUT_SCALE,
                          rounded[1] / OUTPUT_SCALE, rounded[1] % OUTPUT_SCALE,
                          rounded[2] / OUTPUT_SCALE, rounded[2] % OUTPUT_SCALE);
    }
}
