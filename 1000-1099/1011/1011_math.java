import java.util.Scanner;

public class Main {
    static final long HUNDREDTHS = 100, WHOLE = 100 * HUNDREDTHS;

    // A percentage with at most two decimals, in hundredths of a percent.
    static long hundredths(String s) {
        int dot = s.indexOf('.');
        String integerPart = dot < 0 ? s : s.substring(0, dot);
        long integer = integerPart.isEmpty() ? 0 : Long.parseLong(integerPart);
        String fraction = (dot < 0 ? "" : s.substring(dot + 1)) + "00";
        return integer * HUNDREDTHS + Long.parseLong(fraction.substring(0, 2));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long p = hundredths(in.next()), q = hundredths(in.next());
        // the fewest conductors above p are p*n/WHOLE + 1, and n is the answer
        // as soon as their share is below q
        for (long n = 1;; n++) {
            long c = p * n / WHOLE + 1;
            if (c * WHOLE < q * n) {
                System.out.println(n);
                return;
            }
        }
    }
}
