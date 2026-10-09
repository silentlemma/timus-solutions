import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        // cutting a shorter piece off a longer one keeps the gcd of all lengths,
        // so the last piece is always the gcd and the answer is never ambiguous
        long g = 0;
        for (int i = 0; i < n; i++) {
            long length = Long.parseLong(st.nextToken());
            while (length != 0) {
                long t = g % length;
                g = length;
                length = t;
            }
        }
        System.out.println(g);
    }
}
