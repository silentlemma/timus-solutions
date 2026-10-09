import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashSet;
import java.util.Set;

public class Main {
    static Set<String> known = new LinkedHashSet<>();
    static int errors = 0;

    static String fix(String word) {
        if (known.contains(word)) {
            return word;
        }
        // only a single wrong letter is corrected, never a missing or extra one
        for (String d : known) {
            if (d.length() != word.length()) {
                continue;
            }
            int diff = 0;
            for (int i = 0; i < d.length(); i++) {
                if (d.charAt(i) != word.charAt(i)) {
                    diff++;
                }
            }
            if (diff == 1) {
                errors++;
                return d;
            }
        }
        return word;
    }

    static boolean isLetter(char c) { return c >= 'a' && c <= 'z'; }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null && !line.trim().equals("#")) {
            if (!line.trim().isEmpty()) {
                known.add(line.trim());
            }
        }
        StringBuilder out = new StringBuilder();
        while ((line = in.readLine()) != null) {
            for (int i = 0; i < line.length();) {
                if (!isLetter(line.charAt(i))) {
                    out.append(line.charAt(i++));
                    continue;
                }
                int j = i;
                while (j < line.length() && isLetter(line.charAt(j))) {
                    j++;
                }
                out.append(fix(line.substring(i, j)));
                i = j;
            }
            out.append("\n");
        }
        out.append(errors).append("\n");
        System.out.print(out);
    }
}
