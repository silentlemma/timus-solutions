import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    static final int MINUTE = 60, HOUR = MINUTE * MINUTE, DAY = 24 * HOUR;
    static final String ELEMENTS = "AEFW";
    // values closer than this are taken as equal
    static final double EPS = 1e-9;
    // the fields of an element: strong moment and power, weak moment and power
    static final int STRONG = 0, TOP = 1, WEAK = 2, LOW = 3;

    static Map<Character, int[]> moments = new HashMap<>();
    static Map<Character, Integer> side = new HashMap<>();

    static int seconds(String text) {
        String[] parts = text.split(":");
        return Integer.parseInt(parts[0]) * HOUR + Integer.parseInt(parts[1]) * MINUTE +
            Integer.parseInt(parts[2]);
    }

    // the power falls linearly from the strong moment to the weak one and
    // rises back over the rest of the day
    static double power(int[] e, int t) {
        int strong = e[STRONG], top = e[TOP], weak = e[WEAK], low = e[LOW];
        int fall = Math.floorMod(weak - strong, DAY), since = Math.floorMod(t - strong, DAY);
        if (since <= fall) {
            return top + (double)(low - top) * since / fall;
        }
        return low + (double)(top - low) * (since - fall) / (DAY - fall);
    }

    static double advantage(int t) {
        double sum = 0;
        for (char e : ELEMENTS.toCharArray()) {
            int c = side.getOrDefault(e, 0);
            if (c != 0) {
                sum += c * power(moments.get(e), t);
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int k = 0; k < ELEMENTS.length(); k++) {
            char code = in.next().charAt(0);
            int strong = seconds(in.next()), top = in.nextInt();
            int weak = seconds(in.next()), low = in.nextInt();
            moments.put(code, new int[] {strong, top, weak, low});
        }
        for (char c : in.next().toCharArray()) {
            side.merge(c, 1, Integer::sum);
        }
        for (char c : in.next().toCharArray()) {
            side.merge(c, -1, Integer::sum);
        }
        // the advantage is linear between the moments, so its largest value
        // over the day is at a moment or at either end of the day
        TreeSet<Integer> times = new TreeSet<>();
        times.add(0);
        times.add(DAY - 1);
        for (int[] e : moments.values()) {
            times.add(e[STRONG]);
            times.add(e[WEAK]);
        }
        int when = -1;
        double best = 0;
        for (int t : times) {
            double v = advantage(t);
            if (when < 0 || v > best + EPS) {
                best = v;
                when = t;
            }
        }
        if (best <= EPS) {
            System.out.println("We can't win!");
        } else {
            // rounded from the exact binary value, half to even, as printf in C
            String value = new BigDecimal(best).setScale(2, RoundingMode.HALF_EVEN).toPlainString();
            System.out.printf(Locale.US, "%02d:%02d:%02d%n%s%n", when / HOUR,
                              when / MINUTE % MINUTE, when % MINUTE, value);
        }
    }
}
