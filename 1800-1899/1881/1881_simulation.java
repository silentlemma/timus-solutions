import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        int h = Integer.parseInt(words.nextToken());
        int w = Integer.parseInt(words.nextToken());
        int n = Integer.parseInt(words.nextToken());
        int lines = 1;
        int used = -1;
        for (int i = 0; i < n; i++) {
            int length = words.nextToken().length();
            // a word after another one on the line needs a space before it
            if (used + 1 + length > w) {
                lines++;
                used = -1;
            }
            used += 1 + length;
        }
        System.out.println((lines + h - 1) / h);
    }
}
