import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        // the scale shows x times all the bars plus y - x times the platinum
        // ones, so the counts must have pairwise different subset sums; the
        // Conway-Guy sets u_n - u_i do, with the smallest largest count known
        long[] u = new long[n + 1];
        u[1] = 1;
        for (int m = 1; m < n; m++) {
            int r = (int) Math.round(Math.sqrt(2.0 * m));
            u[m + 1] = 2 * u[m] - u[m - r];
        }
        if (u[n] > k) {
            System.out.println("NO");
            return;
        }
        StringBuilder out = new StringBuilder("YES\n");
        for (int i = 0; i < n; i++) {
            out.append(u[n] - u[i]).append(i + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
