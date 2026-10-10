import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // the left half with its middle digit, copied backwards onto the right half
    static String mirror(char[] digits) {
        char[] out = digits.clone();
        for (int i = 0; i < out.length / 2; i++) {
            out[out.length - 1 - i] = out[i];
        }
        return new String(out);
    }

    public static void main(String[] args) throws IOException {
        String s = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        String best = mirror(s.toCharArray());
        // same length strings of digits compare like the numbers they spell
        if (best.compareTo(s) < 0) {
            // add one to the left half with its middle digit; it is not all nines,
            // since all nines mirror to the largest number of this length
            char[] half = s.toCharArray();
            int k = (s.length() + 1) / 2 - 1;
            while (half[k] == '9') {
                half[k--] = '0';
            }
            half[k]++;
            best = mirror(half);
        }
        System.out.println(best);
    }
}
