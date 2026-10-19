import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(all.toString());
        String text = st.nextToken();
        String name = st.nextToken();
        int n = text.length();
        int m = name.length();
        // the name can be written from position j on when each of its
        // letters lands on that letter or on a "?"
        boolean[] fits = new boolean[n - m + 1];
        for (int j = 0; j + m <= n; j++) {
            fits[j] = true;
            for (int i = 0; i < m && fits[j]; i++) {
                char c = text.charAt(j + i);
                if (c != '?' && c != name.charAt(i)) {
                    fits[j] = false;
                }
            }
        }
        // two copies d < m apart agree exactly when d is a period of the
        // name; copies far apart never meet, and a set of copies agrees as
        // soon as each copy agrees with the next one
        int[] border = new int[m];
        for (int i = 1, k = 0; i < m; i++) {
            while (k > 0 && name.charAt(k) != name.charAt(i)) {
                k = border[k - 1];
            }
            if (name.charAt(k) == name.charAt(i)) {
                k++;
            }
            border[i] = k;
        }
        List<Integer> periods = new ArrayList<>();
        for (int k = border[m - 1]; k > 0; k = border[k - 1]) {
            periods.add(m - k);
        }
        // best[j]: the most copies with the last one at j; before[j]: the
        // most with the last one before j
        int[] best = new int[n - m + 1];
        int[] before = new int[n - m + 2];
        for (int j = 0; j + m <= n; j++) {
            if (fits[j]) {
                int previous = j >= m ? before[j - m + 1] : 0;
                for (int d : periods) {
                    if (d <= j) {
                        previous = Math.max(previous, best[j - d]);
                    }
                }
                best[j] = previous + 1;
            }
            before[j + 1] = Math.max(before[j], best[j]);
        }
        System.out.println(before[n - m + 1]);
    }
}
