import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringJoiner;

public class Main {
    static final String UNKNOWN = "unknown";

    // every block of size phrases is one language, and no language is used in
    // two blocks
    static boolean fits(String[] phrases, int size) {
        Set<String> used = new HashSet<>();
        for (int start = 0; start < phrases.length; start += size) {
            String lang = null;
            for (int i = start; i < start + size; i++) {
                if (phrases[i].equals(UNKNOWN)) {
                    continue;
                }
                if (lang == null) {
                    lang = phrases[i];
                }
                if (!phrases[i].equals(lang)) {
                    return false;
                }
            }
            if (lang != null && !used.add(lang)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] phrases = new String[n];
        for (int i = 0; i < n; i++) {
            phrases[i] = in.readLine().trim();
        }
        StringJoiner counts = new StringJoiner(" ");
        for (int k = 1; k <= n; k++) {
            if (n % k == 0 && fits(phrases, n / k)) {
                counts.add(Integer.toString(k));
            }
        }
        System.out.println(counts.length() == 0 ? "Igor is wrong." : counts.toString());
    }
}
