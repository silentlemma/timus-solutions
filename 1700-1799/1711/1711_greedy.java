import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int CHOICES = 3; // names offered for every problem

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            all.append(line).append(' ');
        }
        StringTokenizer tokens = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tokens.nextToken());
        String[][] names = new String[n][CHOICES];
        for (String[] options : names) {
            for (int j = 0; j < CHOICES; j++) {
                options[j] = tokens.nextToken();
            }
            Arrays.sort(options);
        }
        // in the given order, the least name above the previous one leaves the
        // most room for the problems still to come
        StringBuilder out = new StringBuilder();
        String last = "";
        for (int i = 0; i < n; i++) {
            int p = Integer.parseInt(tokens.nextToken()) - 1;
            String next = null;
            for (String name : names[p]) {
                if (name.compareTo(last) > 0) {
                    next = name;
                    break;
                }
            }
            if (next == null) {
                System.out.println("IMPOSSIBLE");
                return;
            }
            last = next;
            out.append(last).append('\n');
        }
        System.out.print(out);
    }
}
