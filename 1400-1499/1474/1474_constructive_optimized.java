import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine().trim());
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        output.write((n * (n + 2) + "\n").getBytes(StandardCharsets.US_ASCII));

        byte[][] tokens = new byte[2 * n + 1][];
        for (int i = 0; i < tokens.length; i++)
            tokens[i] = (" " + i).getBytes(StandardCharsets.US_ASCII);

        int hole = n, direction = 1;
        for (int run = 0; run <= 2 * n; run++) {
            int length = Math.min(run + 1, Math.min(n, 2 * n - run + 1));
            // Rising runs slide last and falling runs slide first.
            int slide = run < n ? length - 1 : (run > n ? 0 : -1);
            for (int i = 0; i < length; i++) {
                hole += (i == slide ? 1 : 2) * direction;
                int skip = run == 0 ? 1 : 0;
                output.write(tokens[hole], skip, tokens[hole].length - skip);
            }
            direction = -direction;
        }
        output.write('\n');
        output.flush();
    }
}
