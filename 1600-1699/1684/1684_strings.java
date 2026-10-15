import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        int left = 0;
        int right = 0;
        for (int i = 1; i < n; i++) {
            int k = i < right ? Math.min(z[i - left], right - i) : 0;
            while (i + k < n && s.charAt(k) == s.charAt(i + k)) {
                k++;
            }
            z[i] = k;
            if (i + k > right) {
                left = i;
                right = i + k;
            }
        }
        return z;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(all.toString());
        String word = words.nextToken();
        String last = words.nextToken();
        int m = word.length();
        int n = last.length();
        int[] z = zFunction(word + "#" + last);
        // from a cut at position p the next piece can end anywhere in
        // p + 1 .. p + z[p]; so the reachable cuts are always 0 .. reach
        int[] parent = new int[n + 1];
        int reach = 0;
        for (int p = 0; p <= reach && p < n; p++) {
            int far = p + z[m + 1 + p];
            for (int q = reach + 1; q <= far; q++) {
                parent[q] = p;
            }
            reach = Math.max(reach, far);
        }
        if (reach < n) {
            System.out.println("Yes");
            return;
        }
        List<String> pieces = new ArrayList<>();
        for (int q = n; q > 0; q = parent[q]) {
            pieces.add(last.substring(parent[q], q));
        }
        Collections.reverse(pieces);
        System.out.println("No\n" + String.join(" ", pieces));
    }
}
