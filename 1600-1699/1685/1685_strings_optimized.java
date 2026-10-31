import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    static String text;
    static char[] out;
    static int at;
    // midpoint recursion has logarithmic depth and avoids two allocated ranges per character.
    static void decode(int lo, int hi) {
        if (lo >= hi)
            return;
        int mid = (lo + hi - 1) / 2;
        out[mid] = text.charAt(at++);
        decode(lo, mid);
        decode(mid + 1, hi);
    }
    public static void main(String[] args) throws java.io.IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        text = in.readLine();
        if (text == null)
            text = "";
        out = new char[text.length()];
        // the encoded text lists the middle of a range, then its left part,
        // then its right part: replay that order and put each letter back
        decode(0, text.length());
        System.out.println(out);
    }
}
