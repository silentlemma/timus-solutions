import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final long R_NUM = 8314, R_DEN = 1000, SCALE = 1000000;

    static void printValue(String name, long numerator, long denominator) {
        long value = (numerator * SCALE + denominator / 2) / denominator;
        System.out.printf(Locale.ROOT, "%s = %d.%06d%n", name, value / SCALE, value % SCALE);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // lines "X = value"
        Map<String, Long> known = new HashMap<>();
        while (in.hasNext()) {
            String name = in.next();
            in.next();
            known.put(name, in.nextLong());
        }
        long p = known.getOrDefault("p", 0L), n = known.getOrDefault("n", 0L);
        long v = known.getOrDefault("V", 0L), t = known.getOrDefault("T", 0L);
        // p V = n R T, with V and T strictly positive
        if (!known.containsKey("p")) {
            printValue("p", n * R_NUM * t, R_DEN * v);
        } else if (!known.containsKey("n")) {
            printValue("n", p * v * R_DEN, R_NUM * t);
        } else {
            // the unknown is V (beside p) or T (beside n R), and both must
            // be positive: a zero factor leaves 0 = 0 or a contradiction
            boolean findV = !known.containsKey("V");
            long factor = findV ? p : n, other = findV ? n : p;
            if (factor == 0 && other == 0) {
                System.out.println("undefined");
            } else if (factor == 0 || other == 0) {
                System.out.println("error");
            } else if (findV) {
                printValue("V", n * R_NUM * t, R_DEN * p);
            } else {
                printValue("T", p * v * R_DEN, n * R_NUM);
            }
        }
    }
}
