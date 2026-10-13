import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    static List<Long> primesOf(long n) {
        List<Long> found = new ArrayList<>();
        for (long p = 2; p * p <= n; p++)
            if (n % p == 0) {
                found.add(p);
                while (n % p == 0)
                    n /= p;
            }
        if (n > 1)
            found.add(n);
        return found;
    }

    static long power(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1)
                result = result * base % mod;
            base = base * base % mod;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong(), n = in.nextLong();
        if (gcd(a, n) != 1) { // the remainders keep a common factor with N and never reach 1
            System.out.println(0);
            return;
        }
        // the order divides phi(N): strip prime factors while a power stays 1
        long phi = n;
        for (long p : primesOf(n))
            phi = phi / p * (p - 1);
        long order = phi;
        for (long p : primesOf(phi))
            while (order % p == 0 && power(a, order / p, n) == 1)
                order /= p;
        System.out.println(order);
    }
}
