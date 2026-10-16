import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    // times in tenths of a second; starts are 30 seconds apart
    static final int TENTHS_PER_MINUTE = 600, TENTHS_PER_SECOND = 10, GAP = 300;

    static int tenths(String text) {
        int colon = text.indexOf(':'), dot = text.indexOf('.');
        int minutes = Integer.parseInt(text.substring(0, colon));
        int seconds = Integer.parseInt(text.substring(colon + 1, dot));
        int tenth = Integer.parseInt(text.substring(dot + 1));
        return minutes * TENTHS_PER_MINUTE + seconds * TENTHS_PER_SECOND + tenth;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] names = new String[n];
        int[] runs = new int[n];
        Integer[] byFinish = new Integer[n];
        for (int i = 0; i < n; i++) {
            names[i] = in.next();
            runs[i] = tenths(in.next());
            byFinish[i] = i;
        }
        Arrays.sort(byFinish, (a, b) -> Integer.compare(a * GAP + runs[a], b * GAP + runs[b]));
        // replay the finishes in order; the board changes on every new best run
        List<String> leaders = new ArrayList<>();
        int best = -1;
        for (int i : byFinish) {
            if (best < 0 || runs[i] < best) {
                best = runs[i];
                leaders.add(names[i]);
            }
        }
        Collections.sort(leaders);
        StringBuilder out = new StringBuilder();
        out.append(leaders.size()).append('\n');
        for (String name : leaders) {
            out.append(name).append('\n');
        }
        System.out.print(out);
    }
}
