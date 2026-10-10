import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // n is a product of two odd primes, so trial division starts here
    static final long SMALLEST = 3;

    static long power(long b, long e, long n) {
        long r = 1;
        for (b %= n; e > 0; e /= 2, b = b * b % n) {
            if (e % 2 == 1) {
                r = r * b % n;
            }
        }
        return r;
    }

    // the inverse of e modulo phi by the extended Euclidean algorithm
    static long inverse(long e, long phi) {
        long a = e % phi, b = phi, x = 1, y = 0;
        while (b != 0) {
            long q = a / b, t = a - q * b;
            a = b;
            b = t;
            t = x - q * y;
            x = y;
            y = t;
        }
        return (x % phi + phi) % phi;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int k = (int)in.nval;
        StringBuilder out = new StringBuilder();
        while (k-- > 0) {
            in.nextToken();
            long e = (long)in.nval;
            in.nextToken();
            long n = (long)in.nval;
            in.nextToken();
            long c = (long)in.nval;
            long p = SMALLEST;
            while (n % p != 0) {
                p += 2;
            }
            long phi = (p - 1) * (n / p - 1);
            // m^(e d) = m modulo n when e d = 1 modulo phi, so the private
            // exponent d undoes the public one
            out.append(power(c, inverse(e, phi), n)).append('\n');
        }
        System.out.print(out);
    }
}
