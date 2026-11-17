import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
    static final String TAIL = "bcd";

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine().trim());
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] letters = new char[n];
        Arrays.fill(letters, 'a');
        char[] suffix = new char[n];
        for (int i = 0; i < n; i++) {
            suffix[i] = TAIL.charAt(i % TAIL.length());
        }

        int first = Math.min(n, TAIL.length());
        for (int count = 1; count <= n; count++) {
            output.write(Integer.toString(count));
            output.write(" : ");
            if (count < first) {
                output.write("NO");
            } else {
                int prefix = n < TAIL.length() ? n : count - TAIL.length();
                output.write(letters, 0, prefix);
                output.write(suffix, 0, n - prefix);
            }
            output.newLine();
        }
        output.flush();
    }
}
