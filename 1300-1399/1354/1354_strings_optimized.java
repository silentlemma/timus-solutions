import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        String word = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        int n = word.length();
        // n <= 10000: char stores prefix lengths exactly in two bytes.
        char[] border = new char[n];
        // index the reversed word directly instead of building a doubled string.
        for (int i = 1; i < n; i++) {
            int k = border[i - 1];
            while (k > 0 && word.charAt(n - 1 - i) != word.charAt(n - 1 - k))
                k = border[k - 1];
            if (word.charAt(n - 1 - i) == word.charAt(n - 1 - k))
                k++;
            border[i] = (char)k;
        }
        int longest = 0;
        // a proper tail ensures that the appended word is nonempty.
        for (int i = 1; i < n; i++) {
            while (longest > 0 && word.charAt(i) != word.charAt(n - 1 - longest))
                longest = border[longest - 1];
            if (word.charAt(i) == word.charAt(n - 1 - longest))
                longest++;
        }
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        out.write(word);
        for (int i = n - longest - 1; i >= 0; i--)
            out.write(word.charAt(i));
        out.newLine();
        out.flush();
    }
}
