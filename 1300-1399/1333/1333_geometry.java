import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int STRIPS = 20000;
    static final double PERCENT = 100;
    static final double MIDDLE = 0.5; // where in its strip the line is taken

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        int n = in.nextInt();
        double[] cx = new double[n], cy = new double[n], r = new double[n];
        for (int i = 0; i < n; i++) {
            cx[i] = in.nextDouble();
            cy[i] = in.nextDouble();
            r[i] = in.nextDouble();
        }
        // the area is the sum over thin vertical strips of the covered part of
        // the line through the middle of each strip
        double covered = 0;
        double[][] pieces = new double[n][];
        for (int k = 0; k < STRIPS; k++) {
            double x = (k + MIDDLE) / STRIPS;
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (Math.abs(x - cx[i]) < r[i]) {
                    double half = Math.sqrt(r[i] * r[i] - (x - cx[i]) * (x - cx[i]));
                    double low = Math.max(0, cy[i] - half), high = Math.min(1, cy[i] + half);
                    if (low < high)
                        pieces[count++] = new double[] {low, high};
                }
            }
            Arrays.sort(pieces, 0, count, (a, b) -> Double.compare(a[0], b[0]));
            double end = 0;
            for (int i = 0; i < count; i++) {
                if (pieces[i][1] > end) {
                    covered += pieces[i][1] - Math.max(pieces[i][0], end);
                    end = pieces[i][1];
                }
            }
        }
        System.out.println(String.format(Locale.US, "%.6f", covered / STRIPS * PERCENT));
    }
}
