import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < n; k++) {
            // kids take the first free horse at or after a random one: linear
            // probing on a circle of n slots with k taken. By Knuth's analysis
            // the wait is (Q - 1)/2 with Q = sum (j + 1) k!/(k - j)! / n^j
            double q = 0, term = 1;
            for (int j = 0; j <= k; j++) {
                q += (j + 1) * term;
                term *= (double) (k - j) / n;
            }
            out.append(String.format("%.9f", (q - 1) / 2)).append('\n');
        }
        System.out.print(out);
    }
}
