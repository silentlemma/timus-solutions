import java.util.*;

public class Main {
    static final long FOUR = 4, SEVEN = 7, EIGHT = 8;
    static final long RESIDUE = 3;   // the primes 4k + 3
    static final long FIRST_ODD = 3; // the first odd divisor to try
    static final int THREE_SQUARES = 3, FOUR_SQUARES = 4;

    static boolean isSquare(long n) {
        long r = (long)Math.sqrt((double)n);
        while (r * r > n)
            r--;
        while ((r + 1) * (r + 1) <= n)
            r++;
        return r * r == n;
    }

    // Fermat: every prime 4k + 3 must appear an even number of times
    static boolean twoSquares(long n) {
        while (n % 2 == 0)
            n /= 2;
        for (long d = FIRST_ODD; d * d <= n; d += 2) {
            int count = 0;
            while (n % d == 0) {
                n /= d;
                count++;
            }
            if (d % FOUR == RESIDUE && count % 2 == 1)
                return false;
        }
        // what is left is 1 or a prime
        return n % FOUR != RESIDUE;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long n = in.nextLong();
        long m = n;
        while (m % FOUR == 0)
            m /= FOUR;
        if (isSquare(n))
            System.out.println(1);
        else if (twoSquares(n))
            System.out.println(2);
        // Legendre: exactly the numbers 4^a (8b + 7) need four
        else if (m % EIGHT == SEVEN)
            System.out.println(FOUR_SQUARES);
        else
            System.out.println(THREE_SQUARES);
    }
}
