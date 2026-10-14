import java.util.*;

public class Main {
    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        // the chance that the row ends with two cards: (n^2 + 3n - 2) / (2n (2n - 1))
        long num = n * (n + 2) + n - 2;
        long den = 2 * n * (2 * n - 1);
        long g = gcd(num, den);
        System.out.println(num / g + "/" + den / g);
    }
}
