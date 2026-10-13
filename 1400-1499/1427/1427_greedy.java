import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer first = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(first.nextToken()), m = Integer.parseInt(first.nextToken());
        String text = in.readLine(); // read whole: the text may start with spaces
        if (text == null)
            text = "";
        int len = text.length();
        // run[i]: how many letters and spaces start at position i
        int[] run = new int[len + 1];
        for (int i = len - 1; i >= 0; i--) {
            char c = text.charAt(i);
            if (c == ' ' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
                run[i] = run[i + 1] + 1;
        }
        // the farthest reach never moves back, so the longest message each time is best
        int pos = 0, count = 0;
        while (pos < len) {
            pos += Math.max(n, Math.min(m, run[pos]));
            count++;
        }
        System.out.println(count);
    }
}
