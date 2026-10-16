import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final double R = 8.314;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // lines "X = value"
        Map<String, Double> known = new HashMap<>();
        while (in.hasNext()) {
            String name = in.next();
            in.next();
            known.put(name, (double) in.nextInt());
        }
        double p = known.getOrDefault("p", 0.0), n = known.getOrDefault("n", 0.0);
        double v = known.getOrDefault("V", 0.0), t = known.getOrDefault("T", 0.0);
        // p V = n R T, with V and T strictly positive
        if (!known.containsKey("p")) {
            System.out.printf("p = %.6f%n", n * R * t / v);
        } else if (!known.containsKey("n")) {
            System.out.printf("n = %.6f%n", p * v / (R * t));
        } else {
            // the unknown is V (beside p) or T (beside n R), and both must
            // be positive: a zero factor leaves 0 = 0 or a contradiction
            boolean findV = !known.containsKey("V");
            double factor = findV ? p : n, other = findV ? n : p;
            if (factor == 0 && other == 0) {
                System.out.println("undefined");
            } else if (factor == 0 || other == 0) {
                System.out.println("error");
            } else if (findV) {
                System.out.printf("V = %.6f%n", n * R * t / p);
            } else {
                System.out.printf("T = %.6f%n", p * v / (n * R));
            }
        }
    }
}
