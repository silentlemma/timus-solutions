import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        long s = in.nextLong();
        long yes = s - 2 * n; // YES takes 3 bytes, NO takes 2
        long no = n - yes;
        // the first test fails when its answer is NO, any later one when its
        // answer differs from the one before: no / n + (n - 1) * 2 yes no / (n (n - 1))
        System.out.println(String.format(Locale.US, "%.7f", (double) (no * (2 * yes + 1)) / n));
    }
}
