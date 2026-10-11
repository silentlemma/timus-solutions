import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int CHARS = 128;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int k = Integer.parseInt(words.nextToken());
        char[] last = words.nextToken().toCharArray();
        int n = last.length;
        // a stable counting sort of the last column: row order[j] ends with
        // the j-th character of the sorted column, the first one of row j
        int[] start = new int[CHARS + 1];
        for (char c : last)
            start[c + 1]++;
        for (int c = 0; c < CHARS; c++)
            start[c + 1] += start[c];
        int[] order = new int[n];
        for (int i = 0; i < n; i++)
            order[start[last[i]]++] = i;
        char[] text = new char[n];
        int row = k - 1;
        for (int i = 0; i < n; i++) {
            row = order[row];
            text[i] = last[row];
        }
        System.out.println(new String(text));
    }
}
