import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    // test 6 was removed and new tests were added after test 7, which became
    // test 6: a failure on old test 7 must now read 6, while an accepted run or
    // a failure on old test 6 may change or stay as it was
    static final int REMOVED = 6;
    static final int RENUMBERED = 7;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            all.append(line).append(' ');
        }
        StringTokenizer tokens = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tokens.nextToken());
        Set<String> must = new HashSet<>();
        Set<String> any = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String name = tokens.nextToken();
            String verdict = tokens.nextToken();
            if (verdict.equals("ML") || verdict.equals("TL") || verdict.equals("WA")) {
                int test = Integer.parseInt(tokens.nextToken());
                if (test == RENUMBERED) {
                    must.add(name);
                    any.add(name);
                } else if (test == REMOVED) {
                    any.add(name);
                }
            } else if (verdict.equals("AC")) {
                any.add(name);
            }
        }
        System.out.println(must.size() + " " + any.size());
    }
}
