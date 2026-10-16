import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int MOST = 100;
    // how many letters may be taken off each end before undoing a doubling
    static final int EDGE = 5;
    // the fewest phrases and the letters taken off the front and the back,
    // with a negative front for the letters one by one
    static Map<String, int[]> best = new HashMap<>();

    // the word whose doubling is core, or null if core is no double
    static String halve(String core) {
        StringBuilder half = new StringBuilder();
        for (int i = 0; i < core.length(); i += 2) {
            if (core.charAt(i) == core.charAt(i + 1)) return null;
            half.append(core.charAt(i));
        }
        return half.toString();
    }

    // the fewest phrases that build s: either all letters one by one, or a few
    // letters at each end around the double of a shorter word; a word free of
    // these repeats always has that shape with short ends
    static int[] plan(String s) {
        int[] known = best.get(s);
        if (known != null) return known;
        int n = s.length();
        int[] result = {n, -1, 0};
        for (int a = 0; a <= EDGE && a <= n; a++) {
            for (int b = 0; b <= EDGE && a + b <= n; b++) {
                int len = n - a - b;
                if (len < 2 || len % 2 == 1) continue;
                String half = halve(s.substring(a, n - b));
                if (half == null) continue;
                int cost = a + b + 1 + plan(half)[0];
                if (cost < result[0]) result = new int[] {cost, a, b};
            }
        }
        best.put(s, result);
        return result;
    }

    static void phrases(String s, List<String> out) {
        int[] p = plan(s);
        if (p[1] < 0) {
            for (char c : s.toCharArray()) out.add("back " + c);
            return;
        }
        int n = s.length();
        phrases(halve(s.substring(p[1], n - p[2])), out);
        out.add("double");
        for (int i = p[1] - 1; i >= 0; i--) out.add("front " + s.charAt(i));
        for (int i = n - p[2]; i < n; i++) out.add("back " + s.charAt(i));
    }

    public static void main(String[] args) throws IOException {
        String word = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        if (plan(word)[0] > MOST) {
            System.out.println(-1);
            return;
        }
        List<String> out = new ArrayList<>();
        phrases(word, out);
        StringBuilder sb = new StringBuilder();
        sb.append(out.size()).append('\n');
        for (String line : out) sb.append(line).append('\n');
        System.out.print(sb);
    }
}
