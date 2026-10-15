import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    static String[] words(String text) {
        String trimmed = text.trim();
        return trimmed.isEmpty() ? new String[0] : trimmed.split("\\s+");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        Map<String, Set<String>> known = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String line = in.readLine();
            int colon = line.indexOf(':');
            known.put(line.substring(0, colon),
                    new HashSet<>(Arrays.asList(words(line.substring(colon + 1)))));
        }
        int m = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String[] names = words(in.readLine());
            // the common associations are the intersection of the sets
            TreeSet<String> common = new TreeSet<>(known.get(names[0]));
            for (String name : names) {
                common.retainAll(known.get(name));
            }
            out.append(common.isEmpty() ? "No solution." : String.join(" ", common)).append('\n');
        }
        System.out.print(out);
    }
}
