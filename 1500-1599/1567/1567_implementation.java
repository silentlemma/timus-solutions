import java.io.*;

public class Main {
    // the characters of each key in the order of presses; the space has a key
    // of its own
    static final String[] KEYS = {"abc", "def", "ghi", "jkl", "mno", "pqr",
                                  "stu", "vwx", "yz",  ".,!", " "};

    public static void main(String[] args) throws IOException {
        // the whole first line, spaces included; anything else costs nothing
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
        int total = 0;
        for (char c : (line == null ? "" : line).toCharArray())
            for (String key : KEYS) {
                int at = key.indexOf(c);
                if (at >= 0)
                    total += at + 1;
            }
        System.out.println(total);
    }
}
