import java.util.Scanner;

public class Main {
    // inputs are at most this
    static final int LARGEST = 10;

    public static void main(String[] args) {
        // a(n) counts weak orders of n objects: the k objects tied for the
        // smallest place are any k of them, followed by a weak order of the rest
        long[][] binom = new long[LARGEST + 1][LARGEST + 1];
        long[] a = new long[LARGEST + 1];
        a[0] = 1;
        for (int n = 0; n <= LARGEST; n++) {
            binom[n][0] = 1;
            binom[n][n] = 1;
            for (int k = 1; k < n; k++) {
                binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k];
            }
        }
        for (int n = 1; n <= LARGEST; n++) {
            for (int k = 1; k <= n; k++) {
                a[n] += binom[n][k] * a[n - k];
            }
        }
        Scanner in = new Scanner(System.in);
        StringBuilder out = new StringBuilder();
        while (in.hasNextInt()) {
            int n = in.nextInt();
            if (n < 0) {
                break;
            }
            out.append(a[n]).append('\n');
        }
        System.out.print(out);
    }
}
