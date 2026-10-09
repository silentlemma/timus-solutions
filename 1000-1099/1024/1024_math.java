import java.util.Scanner;

public class Main {
    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] p = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            p[i] = in.nextInt();
        }
        // P^k is the identity exactly when k is a multiple of every cycle length:
        // the order is their least common multiple
        boolean[] seen = new boolean[n + 1];
        long order = 1;
        for (int i = 1; i <= n; i++) {
            long length = 0;
            for (int j = i; !seen[j]; j = p[j]) {
                seen[j] = true;
                length++;
            }
            if (length > 0) {
                order = order / gcd(order, length) * length;
            }
        }
        System.out.println(order);
    }
}
