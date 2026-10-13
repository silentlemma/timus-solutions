import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // numbers of length k without two zeros in a row: Fibonacci F(k + 2), so
        // F(2N) bars go into F(N) safes, and F(2N) = F(N) L(N) with Lucas L(N)
        BigInteger a = BigInteger.valueOf(2), b = BigInteger.ONE; // L(0), L(1)
        for (int i = 0; i < n; i++) {
            BigInteger c = a.add(b);
            a = b;
            b = c;
        }
        System.out.println(a);
    }
}
