import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] prefixFunction(String t) {
        int[] p = new int[t.length()];
        for (int i = 1, k = 0; i < t.length(); i++) {
            while (k > 0 && t.charAt(i) != t.charAt(k)) {
                k = p[k - 1];
            }
            if (t.charAt(i) == t.charAt(k)) {
                k++;
            }
            p[i] = k;
        }
        return p;
    }

    // the first occurrence of t in s[from, to), or -1
    static int find(String s, int from, int to, String t, int[] p) {
        int k = 0;
        for (int i = from; i < to; i++) {
            while (k > 0 && s.charAt(i) != t.charAt(k)) {
                k = p[k - 1];
            }
            if (s.charAt(i) == t.charAt(k) && ++k == t.length()) {
                return i - k + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String source = in.readLine();
        String[] target = in.readLine().split(" ");
        boolean[] keep = new boolean[source.length()];
        int j = 0;
        int[] p = prefixFunction(target[0]);
        // each wanted word goes to its earliest place in the current word,
        // at least one erased letter after the previous one there; if it
        // does not fit, the next word of the source is tried
        for (int begin = 0; begin < source.length() && j < target.length; ) {
            int end = source.indexOf(' ', begin);
            if (end < 0) {
                end = source.length();
            }
            for (int pos = begin; j < target.length && end - pos >= target[j].length(); ) {
                int at = find(source, pos, end, target[j], p);
                if (at < 0) {
                    break;
                }
                for (int i = at; i < at + target[j].length(); i++) {
                    keep[i] = true;
                }
                pos = at + target[j].length() + 1;
                if (++j < target.length) {
                    p = prefixFunction(target[j]);
                }
            }
            begin = end + 1;
        }
        if (j < target.length) {
            System.out.println("I HAVE FAILED!!!");
            return;
        }
        char[] out = source.toCharArray();
        for (int i = 0; i < out.length; i++) {
            if (out[i] != ' ' && !keep[i]) {
                out[i] = '_';
            }
        }
        System.out.println(new String(out));
    }
}
