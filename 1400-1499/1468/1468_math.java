import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final String DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    static String whole(int x, int k) {
        StringBuilder out = new StringBuilder();
        do {
            out.append(DIGITS.charAt(x % k));
            x /= k;
        } while (x != 0);
        return out.reverse().toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder out = new StringBuilder();
        while (true) {
            int a = in.nextInt(), b = in.nextInt();
            if (a == 0 && b == 0)
                break;
            int k = in.nextInt();
            StringBuilder text = new StringBuilder(whole(a / b, k));
            int rest = a % b;
            if (rest != 0) {
                // long division; a remainder seen before starts the period
                int[] seen = new int[b];
                Arrays.fill(seen, -1);
                StringBuilder frac = new StringBuilder();
                while (rest != 0 && seen[rest] < 0) {
                    seen[rest] = frac.length();
                    rest *= k;
                    frac.append(DIGITS.charAt(rest / b));
                    rest %= b;
                }
                if (rest != 0)
                    frac.insert(seen[rest], '(').append(')');
                text.append('.').append(frac);
            }
            out.append(text).append('\n');
        }
        System.out.print(out);
    }
}
