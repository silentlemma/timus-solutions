import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] words = new String[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            words[i] = in.readLine().trim();
            total += words[i].length();
        }
        // every suffix of every command, sorted; a substring starting at some
        // position is in another command exactly when it is a prefix of another
        // command's suffix, and the nearest such suffixes in the order share most
        String[] texts = new String[total];
        Integer[] order = new Integer[total];
        int[] owner = new int[total];
        int at = 0;
        for (int i = 0; i < n; i++) {
            for (int p = 0; p < words[i].length(); p++) {
                texts[at] = words[i].substring(p);
                owner[at] = i;
                order[at] = at;
                at++;
            }
        }
        Arrays.sort(order, (a, b) -> texts[a].compareTo(texts[b]));
        int[] adjacent = new int[total];
        for (int k = 0; k + 1 < total; k++) {
            String a = texts[order[k]];
            String b = texts[order[k + 1]];
            int l = 0;
            while (l < a.length() && l < b.length() && a.charAt(l) == b.charAt(l)) {
                l++;
            }
            adjacent[k] = l;
        }
        int[] shared = new int[total]; // the longest prefix shared with another command
        int run = 0;
        for (int k = 1; k < total; k++) {
            boolean other = owner[order[k]] != owner[order[k - 1]];
            run = other ? adjacent[k - 1] : Math.min(run, adjacent[k - 1]);
            shared[k] = run;
        }
        run = 0;
        for (int k = total - 2; k >= 0; k--) {
            boolean other = owner[order[k]] != owner[order[k + 1]];
            run = other ? adjacent[k] : Math.min(run, adjacent[k]);
            shared[k] = Math.max(shared[k], run);
        }
        String[] best = new String[n];
        for (int k = 0; k < total; k++) {
            String text = texts[order[k]];
            int w = owner[order[k]];
            int need = shared[k] + 1;
            if (need <= text.length() && (best[w] == null || need < best[w].length())) {
                best[w] = text.substring(0, need);
            }
        }
        StringBuilder out = new StringBuilder();
        for (String b : best) {
            out.append(b).append('\n');
        }
        System.out.print(out);
    }
}
