import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double SECONDS = 10;
    // once a whole line is done with this certainty the rest of the sum is lost
    // in rounding
    static final double SURE = 1e-15;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int m = n - 2;
        // done[i]: the chance that i rockets between two launched ones are all
        // launched within the volleys counted so far; a stretch of i rockets
        // splits at a random one into stretches of l and i - 1 - l
        double[] done = new double[m + 1];
        done[0] = 1;
        double volleys = 0;
        for (int j = 1; j <= m; j++) {
            volleys += 1 - done[m];
            double[] before = done.clone();
            for (int i = 0; i <= m; i++) {
                if (i <= j) {
                    done[i] = 1;
                    continue;
                }
                double sum = 0;
                for (int l = 0; l < i; l++) sum += before[l] * before[i - 1 - l];
                done[i] = sum / i;
            }
            if (1 - done[m] < SURE) break;
        }
        System.out.println(String.format(Locale.US, "%.11f", SECONDS * volleys));
    }
}
