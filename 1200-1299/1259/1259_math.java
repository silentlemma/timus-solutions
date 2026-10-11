import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // Euler's totient: the turns 2*pi*m/n with gcd(m, n) = 1
        int phi = n, rest = n;
        for (int p = 2; p * p <= rest; p++) {
            if (rest % p == 0) {
                while (rest % p == 0)
                    rest /= p;
                phi -= phi / p;
            }
        }
        if (rest > 1)
            phi -= phi / rest;
        System.out.println(phi / 2);
    }
}
