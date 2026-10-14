import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int stops = 2 * n;
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < n; k++) {
            // k, k + 1, k - 1, k + 2, k - 2, ..., k + n around the circle of stops:
            // its neighbouring pairs are exactly those with sum 2k or 2k + 1
            out.append(k + 1);
            for (int j = 1; j <= n; j++) {
                out.append(' ').append((k + j) % stops + 1);
                if (j < n)
                    out.append(' ').append((k - j + stops) % stops + 1);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
