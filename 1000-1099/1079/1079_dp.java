import java.util.Scanner;

public class Main {
    static final int TOP = 99999;

    public static void main(String[] args) {
        int[] a = new int[TOP + 1], best = new int[TOP + 1];
        a[1] = best[1] = 1;
        for (int i = 2; i <= TOP; i++) {
            a[i] = i % 2 == 0 ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
            best[i] = Math.max(best[i - 1], a[i]);
        }
        Scanner in = new Scanner(System.in);
        StringBuilder out = new StringBuilder();
        while (in.hasNextInt()) {
            int n = in.nextInt();
            if (n == 0) {
                break;
            }
            out.append(best[n]).append("\n");
        }
        System.out.print(out);
    }
}
