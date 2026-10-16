import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final int STEPS = 100;
    static double[] mass, purity;
    static Integer[] order;

    // gold, in grams times a thousand, in the first t grams of the bars laid
    // out from the poorest to the richest
    static double goldBefore(double t) {
        double gold = 0;
        for (int i : order) {
            double part = Math.min(mass[i], t);
            if (part <= 0) break;
            gold += part * purity[i];
            t -= part;
        }
        return gold;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        double need = Double.parseDouble(st.nextToken());
        double fineness = Double.parseDouble(st.nextToken());
        mass = new double[n];
        purity = new double[n];
        order = new Integer[n];
        double total = 0;
        for (int i = 0; i < n; i++) {
            mass[i] = Double.parseDouble(st.nextToken());
            purity[i] = Double.parseDouble(st.nextToken());
            total += mass[i];
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> Double.compare(purity[a], purity[b]));
        double target = need * fineness;
        // a window of the needed weight sliding from the poorest end to the
        // richest gains gold steadily, so it hits the target if anything does
        if (total < need || window(0, need) > target || window(total - need, need) < target) {
            System.out.println("NO");
            return;
        }
        double low = 0, high = total - need;
        for (int step = 0; step < STEPS; step++) {
            double mid = (low + high) / 2;
            if (window(mid, need) < target) low = mid;
            else high = mid;
        }
        double start = (low + high) / 2;
        double[] take = new double[n];
        double left = 0;
        for (int i : order) {
            double right = left + mass[i];
            take[i] = Math.max(0, Math.min(right, start + need) - Math.max(left, start));
            left = right;
        }
        StringBuilder sb = new StringBuilder("YES\n");
        for (int i = 0; i < n; i++) sb.append(String.format(Locale.US, "%.10f%n", take[i]));
        System.out.print(sb);
    }

    static double window(double s, double need) {
        return goldBefore(s + need) - goldBefore(s);
    }
}
