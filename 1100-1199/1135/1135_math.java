import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        // a turning pair "><" becomes "<>", a swap of neighbours that removes
        // one pair with '>' before '<', so the count of such pairs is the
        // answer
        long right = 0, turns = 0;
        int seen = 0;
        for (String line = in.readLine(); line != null && seen < n; line = in.readLine()) {
            for (int k = 0; k < line.length() && seen < n; k++) {
                char c = line.charAt(k);
                if (c == '>') {
                    right++;
                    seen++;
                } else if (c == '<') {
                    turns += right;
                    seen++;
                }
            }
        }
        System.out.println(turns);
    }
}
