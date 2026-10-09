import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] left = new int[n], right = new int[n];
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            left[i] = in.nextInt();
            right[i] = in.nextInt();
            if (left[i] > right[i]) {
                int t = left[i];
                left[i] = right[i];
                right[i] = t;
            }
            order[i] = i;
        }
        // a segment inside another is strictly shorter, so by length the inner
        // one always comes first
        Arrays.sort(order, (a, b) -> Integer.compare(right[a] - left[a], right[b] - left[b]));
        int[] best = new int[n], prev = new int[n];
        Arrays.fill(best, 1);
        Arrays.fill(prev, -1);
        for (int p = 0; p < n; p++) {
            int i = order[p];
            for (int q = 0; q < p; q++) {
                int j = order[q];
                if (left[i] < left[j] && right[j] < right[i] && best[j] + 1 > best[i]) {
                    best[i] = best[j] + 1;
                    prev[i] = j;
                }
            }
        }
        int end = 0;
        for (int i = 1; i < n; i++) {
            if (best[i] > best[end]) {
                end = i;
            }
        }
        List<Integer> chain = new ArrayList<>();
        for (; end >= 0; end = prev[end]) {
            chain.add(end + 1);
        }
        Collections.reverse(chain);
        StringBuilder out = new StringBuilder();
        out.append(chain.size()).append("\n");
        for (int i = 0; i < chain.size(); i++) {
            out.append(i > 0 ? " " : "").append(chain.get(i));
        }
        System.out.println(out);
    }
}
