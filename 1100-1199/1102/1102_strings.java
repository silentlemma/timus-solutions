import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int MAX_TOTAL_LENGTH = 4000000;
    static final String[] WORDS = {"out", "output", "puton", "in", "input", "one"};

    static boolean dialogue(char[] line, int end) {
        // no dictionary word is a suffix of another, so the final word is unique.
        while (end > 0) {
            int cut = -1;
            for (String word : WORDS) {
                int start = end - word.length();
                if (start < 0)
                    continue;
                int i = 0;
                while (i < word.length() && line[start + i] == word.charAt(i))
                    ++i;
                if (i == word.length())
                    cut = start;
            }
            if (cut < 0)
                return false;
            end = cut;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        // all lines together contain at most four million letters.
        // one character array avoids the temporary copies made by readline.
        char[] line = new char[MAX_TOTAL_LENGTH];
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; ++i) {
            int length = 0;
            for (int c; (c = in.read()) != -1 && c != '\n';)
                if (c != '\r')
                    line[length++] = (char)c;
            out.append(dialogue(line, length) ? "YES\n" : "NO\n");
        }
        System.out.print(out);
    }
}
