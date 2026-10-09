import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    static final int JURY = 255;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int size = in.nextInt(), park = in.nextInt(), m = in.nextInt();
        int[] w = new int[m], s = new int[m], x = new int[m], y = new int[m];
        for (int i = 0; i < m; i++) {
            w[i] = in.nextInt();
            s[i] = in.nextInt();
            x[i] = in.nextInt();
            y[i] = in.nextInt();
        }
        int top = size - park + 1;
        // sliding the park left only drops plots until its left side reaches a
        // plot's right side or the border, so only those positions are tried
        TreeSet<Integer> xs = new TreeSet<>(), ys = new TreeSet<>();
        xs.add(1);
        ys.add(1);
        for (int i = 0; i < m; i++) {
            if (x[i] + s[i] <= top) {
                xs.add(x[i] + s[i]);
            }
            if (y[i] + s[i] <= top) {
                ys.add(y[i] + s[i]);
            }
        }
        int best = JURY;
        for (int px : xs) {
            for (int py : ys) {
                int worst = 1;
                for (int i = 0; i < m; i++) {
                    if (px < x[i] + s[i] && x[i] < px + park && py < y[i] + s[i] &&
                        y[i] < py + park) {
                        worst = Math.max(worst, w[i]);
                    }
                }
                best = Math.min(best, worst);
            }
        }
        System.out.println(best == JURY ? "IMPOSSIBLE" : String.valueOf(best));
    }
}
